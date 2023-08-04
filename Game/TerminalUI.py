import os
from board import AtomicChessBoard


def Displayboard(board: AtomicChessBoard):
    os.system("clear")
    for row_num, row in enumerate(board.board):
        print(8 - row_num, end = " | ")
        for squere in row:
            match squere:
                case -1:
                    x = "p"
                case -2:
                    x = "n"
                case -3:
                    x = "b"
                case -5:
                    x = "r"
                case -9:
                    x = "q"
                case -10:
                    x = "k"
                case 1:
                    x = "P"
                case 2:
                    x = "N"
                case 3:
                    x = "B"
                case 5:
                    x = "R"
                case 9:
                    x = "Q"
                case 10:
                    x = "K"
                case 0:
                    x = " "
                    
                 
            print(x, end=" | ")
        print(" ")
        print(35 * "-")
    for x in [" ", "A", "B", "C", "D", "E", "F", "G", "H"]:
        print(x, end = " | ")
    print("")
    
def MakeMove(board: AtomicChessBoard):
    if board.toPlay == 1:
        print("White to play.")
    else: print("Black to play.")
    move = input("Enter your move: ")
    def translate(s: str):
        x = 8 - int(s[0])
        for y, letter in enumerate(["A", "B", "C", "D", "E", "F", "G", "H"]):
            if s[1].upper() == letter:
                break
        return x, y
    board.SelectSquere(*translate(move[:-2]))
    m = board.Move(*translate(move[2:]))
    return m[0], m[1], move.upper()
        
def GameLoop():
    atomic = AtomicChessBoard()
    Displayboard(atomic)
    while True:
        message = MakeMove(atomic)
        Displayboard(atomic)
        print(message[2] + ": " + message[0])
        print(atomic.moveHistory[-1])
        print(atomic.moveHistory[-2])
        if message[1] != None:
            break
    if message[1] == 0:
        print("It is a draw.")
    elif message[1] == 1:
        print("White won.")
    else:
        print("Black won.")
            
            
if __name__ == "__main__":
    GameLoop()

        