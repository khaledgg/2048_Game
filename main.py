#2048 Game and solver

import random

def array_of_num(n, num):
    mat = [ [num]*n for _ in range(n)]
    return mat

def nice_print(mat):
    for row in mat:
        print(row)
    return

def rand_2(mat):
    #will randomly populate an empty spot with a 2, if none found

    #get zeroes
    z_mat = find_zero(mat)
    if(len(z_mat)==0):
        return
    #randomly select a zero
    rand_index = random.randint(0, len(z_mat))

    #replace with 2
    mat[z_mat[rand_index][0]][z_mat[rand_index][1]] = 2


def find_zero(mat):
    #find index of all zeroes
    z_ind = []
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 0:
                z_ind.append([row, col])
    return z_ind


def slide_up(mat):
    #move all integers up
        
    return

def slide_up_r(mat, row, col):
    #if at edge, stop
    if  (row == 0):
        return

    #if above is free, put it there
    elif ( mat[row-1][col] == 0 ):
        mat[row-1][col] = 
    
  

    #otherwise, check if can merge

    #if cant merge, STOP



arr = array_of_num(3, 0)
arr[1][1] = 1

nice_print(arr)
z_arr = find_zero(arr)
print()
print(z_arr)

print()
rand_2(arr)
nice_print(arr)

print()
slide_up(arr)
nice_print(arr)