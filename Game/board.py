

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
        self.moveHistory = [[[0,0],[0,0]]]
        
    def SelectSquere(self, x: int, y: int):
        self.selectedSquere = [x, y]
    
    def Move(self, x: int, y: int):
        """Return list of message and winner (None if there is no winner yet, 0 for draw)"""
        self.moveHistory.append([self.selectedSquere, [x, y]])
        
        # Checking if player selected proper squere to play
        if (self.board[self.selectedSquere[0]][self.selectedSquere[1]]) * self.toPlay < 1:
            return ["Selected invalid square", self.toPlay * -1]
        
        #White pawn moves
        if self.board[self.selectedSquere[0]][self.selectedSquere[1]] == 1 and self.toPlay == 1:
            
            #White pawn move on the same file
            if self.selectedSquere[1] == y:
                if self.board[x][y] != 0:
                    return ["White pawn tried to move to not empty squere", self.toPlay * -1]
                elif self.board[x][y] == 0 and self.selectedSquere[0] - x == 1:
                    self.board[x][y] = 1
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.toPlay *= -1
                    return ["White pawn move by 1", None]
                elif self.board[x][y] == 0 and self.selectedSquere[0] - x == 2 and self.selectedSquere[0] == 6:
                    self.board[x][y] = 1
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.toPlay *= -1
                    return ["White pawn move by 2", None]
                else:
                    return ["White pawn tried an illigale move on the same file", self.toPlay * -1]
                
            #White diagonal pawn moves
            elif self.selectedSquere[1] in (y + 1, y - 1) and self.selectedSquere[0] - x == 1:
                if self.board[x][y] < 0:
                    return self.Kill(x, y, "White pion")
                #En passant
                elif self.board[x][y] == 0 and x == 2 and self.moveHistory[-2][1][1] == y and self.moveHistory[-2][0][0] == 1 and self.moveHistory[-2][1][0] == 3 and self.board[self.moveHistory[-2][1][0]][self.moveHistory[-2][1][1]] == -1:
                    self.board[self.moveHistory[-2][1][0]][self.moveHistory[-2][1][1]] = 0
                    self.board[x][y] = -1
                    return self.Kill(x, y, "White pion en passant")
                elif self.board[x][y] == 0:
                    return ["White pawn tried diagonal move on empty squere", self.toPlay * -1]
                else: 
                    return ["White pawn tried to kill his own figure", self.toPlay * -1]
                    
            else:
                return ["White pawn tried invalid move", self.toPlay * -1]
                    
                    
                
        #Black pawn moves
        if self.board[self.selectedSquere[0]][self.selectedSquere[1]] == -1 and self.toPlay == -1:
        
            #Black pawn move on the same file
            if self.selectedSquere[1] == y and self.toPlay == -1:
                if self.board[x][y] != 0:
                    return ["Black pawn tried to move to not empty squere", self.toPlay * -1]
                elif self.board[x][y] == 0 and x - self.selectedSquere[0] == 1:
                    self.board[x][y] = -1
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.toPlay *= -1
                    return ["Black pawn move by 1", None]
                elif self.board[x][y] == 0 and x - self.selectedSquere[0] == 2 and self.selectedSquere[0] == 1:
                    self.board[x][y] = -1
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.toPlay *= -1
                    return ["Black pawn move by 2", None]
                else: 
                    return ["Black pawn tried an illigale move on the same file", self.toPlay * -1]
            
            #Black pion moves diagonally 
            elif self.selectedSquere[1] in (y + 1, y - 1) and x - self.selectedSquere[0] == 1:
                if self.board[x][y] < 0:
                    return self.Kill(x, y, "Black pion")
                #En passant
                elif self.board[x][y] == 0 and x == 5 and self.moveHistory[-2][1][1] == y and self.moveHistory[-2][0][0] == 6 and self.moveHistory[-2][1][0] == 4 and self.board[self.moveHistory[-2][1][0]][self.moveHistory[-2][1][1]] == 1:
                    self.board[self.moveHistory[-2][1][0]][self.moveHistory[-2][1][1]] = 0
                    self.board[x][y] = 1
                    return self.Kill(x, y, "Black pion en passant")
                elif self.board[x][y] == 0:
                    return ["Black pawn tried diagonal move on empty squere", self.toPlay * -1]
                else: 
                    return ["Black pawn tried to kill his own figure", self.toPlay * -1]

            else: 
                return ["Black pawn tried invalid move", self.toPlay * -1]
                
                
                
    
    def Kill(self, X, Y, pion):
        xs = [X - 1, X, X + 1]
        ys = [Y - 1, Y, Y + 1]
        for x in xs:
            for y in ys:
                try:
                    if (self.board[x][y] == 10 and self.toPlay == 1) or (self.board[x][y] == -10 and self.toPlay == -1):
                            return [pion + " tried to explode his own king", self.toPlay * -1]
                except:
                    pass                  
        
        kingisdead = False
        self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
        self.board[X][Y] = 0
        killcount = 1
        for x in xs:
            for y in ys:
                try:
                    if abs(self.board[x][y]) != 1:
                        if self.board[x][y] != 0:
                            killcount += 1
                        if abs(self.board[x][y]) == 10:
                            kingisdead = True
                        self.board[x][y] = 0
                except:
                    pass
        if kingisdead:
            return [pion + " killed opposite king", self.toPlay]
        self.toPlay *= -1                
        return [f"{pion} killed {killcount} opposite figure(s)", None]  
    
if __name__ == "__main__":
    atomic = AtomicChessBoard()
    print(atomic.SelectSquere(6, 1))
    print(atomic.Move(4,1))