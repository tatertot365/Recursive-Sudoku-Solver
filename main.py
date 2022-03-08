import numpy as np

puzzle = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def possible(y,x,n):
  global puzzle
  for i in range(9):
    if puzzle[y][i] == n:
      return False


  for i in range(9):
    if puzzle[i][x] == n:
      return False

  x1 = (x//3)*3
  y1 = (y//3)*3
  for i in range(3):
    for j in range(3):
      if puzzle[y1+i][x1+j] == n:
         return False

  return True

def solve():
  global puzzle
  for y in range(9):
    for x in range(9):
      if puzzle[y][x] == 0:
        for n in range(1,10):
          if possible(y,x,n):
            puzzle[y][x] = n
            solve()

            puzzle[y][x] = 0
        return
  print(np.matrix(puzzle))

solve()


