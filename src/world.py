from matrix import *

def assign_color(world, rows, cols, color):
  for i in rows:
    for j in cols:
      world[i][j] = color

def create_world():
  world = create_matrix()
  
  # Zones
  Sun = [([1,3], range(28, 31)), ([2], range(27, 32)),([4], [27,29,31])]
  Bedrock = [(range(14,21), range(1, 42))]
  Leaf_zones = [
    ([13], range(1, 26)), ([13], range(28, 41)), ([8], range(3,8)), ([8], range(9,14)), ([8], range(15,20)),([8],[25,29,39]), ([9], range(24,27)), ([9], range(28,31)), ([9], range(38,41)), ([7], range(4,7)), ([7], range(10,13)), ([7], range(16,19)), ([6],[5,11,17]),([6], range(19,26)),([6], range(34,41)), ([5], range(20,25)), ([5], range(35,40)), ([4], range(21,24)), ([4], range(36,39)), ([3], [22,37])
  ]
  water = [(range(13,18), range(26, 29))]
  wood = [(range(7,13), [22,37]),(range(9, 13),[5,11,17]),(range(10, 13),[25,29,39])]
  stone = [([12], range(7,10)), ([12], [12, 15,16, 20, 30, 35]), ([11], range(7,10)), ([10],[8]), ([14,18], [5]), [[16,19],[7]], ([19],[15,29]),([16], [10,34]),([15],[25]),(range(15,19),[23]),([16,18],[37]),([18],[40])]

  # Assigning colors to zones  
  for i,j in Sun:
    assign_color(world, i, j, yellow)
  for i,j in Bedrock:
    assign_color(world, i, j, black)
  for i,j in Leaf_zones:
    assign_color(world, i, j, green)
  for i,j in water:
    assign_color(world, i, j, blue)
  for i,j in wood:
    assign_color(world, i, j, red)
  for i,j in stone:
    assign_color(world, i, j, lightblack)

  return world
