#!/usr/bin/env python3

import os
import sys
from enum import Enum

class Token:
    PLUS = 0,
    NUM  = 1

    def __init__(self):
        self.type = None
        self.src  = None



class Lexer:
    pass


# ================== Main ==================

def main():
    source = "5 + 5"
    print("Hello lang")


if __name__ == '__main__':
    main()
