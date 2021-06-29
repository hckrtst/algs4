#!/bin/python3
import sys

if __name__ == '__main__':
  line = None
  try:
    nums = int(input('How many elements? '))
    while nums:
      line = input('> ')
      # if empty input we are done
      if (not len(line)):
        break
      p,q = [int(i) for i in line.split()]
      print(f'{p}--{q}')
      nums -= 1
  except ValueError as e:
    print(e)
  
  print('bye')