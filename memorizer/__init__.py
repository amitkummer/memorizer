from argparse import ArgumentParser
from pathlib import Path
import random
import json
import sys
import re

from rich.console import Console

console = Console() 

def run():
    parser = ArgumentParser(prog='memorizer')
    parser.add_argument('--path', type=Path, required=True,
        help='Path to a json file or folder with json files'
        + 'containing words and their meanings.')
    parser.add_argument('--count', type=int, help='''Count of words 
        to be randomly sampled from the file and presented as questions.
        If ommitted all words in file will be picked.''')
    parser.add_argument('--pattern', type=str, help='''Regex pattern to
        match files with. If there is a match with the file stem words
        from the file will be picked. Applied only when path argument is
        a directory.''')
    args = parser.parse_args()
    sampledWords = []
    if args.path.is_dir():
        sampledWords = sampleWordsFromDir(args.path, args.count, args.pattern)
    else:
        sampledWords = sampleWordsFromFile(args.path, args.count)
    startGame(sampledWords)

def sampleWordsFromDir(path, sampleCount=None, pattern=None):
    '''
    Sample group is all words in files that are inside the directory @pathת
    and match with @pattern if provided.
    '''
    words = []
    for file in path.iterdir():
        if file.suffix == '.json':
            if pattern and not re.match(pattern, file.stem):
                continue
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
    
def sampleWordsFromFile(path, sampleCount=None):
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