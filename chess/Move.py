class Move:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPlayer(self):
        return self.player

    def toString(self):
        str = ''
        str += chr(ord('a') + self.y)
        str += chr(ord('1') + self.x)
        return str

