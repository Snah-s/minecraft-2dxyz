from player import *

def print_world(world,mv):
  for rows in range(len(world)):
    for columns in range(len(world[rows])):
      if columns == 0:
        print(world[rows][columns].center(4), end='')
      if mv < columns < 31 + mv: 
        print(world[rows][columns].center(4), end='') 
      elif columns == 31 + mv:
        print()

def finalCommands(option):
  finalOutput = [] 
  temp = option.split(',')
  bypass = []
  for i in range(len(temp)):
    if temp[i].strip()[0].isdigit():
      bypass.append(temp[i].split())
    else:
      bypass.append(temp[i].strip())
  for i in bypass:
    if i[0].isdigit() and 1 < len(i):
      for _ in range(int(i[0])):
        finalOutput.append(i[1])
    else:
      finalOutput.append(i)
  return finalOutput

def game():
  world = create_matrix()
  mv = 0
  x = 2
  y = 11
  
  wood = 0
  stone = 0

  create_world(world)
  init_player(world, x, y)
  
  prompt = input()

  while prompt != 'init':
    prompt = input("$ ")

  print_world(world,mv)
  while prompt != 'exit':
    prompt = input("Ingrese un comando: ")
    if prompt == 'exit':
      break
    option = finalCommands(prompt)
    world, x, y, mv, wood, stone = actions(world, mv, option, x, y, wood, stone)
    print(x, y)
    print_world(world, mv)


game()