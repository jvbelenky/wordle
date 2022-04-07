#!/usr/bin/python

#fuck it. wordle time
import string
from copy import deepcopy
from itertools import combinations, combinations_with_replacement
from helpers import Helpers

def init_string(green: dict)->str:
  """
  initialize a base string with the green letters
  """
  string = list('_____')
  
  if len(green)>0:

    for key,val in green.items():
      string[val] = key
      
  return ''.join([char for char in string])
  

def make_valid_strings(base_word:str ='_____', 
                         known_letters: dict={})->list:
      
      """
      init_string: str, default = `_____`
      known_letters: tuple, default = (``,[])
      """

      if len(base_word)>5:
          raise Exception('word '+base_word+' is '+str(len(base_word))+' characters long, it must be 5!')
      
      base_word = list(base_word)
      
      wordbank = []        
      for iters in Helpers.make_iters(known_letters):
          word = deepcopy(base_word)
          
          for letter,pos in iters:
	    
             word[pos] = letter
             wordbank.append(word)

      return wordbank

def make_final_guesses(wordbank, possible_letters):
      
      num_blanks = len(Helpers.get_blanks(wordbank[0]))
      new_bank = []
      
      combos = list(combinations_with_replacement(possible_letters,num_blanks))
      for a,b in combos:
          for word in wordbank:
	    
              new_word = deepcopy(word)
              blanks = Helpers.get_blanks(word)
              
              new_word[blanks[0]] = a
              new_word[blanks[1]] = b
              
              new_bank.append(new_word)
      
      return [''.join(word) for word in new_bank]
    
def guess(green: dict={},
          yellow: dict={},
          white: str=[])->list:
    """
    green: dict
        dict of known letters and their exact positions
    yellow: dict
        dict of known letters and a list of their possible positions
    white: str
        unguessed letters
    """
    if len(green)>0:
        base_word = init_string(green)
    else:
        base_word = list('_____')

    if len(yellow)>0:
        wordbank = make_valid_strings(base_word=base_word, known_letters=yellow)
    else:
        wordbank = list(base_word)
    
    if len(white)>0:
        final_wordbank = make_final_guesses(wordbank, possible_letters=white)
    else:
        white = string.ascii_uppercase
        final_wordbank = make_final_guesses(wordbank, possible_letters=white)
    return sorted(set(final_wordbank))
