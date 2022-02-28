import curses
import pprint
import time
import random
from constants import *

shell = curses.initscr()



class breakLoop(Exception):
  pass

class gameOver(Exception):
  pass

class Game:
  def __init__(self):
    self.grid = GRID
    self.upCheck = self.checkUp()
    
  def __getitem__(self, coords):
    return self.grid[coords[1]][coords[0]]

  def center_number(self, number):
    if number == '0':
      return '    '
    elif len(number) == 1:
      return ' ' + number + '  '
    elif len(number) == 2:
      return ' ' + number + ' '
    elif len(number) == 3:
      return number + ' '
    elif len(number) == 4:
      return number

  def display_grid(self):
    shell.addstr('-' * 21 + '\n')
    for line in self.grid:
      shell.addstr('|')
      for cell in line:
        shell.addstr(self.center_number(str(cell)) + '|')
      shell.addstr('\n' + ('-'*21) + '\n')


  def up(self):
    for i in range(3):
      for line in range(1,4):
        


          
        for cell in range(len(self.grid[line])):
          
          if self[(cell, line - 1)] == 0:
            self[(cell, line - 1)], self[(cell, line)] = self[(cell, line)], self[(cell, line - 1)]
            self[(cell, line)] = 0
          if self[(cell, line - 1)] == self[(cell, line)]:
            self[(cell, line - 1)], self[(cell, line)] = self[(cell, line)] * 2, 0
            self[(cell, line)] = 0

  def down(self):
    for i in range(3):
      for line in range(2, -1, -1):

        for cell in range(len(self.grid[line])):
          
          if self[(cell, line + 1)] == 0:
            self[(cell, line + 1)], self[(cell, line)] = self[(cell, line)], self[(cell, line + 1)]
            self[(cell, line)] = 0

          elif self[(cell, line + 1)] == self[(cell, line)]:
            self[(cell, line + 1)], self[(cell, line)] = self[(cell, line)] * 2, 0
            self[(cell, line)] = 0

  def left(self):
    for i in range(3):
      for line in range(len(self.grid)):

        for cell in range(1,4):
          
          if self[(cell - 1, line)] == 0:
            self[(cell - 1, line)], self[(cell, line)] = self[(cell, line)], self[(cell - 1, line)]
            self[(cell, line)] = 0

          if self[(cell - 1, line)] == self[(cell, line)]:
            self[(cell - 1, line)], self[(cell, line)] = self[(cell, line)] * 2, 0
            self[(cell, line)] = 0

  def right(self):
    for i in range(3):
      for line in range(4):

        for cell in range(2, -1, -1):
          
          if self[(cell + 1, line)] == 0:
            self[(cell + 1, line)], self[(cell, line)] = self[(cell, line)], self[(cell + 1, line)]
            self[(cell, line)] = 0

          if self[(cell + 1, line)] == self[(cell, line)]:
            self[(cell + 1, line)], self[(cell, line)] = self[(cell, line)] * 2, 0
            self[(cell, line)] = 0

  def spawn_number(self):
    numOfZeros = 0
    for line in self.grid:
      for cell in line:
        if cell == 0:
          numOfZeros += 1

    if numOfZeros <= 0:
      return

    try:
      while True:
        for line in range(len(self.grid)):
          for cell in range(len(self.grid[line])):
            if self[(cell, line)] == 0 and random.randint(0, numOfZeros) == 0:
              self[(cell, line)] = 4 if random.randint(1, 10) == 10 else 2
              raise breakLoop
    except breakLoop:
      pass

  def checkUp(self):
    try:
      for line in range(len(self.grid)): # Loops through every line in the grid
        for cell in range(len(self.grid)): # Loops through every cell in the line
          if self[(cell, line)] == self.grid[line + 1][cell]: # Checks if the cell is equal to to one below it
            raise breakLoop # If it is, raise an expeption that breaks out of the loop

      shell.addstr('lmao you cant do that')
      return False

    except breakLoop:
      return True

      
      return False

    except breakLoop:
      return True
        