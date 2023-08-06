import copy

class AtomicChessBoard:
    def __init__(self):
        """Black is represented as negative number, white as possitive. 
        1 - pawn, - 2 - knigh, 3 - bishop, 5 - rook, 9 - queen, 10 - king"""
        self.board = [[-5, -2, -3, -9, -10, -3, -2, -5],
                      [-1, -1, -1, -1, -1,  -3, -1, -1],
                      [0,  0,  0,  0,  0,   0,  0,  0],
                      [0,  0,  0,  0,  0,   0,  0,  0],
                      [0,  0,  0,  0,  0,   0,  0,  0],
                      [0,  0,  0,  0,  0,   0,  0,  0],
                      [1,  1,  3,  1,  1,   1,  1,  1],
                      [5,  2,  3,  9,  10,  3,  2,  5]]
        self.move = 0
        self.toPlay = 1
        self.selectedSquere = [0,0]
        self.moveHistory = [[[0,0],[0,0]]]
        self.boardHistory = []
        self.player = "White"
        self.lastPawnnMove = 0
        
    def SelectSquere(self, x: int, y: int):
        self.selectedSquere = [x, y]
    
    def Move(self, x: int, y: int):
        """Return list of message and winner (None if there is no winner yet, 0 for draw)"""
        self.moveHistory.append([self.selectedSquere, [x, y]])
        self.player = "White" if self.toPlay == 1 else "Black"
        self.move += 1
        self.boardHistory.append(copy.deepcopy(self.board))
        
        if self.isThreeFoldRepetition():
            return ["Draw by threefold repetition", 0]
        
        if self.move - self.lastPawnnMove >= 100:
            return ["Draw by 50 move rule", 0]
        
        
        # Checking if player selected proper squere to play
        if (self.board[self.selectedSquere[0]][self.selectedSquere[1]]) * self.toPlay < 1:
            return ["Selected invalid square", self.toPlay * -1]
        
        #White pawn moves
        if self.board[self.selectedSquere[0]][self.selectedSquere[1]] == 1 and self.toPlay == 1:
            self.lastPawnnMove = self.move
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
            self.lastPawnnMove = self.move
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
              
        #Knigh moves  
        if abs(self.board[self.selectedSquere[0]][self.selectedSquere[1]]) == 2:
            #checking if move is valide
            delta_x = abs(self.selectedSquere[0] - x)
            delta_y = abs(self.selectedSquere[1] - y)
            
            IsValidKnightMove = (delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1)
            
            if IsValidKnightMove:
                if self.board[x][y] == 0:
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.board[x][y] = 2 * self.toPlay
                    self.toPlay *= -1
                    return [f"{self.player} Knight moves to empty square", None]
                elif self.have_same_sign(self.board[x][y], self.toPlay):
                    return [f"{self.player} Knight tried to kill his own figure", self.toPlay * -1]
                else:
                    return self.Kill(x, y, f"{self.player} Knight")
            else: 
                return [f"{self.player} Knight tried invalid move", self.toPlay * -1]
              
        #Bishop moves  
        if abs(self.board[self.selectedSquere[0]][self.selectedSquere[1]]) == 3:
            return self.makeLongMove(x, y, self.isDiagonal, "Bishop", 3, "Diagonal")
        
        #Rook moves
        if abs(self.board[self.selectedSquere[0]][self.selectedSquere[1]]) == 5:
            return self.makeLongMove(x, y, self.isOrthogonal, "Rook", 5, "Orthogonal")
        
        #Qeen moves
        if abs(self.board[self.selectedSquere[0]][self.selectedSquere[1]]) == 9:
            if self.isDiagonal(x, y):
                return self.makeLongMove(x, y, self.isDiagonal, "Queen", 9, "Diagonal")
            elif self.isOrthogonal(x, y):
                return self.makeLongMove(x, y, self.isOrthogonal, "Queen", 9, "Orthogonal")
            else:
                return [f"{self.player} Queen tried invalid move", self.toPlay * -1]

        #King moves
        if abs(self.board[self.selectedSquere[0]][self.selectedSquere[1]]) == 10:
            if (self.isDiagonal(x, y) or self.isOrthogonal(x, y)) and self.isOneSquareAway(x, y):
                if self.board[x][y] == 0:
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.board[x][y] = 10 * self.toPlay
                    self.toPlay *= -1
                    return [f"{self.player} King moves to empyty square", None]
                else:
                    return [f"{self.player} King tries to not empty square", self.toPlay * -1]
            else:
                return [f"{self.player} King tries invalid move", self.toPlay * -1]
            
    def isOneSquareAway(self, x, y):
        x1, y1 = self.selectedSquere
        return (abs(x - x1) == 1 and (abs(y - y1) == 1 or abs(y - y1) == 0)) or (abs(x - x1) == 0 and (abs(y - y1) == 1 or abs(y - y1) == 0)) 
                
    def isThreeFoldRepetition(self):
        same_cound = 0
        for board in self.boardHistory:
            if self.areBoardsTheSame(board, self.board):
                same_cound += 1
        return same_cound >= 3
    
    def areBoardsTheSame(self, board1, board2):
        for x in range(len(board1)):
            for y in range(len(board1[0])):
                if board1[x][y] != board2[x][y]:
                    return False
        return True

    def makeLongMove(self, x, y, func, figure, figureNum, kindOfMove):
        if func(x, y):
            if self.isBetweenSpaceEmpty(x, y):
                if self.board[x][y] == 0:
                    self.board[self.selectedSquere[0]][self.selectedSquere[1]] = 0
                    self.board[x][y] = figureNum * self.toPlay
                    self.toPlay *= -1
                    return [f"{self.player} {figure} moves {kindOfMove}ly to empty square", None]
                elif self.have_same_sign(self.board[x][y], self.toPlay):
                    return [f"{self.player} {figure} tried to kill his own figure {kindOfMove}ly", self.toPlay * -1]
                else:
                    return self.Kill(x, y, f"{self.player} {figure} {kindOfMove}ly")
            else:
                return [f"{self.player} {figure} tried move {kindOfMove}ly over other figures", self.toPlay * -1]
        else:
            return [f"{self.player} {figure} tried invalid move", self.toPlay * -1]
                
    def isOrthogonal(self, x, y):
        return self.selectedSquere[0] == x or self.selectedSquere[1] == y                                
                
    def isDiagonal(self, x2, y2):
        x1 = self.selectedSquere[0]
        y1 = self.selectedSquere[1]
        return x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2
                    
    def isBetweenSpaceEmpty(self, x, y):
        start = self.selectedSquere
        end = (x, y)
        direction = self.checkDirection(start, end)
        step = (start[0] + direction[0], start[1] + direction[1])
        while step != end:
            if self.board[step[0]][step[1]] !=0:
                return False
            step = (step[0] + direction[0], step[1] + direction[1])
        return True
        
    def checkDirection(self, start, end):
        if start[0] < end[0]:
            topbottom = 1
        elif start[0] == end[0]:
            topbottom = 0
        else:
           topbottom = -1
        if start[1] < end[1]:
            sides = 1
        elif start[1] == end[1]:
            sides = 0
        else:
            sides = -1
        return (topbottom, sides)
    
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
    
    def have_same_sign(self, a, b):
        return (a >= 0 and b >= 0) or (a < 0 and b < 0)
    
