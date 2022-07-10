def won():
  for row in [2,1,0]:
    if(grid[row*3] == grid[row*3+1] == grid[row*3+2]):
      return True
  for col in [2,1,0]:
    if(grid[col] == grid[col+3] == grid[col+6]):
      return True
  for diag in [0,2]:
    if(grid[diag] == grid[4] == grid[8-diag]):
      return True
  if is_draw():
    return True
  return False
def is_draw():
  for i in grid:
    if not i in ["X","O"]:
      return False
  return True
def print_grid():
  print()
  for row in [2,1,0]:
    print(str(grid[row*3])+" | "+str(grid[row*3+1])+" | "+str(grid[row*3+2]))
def taken(cell):
  return grid[cell-1] in ["X","O"]
def go():
  print_grid()
  if turn() in ai:
    square = ai_a()
  else:
    square = input(turn()+"'s turn: ")
  try:
    if grid[int(square)-1] not in ["X","O"]:
      grid[int(square)-1] = turn()
      return True
  except:
    return False
def turn():
  if is_x:  return "X"
  else:  return "O"
def oturn():
  if is_x:  return "O"
  else:  return "X"
def has2(cells):
  for player in [[turn(),oturn()],[oturn(),turn()]]:  
    has=0
    hasnot=0
    for cell in cells:
      if grid[cell]==player[0]:
        has+=1
      elif not grid[cell]==player[1]:
        hasnot=grid[cell]
    if has==(len(cells)-1) and hasnot>0:
      return hasnot
  return False
def ai_a():
  for row in [2,1,0]:
    tmp = has2([row*3,row*3+1,row*3+2])
    if tmp:
      return tmp
  for col in [2,1,0]:
    tmp = has2([col,col+3,col+6])
    if tmp:
      return tmp
  for diag in [0,2]:
    tmp = has2([diag,4,8-diag])
    if tmp:
      return tmp  
  for cor in [[1,3,1],[1,5,3],[7,3,7],[7,5,9]]:
    if grid[cor[0]] == grid[cor[1]] and not taken(cor[2]):
      return cor[2]
  if not taken(5):
    return 5  
  if grid[4] is oturn():
    for i in range(1,5):
      if not taken(2*i-1):
        return 2*i-1
  for i in range(1,5):
    if not taken(2*i):
      return 2*i
  for i in range(1,9):
      if not taken(i-1):
        return i-1
ai = []
tmp = input("players (1,2)")
if tmp == "1":
  ai = ["O"]
while tmp not in ["1","2"]:
  tmp = input("players (1,2)")
  if tmp == "1":
    ai = ["O"]
#  else:
#    ai = []
points=[0,0]
while input("Ready?") not in ["n","N","NO","No","no","0"]:
  grid = [1,2,3,4,5,6,7,8,9]
  is_x = True
  while not won():
    if go():
      is_x = not is_x
  print_grid()
  if is_draw():
    print("It's a draw")
  else:
    print(oturn() + " has won")
    points[(is_x and ai == ["X"])-1]+=1
  print("POINTS")
  for i in [1,2]:
    print("Player "+str(i)+": "+str(points[i-1]))
  if ai == ["O"]:
    ai = ["X"]
  elif ai == ["X"]:
    ai = ["O"]