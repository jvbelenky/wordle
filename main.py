#!/usr/bin/python
from wordle import guess
from utils import parse, save_wordbank
  
if __name__ == "__main__":
    wordbank = guess(*parse())
    save_wordbank(wordbank)