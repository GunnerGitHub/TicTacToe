

import time

#theBoard information (initially 0)
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def printBoard(board):
    """Tic Tac Toe board (grid of 3x3)"""
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])

def game():
    print("Welcome to Tik-Tac-Toe, the following grid explains the inputs:")
    print('7'+'|'+'8'+'|'+'9')
    print('-+-+-')
    print('4'+'|'+'5'+'|'+'6')
    print('-+-+-')
    print('1'+'|'+'2'+'|'+'3')

    time.sleep(2)    
    print('Are you ready? May the best player win!')
    
    turn = 'X' #turn
    count = 0 #count number of moves of both players
    for i in range(1000):
        printBoard(theBoard)
        print("It's your turn, "+ turn+ ". Move to which place?")
        move = input()

        #check if valid
        if int(move)<1 or int(move)>9:
            print("Invalid move, try again.")
            continue

        #gameplay
        if theBoard[move] == " ":
            theBoard[move] = turn
            count+=1
        else:
            print("That place is already filled.\nChoose another place.")
            continue

        #check the win conditions
        if count>=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': #across
                printBoard(theBoard)
                print("\nGame Over!.\n")
                print(" *** "+ turn + " won. ***")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': #across
                printBoard(theBoard)
                print("\nGame Over!.\n")
                print(" *** "+ turn + " won. ***")
                break          
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': #across
                printBoard(theBoard)
                print("\nGame Over!.\n")
                print(" *** "+ turn + " won. ***")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': #down
                printBoard(theBoard)
                print("\nGame Over!.\n")
                print(" *** "+ turn + " won. ***")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': #down
                printBoard(theBoard)
                print("\nGame Over!.\n")
                print(" *** "+ turn + " won. ***")
                break          
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': #down
                printBoard(theBoard)
                print("\nGame Over!.\n")
                print(" *** "+ turn + " won. ***")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': #diagnal
                printBoard(theBoard)
                print("\nGame Over!.\n")
                print(" *** "+ turn + " won. ***")
                break          
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': #diagnal
                printBoard(theBoard)
                print("\nGame Over!.\n")
                print(" *** "+ turn + " won. ***")
                break

        #if neither of them win
        if count == 9:
            print("\nGame Over!.\n")
            print("It's a TIE!")
            break

        #change the player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

#call the function to execute
game()
