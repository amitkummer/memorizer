from pathlib import Path

import memorizer


def test_equals_diff_case():
    assert memorizer.equals("A", "a")

def test_eqals_has_spaces():
    assert memorizer.equals("a", " a ")

def test_sampled_size():
    p = Path('.').joinpath('data').joinpath('test.json')
    result = memorizer.sampleWordsFromFile(p, 2)
    assert len(result) == 2