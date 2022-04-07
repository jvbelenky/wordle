#!/usr/bin/python

class Helpers:
    """
    Class for some useful helper functions
    """
    def make_iters(known_letters:dict)->int:

        """make iterable of possible word combinations"""
        iters = [[(letter,pos) for pos in positions] for letter, positions in known_letters.items()]
        combos=[]
        for a in iters[0]:
            for b in iters[1]:
                if a[1]!=b[1]:
                    combos.append([a,b])
        return combos

    def get_blanks(word:list)->list:
        """ return the index of blank letters"""
        return [i for i, x in enumerate(word) if x == "_"]