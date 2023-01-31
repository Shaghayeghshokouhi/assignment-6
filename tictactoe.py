# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 00:05:37 2023

@author: 2022
"""

import pyfiglet



def display_board():
    for row in board:
        for cell in row:
            print(cell,"",end=" ")
        print()
        
title = pyfiglet.figlet_format("tic tac toe", font = "slant")
print(title)


def play_game():
    if board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x" :
        print("player1 wins!")
        
    if board[0][0] == "o" and board[0][1] == "o" and board[0][2] == "o" :
       print("player2 wins!")
         
    if board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x" :
        print("player1 wins!")
        
    if board[1][0] == "o" and board[1][1] == "o" and board[1][2] == "o" :
        print("player2 wins!")
        
    if board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x" :
        print("player1 wins!")
        
    if board[2][0] == "o" and board[2][1] == "o" and board[2][2] == "o" :
        print("player2 wins!")
        
    if board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x" :
        print("player1 wins!")
        
    if board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o" :
        print("player2 wins!")
        
    if board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x" :
        print("player1 wins!")
    
    if board[0][1] == "o" and board[1][1] == "o" and board[2][1] == "0" :
        print("player2 wins!")
        
    if board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x" :
        print("player1 wins!")
        
    if board[0][2] == "o" and board[1][2] == "o" and board[2][2] == "o" :
        print("player2 wins!")
        
    if board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x" :
        print("player1 wins!")
        
    if board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o" :
        print("player2 wins!")
        
    if board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x" :
        print("player1 wins!")
        
    if board[0][2] == "o" and board[1][2] == "o" and board[2][0] == "o" :
        print("player2 wins!")
        
    if board[0][0] != "-" and board[0][1] != "-" and board[0][2] != "-" and board[1][0] != "-" and board[1][1] != "-" and board[1][2] != "-"  and  board[2][0] != "-" and board[2][1] != "-" and board[2][2] != "-" :
        print("it's a draw!")
 
        
board = [["-", "-", "-"]
          ["-", "-", "-"]
          ["-", "-", "-"]]


display_board()

while True:
    print("player1 you're up!")
    while True:
        r = int(input("row : "))
        c = int(input("column: "))
        if 0 <= r <=2 and 0 <= c <=2 :
            if board[r][c] == "-":
                board[r][c] = "x"
                display_board()
                play_game()
                break
        else:
            print("choose anothe cell:")
    
    while True:
        print("player2 you're up!")
        while True:
            r = int(input("row : "))
            c = int(input("column: "))
            if 0 <= r <=2 and 0 <= c <=2 :
             if board[r][c] == "-":
                 board[r][c] = "x"
                 display_board()
                 play_game()
                 break
    else:
        print("choose another cell:")
        
display_board()
                

                
                
                
     
        
        
        
        
        