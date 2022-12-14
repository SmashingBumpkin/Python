#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Othello, or Reversi (https://en.wikipedia.org/wiki/Reversi), is a board game
played by two players, playing "disks" of different colors an 8x8 board.
Despite having relatively simple rules, Othello is a game of high strategic depth.
In this homework you will need to simulate a simplified version of othello,
called Dumbothello, in which each player can capture the opponent's disks
by playing a new disk on an adjacent empty cell.
The rules of Dumbothello are:
- each player has an associated color: white, black;
- the player with black is always the first to play;
- in turn, each player must place a disk of their color in such a way
  to capture one or more opponent's disks;
- capturing one or more opponent's disks means that the disk played by the
  player changes into the player's color all the directly adjacent opponent's disks,
  in any horizontal, vertical or diagonal direction;
- after playing one's own disk, the captured opponent's disks change
  their color, and become the same color as the player who just played;
- if the player who has the turn cannot add any disk on the board,
  the game ends. The player who has the higher number of disks on the board wins
  or a tie occurs if the number of disks of the two players is equal;
- the player who has the turn cannot add any disk if there is
  no way to capture any opponent's disks with any move, or if there are no
  more free cells on the board.

Write a function dumbothello(filename) that reads the configuration of the
board from the text file indicated by the string "filename" and,
following the rules of Dumbothello, recursively generates the complete game tree
of the possible evolutions of the game, such that each leaf of the tree
is a configuration from which no more moves can be made.

The initial configuration of the chessboard in the file is stored line by
line in the file: letter "B" identifies a black disk, a "W" a white disk,
and the character "." an empty cell. The letters are separated by one or
more spacing characters.

The dumbothello function will return a triple (a, b, c), where:
- a is the total number of evolutions ending in a black victory;
- b is the total number of evolutions ending in a white victory;
- c is the total number of evolutions ending in a tie.

For example, given as input a text file containing the board:
. . W W
. . B B
W W B B
W B B W

The function will return the triple:
(2, 16, 0)

NOTICE: the dumbotello function or some other function used by it must be recursive.

'''

#def dumbothello(filename : str) -> tuple[int,int,int] :
def dumbothello(filename):
    
    with open(filename, 'r', encoding="utf8") as fileref:
        board = [line.split() for line in fileref.readlines()]
    result = move_checker(board, True)
    return result

def move_checker(board: list, blkTurn: bool):
    #find all potential positions
    boardH = len(board)
    boardW = len(board[0])
    options = [[y,x] for y, line in enumerate(board) for x, posn in enumerate(line) if posn == '.']
    if not options:
        return board_winner(board)

    if blkTurn:
        target = 'W'
        newcol = 'B'
    else:
        target = 'B'
        newcol = 'W'
    blkW = 0
    whtW = 0
    tie = 0
    #loop through each option
    for y, x in options:
        
        success = False
        tempboard = [line.copy() for line in board]
        tempboard[y][x] = newcol
        
    #check if move is legal, if not skip
        #check all surrounding squares for target colour
            #change colour to newcol
            #success = True
        xrangeMin = max(x - 1,0)
        xrangeMax = min(boardW, x + 2)
        yrangeMin = max(y - 1,0)
        yrangeMax = min(boardH, y + 2)
        
        for xcheck in range(xrangeMin, xrangeMax):
            for ycheck in range(yrangeMin, yrangeMax):
                if tempboard[ycheck][xcheck] == target:
                    success = True
                    tempboard[ycheck][xcheck] = newcol
        #if success, use recursion
        #else add result of board_winner to results
        if success:
            result = move_checker(tempboard, not blkTurn)
        else:
            result = board_winner(tempboard)
        blkW, whtW, tie = blkW + result[0], whtW + result[1], tie + result[2]
            
    #
    return blkW, whtW, tie


def board_winner(board: list):
    blacks = [1 for line in board for posn in line if posn == 'B']
    whites = [1 for line in board for posn in line if posn == 'W']
    if len(blacks) > len(whites):
        return [1,0,0]
    elif len(whites) > len(blacks):
        return [0,1,0]
    else:
        return [0,0,1]
    
    
if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
