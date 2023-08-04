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
            
if __name__ == "__main__":
    atomic = AtomicChessBoard()
    Displayboard(atomic)

        