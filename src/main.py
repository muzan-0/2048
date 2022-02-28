from game import *
import time

game = Game()

curses.cbreak()
curses.noecho()
shell.keypad(True)

game.spawn_number()
game.display_grid()
shell.refresh()


while True:
  key = shell.getkey()

  if key == 'KEY_UP':
    shell.erase()
    game.up()
    game.spawn_number()
    game.display_grid()
    shell.refresh()

  elif key == 'KEY_DOWN':
    shell.erase()
    game.down()
    game.spawn_number()
    game.display_grid()
    shell.refresh()

  elif key == 'KEY_LEFT':
    shell.erase()
    game.left()
    game.spawn_number()
    game.display_grid()
    shell.refresh()
  
  elif key == 'KEY_RIGHT':
    shell.erase()
    game.right()
    game.spawn_number()
    game.display_grid()
    shell.refresh()