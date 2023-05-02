import os
import sys
import unittest

from app.engine.errors import ParsingError
from app.engine.tree import build_ast

class TestAstBuilder(unittest.TestCase):

    def test_build_ast(self):
        # Setup
        directory = os.path.join(os.getcwd(), 'app', 'fixtures')
        extension = '.lkml'

        for f in os.listdir(directory):
            if f.endswith(extension):
                lookml_file_path = os.path.join(directory, f)
                with self.subTest(file=f):
                    try:
                        # Exercise
                        parse_tree = build_ast(lookml_file_path)
                        
                        # Verify
                        self.assertIsNotNone(parse_tree)
                    except ParsingError as e:
                        # Cleanup
                        self.fail(f"Unexpected ParsingError: {e}")


if __name__ == '__main__':
    unittest.main()
