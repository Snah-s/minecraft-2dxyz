from world import *

def init_player(world, x, y):
  world[y-1][x] = cyan
  world[y][x] = cyan
  world[y+1][x] = cyan
  world[y][x+1] = magenta


def actions(world, mv, option, x, y, wood, stone):
  tempX = x
  tempY = y
  
  tempW = create_matrix()
  create_world(tempW)
  
  x = max(0, min(x, 40))
  y = max(0, min(y, 20))
  
  for i in option:
    if str(i).lower() == 'left':
      x = x - 1
    elif str(i).lower() == 'right':
      x = x + 1
    elif str(i).lower() == 'up':
      y = y - 1
    elif str(i).lower() == 'down':
      y = y + 1
  
  world[tempY-1][tempX] = tempW[tempY-1][tempX]
  world[tempY][tempX] = tempW[tempY][tempX]
  world[tempY+1][tempX] = tempW[tempY+1][tempX]
  world[tempY][tempX+1] = tempW[tempY][tempX+1] 
  
  world[y][x] = cyan
  world[y-1][x] = cyan
  world[y+1][x] = cyan
  world[y][x+1] = magenta
  for i in range(x):
    if 19 < i < 30:
      mv = mv + 1
  
  return world, x, y, mv, wood, stone