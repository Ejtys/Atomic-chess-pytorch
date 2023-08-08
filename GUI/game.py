from Game.board import AtomicChessBoard
import cons

import arcade

class GameWindow(arcade.Window):
    
    def __init__(self):
        
        super().__init__(cons.SCREEN_WIDTH, cons.SCREEN_HIGHT, cons.TITLE)
        
    def setup(self):
        pass
    
    def on_draw(self):
        pass
    
    def on_update(self, delta_time: float):
        return super().on_update(delta_time)
    

def main():
    window = GameWindow()
    window.setup()
    window.run()
    
if __name__ == "__main__":
    main()