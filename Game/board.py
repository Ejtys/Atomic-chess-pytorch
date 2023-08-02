import torch
from typing import List

class AtomicChessBoard:
    def __init__(self):
        """Black is represented as negative number, white as possitive. 
        1 - pawn, - 2 - knigh, 3 - bishop, 5 - rook, 9 - queen, 10 - king"""
        self.board = [[-5, -2, -3, -9, -10, -3, -2, -5],
                      [-1, -1, -1, -1, -1,  -1, -1, -1],
                      [0,  0,  0,  0,  0,   0,  0,  0],
                      [0,  0,  0,  0,  0,   0,  0,  0],
                      [0,  0,  0,  0,  0,   0,  0,  0],
                      [0,  0,  0,  0,  0,   0,  0,  0],
                      [1,  1,  1,  1,  1,   1,  1,  1],
                      [5,  2,  3,  9,  10,  3,  2,  5]]
        self.move = 0
        self.toPlay = 1
        self.selectedSquere = [0,0]
        
    def SelectSquere(self, x: int, y: int):
        self.selectedSquere = [x, y]
        return self.board[x][y]
    
    def Move(self, x: int, y: int):
        """Return list of message and winner (None if there is no winner yet, 0 for draw)"""
        
        # Checking if player selected proper squere to play
        if (self.board[self.selectedSquere[0]][self.selectedSquere[1]]) * self.toPlay < 1:
            return ["Selected invalid square", self.toPlay * -1]
        
        #White pawn moves
        if self.board[self.selectedSquere[0]][self.selectedSquere[1]] == 1:
            
            #White pawn move on the same file
            if self.selectedSquere[1] == y:
                if self.board[x][y] != 0:
                    return ["White pawn tried to move to not empty squere", self.toPlay * -1]
                if self.board[x][y] == 0 and self.selectedSquere[0] - x == 1:
                    self.board[x][y] = 1
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.toPlay *= -1
                    return ["White pawn move by 1", None]
                if self.board[x][y] == 0 and self.selectedSquere[0] - x == 2 and self.selectedSquere[0] == 6:
                    self.board[x][y] = 1
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.toPlay *= -1
                    return ["White pawn move by 2", None]
    
    def Kill(self, x, y):
        pass
    
if __name__ == "__main__":
    atomic = AtomicChessBoard()
    print(atomic.SelectSquere(6, 1))
    print(atomic.Move(4,1))