import os
from typing import List

from app.engine.errors import ParsingError
from app.engine.tree import build_ast


import pytest
from app.engine.tree import build_ast


def get_lookml_files() ->List[str]:
    files = []
    directory = os.path.join(os.getcwd(), 'test', 'fixtures')
    extension = '.lkml'

    for f in os.listdir(directory):
        if f.endswith(extension):
            lookml_file_path = os.path.join(directory, f)
            files.append(lookml_file_path)
    return files


@pytest.mark.parametrize("input_file", get_lookml_files())
def test_build_ast(input_file):
    # Read the input file
    # import pdb
    # pdb.set_trace()

    # Call build_ast and check if it raises any errors
    try:
        build_ast(input_file)
    except Exception as e:
        pytest.fail(f"build_ast raised an error: {e}")
