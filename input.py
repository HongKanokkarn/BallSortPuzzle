A = []
B = []
C = []
D = []
E = ['.', '.', '.', '.']
F = ['.', '.', '.', '.']
list = [A, B, C, D, E, F]

#takes the input file number from the user
def initialStack():
  val = int(input("Enter the input file number (1-4): "))  
  with open('input/input{}.in'.format(val)) as f:
      lines = f.readlines()
  balls=lines

  for i in range (4):
      A.append(balls[i][0])
  for i in range (4):
      B.append(balls[i][2])
  for i in range (4):
      C.append(balls[i][4])
  for i in range (4):
      D.append(balls[i][6])
  return list

