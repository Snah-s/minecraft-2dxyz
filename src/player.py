from world import *

def init_player(world, x, y):
  world[y-1][x] = cyan
  world[y][x] = cyan
  world[y+1][x] = cyan
  world[y][x+1] = magenta


def actions(world, mv, option, x,y, it, wood, stone):
  x = max(0, min(x, 40))
  y = max(0, min(y, 20))
  
  tempW = world
  
  if it < 1:
    world[y-1][x] = void
    world[y][x] = void
    world[y+1][x] = void
    world[y][x+1] = void
  else:
    world[y-1][x] = tempW[y-1][x]
    world[y][x] = tempW[y][x]
    world[y+1][x] = tempW[y+1][x]
    world[y][x+1] = tempW[y][x+1]
    
  for i in option:
    if str(i).lower() == 'left':
      x = x - 1
    elif str(i).lower() == 'right':
      x = x + 1
    elif str(i).lower() == 'up':
      y = y - 1
    elif str(i).lower() == 'down':
      y = y + 1

  world[y][x] = cyan
  world[y-1][x] = cyan
  world[y+1][x] = cyan
  world[y][x+1] = magenta
  for i in range(x):
    if 19 < i < 30:
      mv = mv + 1
  
  for i in option:
    if str(i).lower() == 'destroy':
      world[y][x+1] = void
      auth = 'd'
    elif str(i).lower() == 'extract':
      world[y][x+1] = void
      if world[y][x] == red:
        wood = wood + 1
      elif world[y][x] == lightblack:
        stone = stone + 1
      auth = 'd'
    elif str(i).lower() == 'build wood':
      if wood > 0:
        world[y][x+1] = red
        wood = wood - 1
    elif str(i).lower() == 'build stone':
      if stone > 0:
        world[y][x+1] = lightblack
        stone = stone - 1
  
  print('Wood: \t', wood)
  print('Stone: \t', stone)
  
  it = it + 1
  
  return world, mv, option, x,y, it, wood, stone