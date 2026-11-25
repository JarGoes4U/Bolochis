import re
import tkinter as tk
from tkinter import messagebox


class BolochisParser:
    def __init__(self, input: str):
        self.input = input.strip()
        self.index = 0
        self.error: str | None = None
        self.declared_functions: set[str] = set()
        self.declared_variables: set[str] = set()

    def consume_space(self) -> None:
        while self.index < len(self.input) and self.input[self.index].isspace():
            self.index += 1

    def match(self, pattern: str) -> str | None:
        self.consume_space()
        match_obj = re.match(pattern, self.input[self.index :])
        if match_obj:
            self.index += match_obj.end()
            return match_obj.group(0).strip()
        return None

    def analize(self) -> bool:
        if not self.input:
            self.error = "Error: Empty input, man."
            return False

        while self.index < len(self.input):
            if not self.content():
                pos = min(self.index, len(self.input) - 1)
                caracter = repr(self.input[pos])
                self.error = (
                    f"Syntax error at {self.index}: "
                    f"Unexpected character {caracter} near {self.input[self.index:]!r}"
                )
                return False

        self.error = "Right, man. No syntax errors found."
        return True

    def content(self) -> bool:
        return (
            self.declare_variable()
            or self.function()
            or self.cycle()
            or self.conditional()
        )
