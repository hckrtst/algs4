#!/bin/python3
import sys

class QuickFindUF:
  def __init__(n):
    self.id = [i for i in range(n)]
  
  # time complexity O(N^2)
  def union(p, q):
    pid = self.id[p]
    qid = self.id[q]
    for i in range(len(id)):
      if 

  def connected(p, q)
    return self.id[p] == self.id[q]

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