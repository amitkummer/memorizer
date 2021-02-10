from argparse import ArgumentParser
from pathlib import Path
import random
import json
import sys

from rich.console import Console

console = Console() 

def run():
    parser = ArgumentParser(prog='memorizer')
    parser.add_argument('--path', type=Path, required=True,
        help='Path to a json file containing words and their meanings.')
    parser.add_argument('--count', type=int, help='''Count of words 
    to be randomly sampled from the file and presented as questions.
    If ommitted all words in file will be picked.''')
    args = parser.parse_args()
    sampledWords = sampleWordsFromFile(args.path, args.count)
    startGame(sampledWords)

def sampleWordsFromDir(path, sampleCount):
    '''
    Sample group is all words in files that are inside the directory @path.
    '''
    words = []
    for file in path.iterdir():
        if file.suffix == '.json':
            with file.open(encoding='UTF-8') as file:
                words.extend(json.load(file))
    if (sampleCount == None):
        sampleCount = len(words)
    if (len(words) < sampleCount):
        sampleCount = len(words)
        console.print('Warning: count argument is bigger than' +
        'words count in file. All words in file are picked.',
        style="yellow")
    return random.sample(words, sampleCount)
    
def sampleWordsFromFile(path, sampleCount):
    '''
    Sample group is all words in the file @path.
    '''
    with path.open(encoding='UTF-8') as wordsFile:
        words = json.load(wordsFile)
        if (sampleCount == None):
            sampleCount = len(words)
        if (len(words) < sampleCount):
            sampleCount = len(words)
            console.print('Warning: count argument is bigger than' +
            'words count in file. All words in file are picked.',
            style="yellow")
        return random.sample(words, sampleCount)        

def startGame(words):
    console.print('✨ Welcome to Memorizer! ✨')
    console.print(' * Type exit() to stop the game.')
    console.print(' * Whitespace and casing are ignored.')
    console.print("🖊️ Get ready, we're starting 🖊️")
    mistakes = iterate(words)
    while (len(mistakes) != 0):
        console.print('🔄 Retrying the ones you got wrong.')
        mistakes = iterate(mistakes)
    console.print('👋 Thank you for playing.')

def iterate(words):
    mistakes = []
    for word in words:
        german = word['word']
        meaning = word['meaning']
        answer = console.print(f'Your word is [bold]{german}[/bold], what does it mean?')
        answer = console.input('[green]> ')
        if (equals(answer, "exit()")):
            sys.exit(0)
        if (equals(answer, meaning)):
            console.print('🎉 You got it right 🎉')
        else:
            mistakes.append(word)
            console.print(f'🤨 Sure about that one? It means [bold]{meaning} 🤨')
    return mistakes

def equals(first, second):
    return first.lower().strip() == second.lower().strip()