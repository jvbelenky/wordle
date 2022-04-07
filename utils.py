#!/usr/bin/python
import argparse
from datetime import date
from pathlib import Path

def add_arguments(parser):

    parser.add_argument(
	"-g",
	"--green", 
	type=str, 
	nargs='+',
	help="The letters known, and in the correct position.")
    
    parser.add_argument(
	"-gp",
	"--green-positions", 
	type=int, 
	nargs='+', 
	help="The letters known, and in the correct position.")
    
    parser.add_argument(
	"-y",
	"--yellow", 
	type=str, 
	nargs='+', 
	help="The letters known, with an unknown position.")
    
    parser.add_argument(
	"-yp",
	"--yellow-positions", 
	type=int, 
	nargs='+',
	action='append', 
	help="The possible positions of the known letters with unknown positions.")
    
    parser.add_argument(
      "-ug",
      "--unguessed", 
      type=str, 
      default="", 
      help="A string of all letters not yet guessed")

def clean_args(args):
    
    for pos in args.green_positions:
      if pos>5:
         raise Exception(str(pos)+"is not a valid letter position in Wordle")
    
    for sublist in args.yellow_positions:
      for pos in sublist:
          if pos>5:
              raise Exception("Error in "+str(args.yellow_positions)+" \n"+str(pos)+" is not a valid letter position in Wordle")
    
    green_pos = [pos-1 for pos in args.green_positions]
    yellow_pos = [[pos-1 for pos in sublist] for sublist in args.yellow_positions]
  
  
    green = dict(zip(args.green,green_pos))
    yellow = dict(zip(args.yellow,yellow_pos))
    white = args.unguessed
    return green, yellow, white

def parse(): 
  parser = argparse.ArgumentParser(description='A useful tool for enhanced winning at wordle')
  add_arguments(parser)
  args = parser.parse_args()
  return clean_args(args)

def save_wordbank(wordbank,outpath="./output"):
  
    path = Path(outpath)
    if not path.is_dir():
        os.mkdir(path)
  
    today = date.today()
    fileName = "wordle_"+today.strftime("%d-%m-%Y")+".txt"
    path = path / fileName
    print("saving output to",path)
    
    
    wb = "\n".join(wordbank)
    with open(path, 'w') as f:
      f.write(wb)