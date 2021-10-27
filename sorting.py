from input import initialStack
import copy
import utils


# moving the balls from stack i[s1] to j[s2]
def moving(stack, i, j, s1, s2, cost):
    new_stack = copy.deepcopy(stack)
    if s2 == 3 and new_stack[j][s2] == '.':
        new_stack[j][s2] = new_stack[i][s1]
    else:
        new_stack[j][s2 - 1] = new_stack[i][s1]
    new_stack[i][s1] = '.'
    return (new_stack, cost)


#find the the deepest empty space in the stack
def check_space(stack, i, j):
    count_i = 0  #counts the number of . in a stack
    for k in range(3):
        if stack[i][k] == '.':
            count_i += 1

    count_j = 0
    for k in range(3):
        if stack[j][k] == '.':
            count_j += 1

    return count_i, count_j


def successors(stack, cost):
    for i in range(6):
        for j in range(6):
            #from-stack (i) != to-stack (j) and from-stack isn't empty
            if i != j and not utils.hasNothing(stack[i]):
                if not utils.hasNothing(stack[j]):  # if to-stack is not empty
                    if utils.isnotX(stack[j][0]):  #if to-stack is full
                        continue
                    s3, s4 = check_space(stack, i, j)
                    if stack[i][s3] != stack[j][
                            s4]:  #if top ball in i != top ball in j
                        continue
                s1, s2 = check_space(stack, i, j)
                yield moving(stack, i, j, s1, s2, cost)  #move i[s1] to j[s2]


def is_goal(stack):
    checker = 0
    for i in range(6):
        for j in range(4):
            #if first element == every other element for 4 stacks
            if (stack[i][0] == stack[i][j] and utils.isnotX(stack[i][0])):
                checker += 1 / 4
    if checker == 4:
        return True
    else:
        return False
