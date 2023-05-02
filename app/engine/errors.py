from typing import Any

from antlr4 import Parser, Token
from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    """Custom error listener that raises a SyntaxError when a syntax error is detected."""

    def syntaxError(
        self,
        recognizer: Parser,
        offendingSymbol: Token,
        line: int,
        column: int,
        msg: str,
        e: Any,
    ) -> SyntaxError:
        """
        Raise a SyntaxError when a syntax error is detected in the input stream.

        Args:
            recognizer (Parser): The parser instance.
            offendingSymbol (Token): The offending token in the input stream.
            line (int): The line number where the error occurred.
            column (int): The column number where the error occurred.
            msg (str): The error message.
            e (Any): The RecognitionException instance if available, otherwise None.
        """
        error_message = (
            f"Syntax error detected at line {line}, column {column}:\n"
            f"  {msg}\n"
            f"Parser instance: {recognizer}\n"
            f"Offending token: {offendingSymbol}\n"
            f"RecognitionException (if any): {e}"
        )
        raise SyntaxError(error_message)

class ParsingError(Exception):
    """Custom exception class for parsing errors."""