from pathlib import Path

def countJsonFiles(path):
    count = 0
    for child in path.iterdir():
        if child.suffix == '.json':
            count += 1
    return count