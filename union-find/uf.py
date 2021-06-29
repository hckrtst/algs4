#!/bin/python3
import sys

if __name__ == '__main__':
  line = None
  try:
    while True:
      line = input('> ')
      # if empty input we are done
      if (not len(line)):
        break
  except:
      pass
  print('bye')