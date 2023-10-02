#!/usr/bin/env python3

import os, sys
from enum import Enum


class Token:
    PLUS = 0,
    NUMBER  = 1

    def __init__(self, token_type, src):
        self.token_type = token_type
        self.src = src


class Lexer:
    """
    Making lexems for my Parser.
    """

    def __init__(self):
        pass

    # TODO: Create util methods for manipulation of given string.

    def peek(self, relativePosition):
        pass
    
    def next(self, amount):
        pass
    
    def step(self):
        pass



def main():
    source = "5 + 5"
    print(source)


if __name__ == '__main__':
    main()
