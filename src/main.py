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


    if key == 'KEY_UP' and game.upCheck:
      shell.erase()
      game.up()
      if doNumberSpawning:
        game.spawn_number()
      game.display_grid()
      shell.refresh()
      game.refresh_var()

    elif key == 'KEY_DOWN' and game.downCheck:
      shell.erase()
      game.down()
      if doNumberSpawning:
        game.spawn_number()
      game.display_grid()
      shell.refresh()
      game.refresh_var()

    elif key == 'KEY_LEFT' and game.leftCheck:
      shell.erase()
      game.left()
      if doNumberSpawning:
        game.spawn_number()
      game.display_grid()
      shell.refresh()
      game.refresh_var()
  
    elif key == 'KEY_RIGHT' and game.rightCheck:
      shell.erase()
      game.right()
      if doNumberSpawning:
        game.spawn_number()
      game.display_grid()
      shell.refresh()
      game.refresh_var()

    elif key == 'x':
      game.end_game()

except breakLoop:
  game.end_game()