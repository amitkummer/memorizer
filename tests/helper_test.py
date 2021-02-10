from memorizer import helper

import pytest

@pytest.fixture
def json_folder(tmp_path):
    tmp_path.joinpath('1.json').touch()
    tmp_path.joinpath('2.json').touch()
    tmp_path.joinpath('3.json').touch()
    return tmp_path

def test_count_json(json_folder):
    assert helper.countJsonFiles(json_folder) == 3
