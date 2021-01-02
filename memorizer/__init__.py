from argparse import ArgumentParser
from pathlib import Path
import random
import json
import fileinput
import sys

from rich.console import Console
from rich.prompt import Prompt

console = Console() 

def run():
    parser = ArgumentParser(prog='memorizer')
    parser.add_argument('--path', type=Path, required=True,
        help='Path to a json file containing words and their meanings')
    parser.add_argument('--count', type=int, help='''Count of words 
    to be randomly sampled from the file and presented as questions.
    If ommitted all words in file will be picked.''')
    args = parser.parse_args()
    sampledWords = sampleWordsFromFile(args.path, args.count)
    startGame(sampledWords)

def sampleWordsFromFile(path, sampleCount):
    with path.open(encoding='UTF-8') as wordsFile:
        words = json.load(wordsFile)
        if (sampleCount == None):
            sampleCount = len(words)
            console.print("Count argument wasn't specified: picking all words.",
            style="cyan")
        if (len(words) < sampleCount):
            sampleCount = len(words)
            console.print('Warning: count argument is bigger than' +
            'words count in file. All words in file are picked.',
            style="yellow")
        return random.sample(words, sampleCount)
            

def startGame(words):
    console.print('Game is starting! Write your answer and press enter.',
    style="green")
    console.print('Type exit() to exit the game.', style='green')
    console.print("Letter's case and spaces are ignored.", style='green')
    console.print("Wrong words will be cycled until correct input.", style='green')
    mistakes = iterate(words)
    while (len(mistakes) != 0):
        mistakes = iterate(mistakes)

def iterate(words):
    input = fileinput.input('-')
    mistakes = []
    for word in words:
        german = word['word']
        meaning = word['meaning']
        answer = Prompt.ask(f'What is the English word for the word: [cyan]{german}?')
        if (equals(answer, "exit()")):
            sys.exit(0)
        if (equals(answer, meaning)):
            console.print("Your'e answer is correct!", style='green')
        else:
            mistakes.append(word)
            console.print(f'Wrong! The correct answer is: [bold]{meaning}',
            style='red')
    input.close()
    return mistakes

def equals(first, second):
    return first.lower().strip() == second.lower().strip()