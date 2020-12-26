from argparse import ArgumentParser
from pathlib import Path
import random
import json
import fileinput

def run():
    parser = ArgumentParser(prog='memorizer')
    parser.add_argument('--path', type=Path, help='''path to a json file 
    containing words and their meanings''')
    parser.add_argument('--count', type=int, help='''count of words 
    to be randomly sampled from the file and presented as questions''')
    args = parser.parse_args()
    sampledWords = sampleWordsFromFile(args.path, args.count)
    startGame(sampledWords)

def sampleWordsFromFile(path, sampleCount):
    with path.open() as wordsFile:
        words = json.load(wordsFile)
        return random.sample(words, sampleCount)

def startGame(words):
    print('Game is starting! Write your answer and press enter.')
    console = fileinput.input('-')
    for word in words:
        german = word['word']
        meaning = word['meaning']
        print(f'What is the English word for the word: {german}?')
        answer = console.readline()
        if (equals(answer, meaning)):
            print("Your'e answer is correct!")
        else:
            print(f'Wrong! The correct answer is: {meaning}')

def equals(first, second):
    return first.lower().strip() == second.lower().strip()