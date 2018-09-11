# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:33:58 2017

@author: ZHENGHAN ZHANG
"""

'''
This program solves an alphadoku problem
the board comes from a csv file
and computer solves it by using recursion
Author: Harry Zhenghan Zhang
'''
#in this program we suppose that rows and column starts from 0

import datetime

#this program reads the board from csv file and return a list
def get_board(csvfile):
    fp=open(csvfile,'r')
    list1=[]
    for line in fp:
        list1.append(line.strip().split(','))
    fp.close
    return list1

#get the non-repetitive existing characters in row
def in_row(board,row,column):
    a=[]
    b=board[row]
    for i in b:
        if b != '+':
            a.append(i)
    return a

#get the non-repetitive existing characters in column
def in_column(board,row,column):
    a=[]
    for i in board:
        if i[column] != '+':
            a.append(i[column])
    return a

#get the non-repetitive existing characters in a sector, given the coordinates
def in_sector(board,row,column):
    x = column // (len(board) ** 0.5)
    y = row // (len(board) ** 0.5)
    a = []
    for i in range(int(len(board) ** 0.5)):
        for j in range(int(len(board) ** 0.5)):
            if board[int((len(board) ** 0.5)*y + i)][int((len(board) ** 0.5)*x + j)] != '+':
                a.append(board[int((len(board) ** 0.5)*y + i)][int((len(board) ** 0.5)*x + j)])
    return a

#find one blank space
def get_blank(board):
    a = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '+':
                a.append(i)
                a.append(j)
    if a == []:
        return False
    else:
        return a

#visualization
def print_board(board):
    print('+-' * len(board) + '+')
    for i in range(len(board)):
        a=''
        for j in range(len(board[i])):
            if board[i][j] == '+':
                a += '| '
            else:
                a += '|' + board[i][j]
        a += '|'
        print(a)
        print('+-' * len(board) + '+')

#give the valid characters, determined by the length and width      
def valid_characters(board):
    a = []
    for i in range(len(board)):
        a.append(chr(97+i))
    return a

'''
In the recursion step, we need to find the possible values for a space
I intend to write a function, so that the "solve" function would not be as messy
'''
#the possible values = valid characters -(column+row+sector) [this is a way to put it :)]
def get_possible(board,row,column):
    a = ''
    x = in_column(board,row,column)
    y = in_row(board,row,column)
    z = in_sector(board,row,column)
    m = valid_characters(board)
    for i in x:
        if i not in y:
            y += i
    for j in z:
        if j not in y:
            y += j
    for k in y:
        if k not in z:
            z += k
    for l in m:
        if l not in z:
            a += l
    return a

#here is where the recursion happens
def solve(board):
    #test if there are blank spaces
    a = get_blank(board)
    #the base case
    if a == False:
        print_board(board)
        return True
    # the recursion step
    else:
        a = get_blank(board)
        x = get_possible(board,a[0],a[1])
        #breadcrumbs!!!
        previous = board[a[0]][a[1]]
        for i in x:
            board[a[0]][a[1]] = i
            if solve(board):
                return True
        board[a[0]][a[1]] = previous 
    return False



#execution                
board = get_board('9x9-98.csv')           
print_board(board)
print('-'*50)
#we also want a timer
x = datetime.datetime.now()        
solve(board)        
y = datetime.datetime.now()
print(y-x)