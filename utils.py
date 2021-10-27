from collections import deque


def create_node(state,parent,path_cost):
    return (state,parent,path_cost)

def print_solution(n):
    r = deque()
    while n is not None:
        r.appendleft(n[0])
        n = n[1]
    for i in range (len(r)):
      print("Step {}".format(i))
      print(r[i][0][0],r[i][1][0],r[i][2][0],r[i][3][0],r[i][4][0],r[i][5][0])
      print(r[i][0][1],r[i][1][1],r[i][2][1],r[i][3][1],r[i][4][1],r[i][5][1])
      print(r[i][0][2],r[i][1][2],r[i][2][2],r[i][3][2],r[i][4][2],r[i][5][2])
      print(r[i][0][3],r[i][1][3],r[i][2][3],r[i][3][3],r[i][4][3],r[i][5][3])
      print()
    
#checks if the pointer is currently pointing at X
def isnotX(x):
    if x != '.':
        return True
    else:
        return False

#checks if the stack has space
def is_empty(stack):
    for i in range(4):
        if stack[i] == '.':
            return True
    return False

#checks if the stack is empty
def hasNothing(stack):
    checker = 0
    for i in range(4):
        if stack[i]=='.':
            checker+=1
    if checker == 4:
        return True
    else:
        False
