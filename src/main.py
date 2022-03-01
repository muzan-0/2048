from sys import exit
from actor import *
import time

game = Game()

doNumberSpawning = True

curses.cbreak()
curses.noecho()
shell.keypad(True)

if doNumberSpawning:
  game.spawn_number()
game.display_grid()
game.refresh_var()
shell.refresh()

try:
  while True:
    key = shell.getkey()

    if game.upCheck or game.downCheck or game.leftCheck or game.rightCheck:
      if key == 'KEY_UP':
        shell.erase()
        game.up()
        if doNumberSpawning:
          game.spawn_number()
        game.display_grid()
        shell.refresh()
        game.refresh_var()

      elif key == 'KEY_DOWN':
        shell.erase()
        game.down()
        if doNumberSpawning:
          game.spawn_number()
        game.display_grid()
        shell.refresh()
        game.refresh_var()

      elif key == 'KEY_LEFT':
        shell.erase()
        game.left()
        if doNumberSpawning:
          game.spawn_number()
        game.display_grid()
        shell.refresh()
        game.refresh_var()
  
      elif key == 'KEY_RIGHT':
        shell.erase()
        game.right()
        if doNumberSpawning:
          game.spawn_number()
        game.display_grid()
        shell.refresh()
        game.refresh_var()

      elif key == 'x':
        game.end_game()

    else:
      raise breakLoop

except breakLoop:
  game.end_game()