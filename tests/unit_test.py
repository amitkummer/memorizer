from pathlib import Path

import memorizer

def test_equals_diff_case():
    assert memorizer.equals("A", "a")

def test_eqals_has_spaces():
    assert memorizer.equals("a", " a ")

def test_sampled_size_from_file():
    p = Path('tests').joinpath('data').joinpath('test.json')
    result = memorizer.sampleWordsFromFile(p, 2)
    assert len(result) == 2

def test_sample_size_bigger_than_file_size():
    p = Path('tests').joinpath('data').joinpath('test.json')
    result = memorizer.sampleWordsFromFile(p, 200)
    assert len(result) == 3

def test_sample_size_from_dir():
    p = Path('tests').joinpath('data')
    words = memorizer.sampleWordsFromDir(p, 4)
    assert len(words) == 4

def test_sample_size_bigger_than_dir_size():
    p = Path('tests').joinpath('data')
    result = memorizer.sampleWordsFromDir(p, 200)
    assert len(result) == 6