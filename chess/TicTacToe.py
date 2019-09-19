from Move import Move
from Node import Node

class AB:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

class TicTacToe:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.size = 3
        
    def getPlayerMove(self):
        while(True):
            str = input("[O] > ")
            if(len(str) != 2):
                continue
            
            x = str[1]
            y = str[0]
            if(x >= '1' and x <= '3' and y >= 'a' and y <= 'c'):
                if(self.board[ord(x) - ord('1')][ord(y) - ord('a')] != 0):
                    continue
                return Move(ord(x) - ord('1'), ord(y) - ord('a'), 1)

    def evaluate(self):
        value = 0
        for i in range(self.size):
            line = [0, 0, 0]
            for j in range(self.size):
                line[j] = self.board[i][j]
            v = self.getValue(line)
            if(v == 1000 or v == -1000):
                return v
            value += v

        for j in range(self.size):
            line = [0, 0, 0]
            for i in range(self.size):
                line[i] = self.board[i][j]
            v = self.getValue(line)
            if(v == 1000 or v == -1000):
                return v
            value += v

        line = [0, 0, 0]
        for i in range(self.size):
            line[i] = self.board[i][i]
        
        v = self.getValue(line)
        if(v == 1000 or v == -1000):
                return v
        value += v
        for i in range(self.size):
            line[i] = self.board[i][self.size - i - 1]

        v = self.getValue(line)
        if(v == 1000 or v == -1000):
                return v
        value += v
        return value

    def getValue(self, line):
        p1 = 0
        p2 = 0
        for n in line:
            if n == 1:
                p1 += 1
            if n == 2:
                p2 += 1
        if(p1 > 0 and p2 > 0):
            return 0
        if(p1 == 3):
            return 1000
        if(p1 == 2):
            return 10
        if(p1 == 1):
            return 1
        if(p2 == 3):
            return -1000
        if(p2 == 2):
            return -10
        if(p2 == 1):
            return -1
        return 0

    def getVaildMoves(self, player):
        result = []
        value = self.evaluate()
        if(value == 1000 or value == -1000):
            return result
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    result.append(Move(i, j, player))
        return result

    def move(self, m):
        self.board[m.getX()][m.getY()] = m.getPlayer()

    def unmove(self, m):
        self.board[m.getX()][m.getY()] = 0

    def makeTree(self, curPlayer, move, depth):
        root = Node()
        moves = self.getVaildMoves(curPlayer)
        if(depth == 0 or len(moves) == 0):
            v = self.evaluate()
            if curPlayer == 2:
                v *= -1
            root.setVal(v)
            #print('v:' + str(v), end = " ")
        root.setMove(move)
        #if move is not None:
            #print(move.toString(), end = " ")
        if depth > 0:
            for m in moves:
                self.move(m)
                if curPlayer == 1:
                    curPlayer = 2
                else:
                    curPlayer = 1
                root.addChild(self.makeTree(curPlayer, m, depth - 1))
                self.unmove(m)
        return root              

    def alphabeta(self, node, depth, alpha, beta):
        if(depth == 0 or len(node.getChildren()) == 0):
            return AB(node.getVal(), -1)
        selectedIdx = -1
        nodes = node.getChildren()
        i = 0
        for n in nodes:
            value = -1 * self.alphabeta(n, depth - 1, -1 * beta, -1 * alpha).val
            if(value > alpha):
                alpha = value
                selectedIdx = i
            if(alpha > beta):
                 return AB(alpha, selectedIdx)
            i += 1
        return AB(alpha, selectedIdx)

    def isGameOver(self, curPlayer):
        moves = self.getVaildMoves(curPlayer)
        if(len(moves) == 0):
            return True
        value = self.evaluate()
        if(value == 1000 or value == -1000):
            return True
        return False

    def printBoard(self):
        print("  a b c   ")
        for i in range(self.size):
            print(i + 1, end=" ")
            for j in range(self.size):
                if(self.board[i][j] == 0):
                    print(end = "  ")
                elif(self.board[i][j] == 1):
                    print("O", end = " ")
                else:
                    print("X", end = " ")
            print(i + 1)
        print("  a b c")

ttt = TicTacToe()
curPlayer = 1
depth = 2
while True:
    ttt.printBoard()
    if ttt.isGameOver(curPlayer):
        break
    if (curPlayer == 1):
        ttt.move(ttt.getPlayerMove())
    else:
        root = ttt.makeTree(curPlayer, None, depth)
        ab = ttt.alphabeta(root, depth, -1001, 1001)
        move = root.getChildren()[ab.idx].getMove()
        print("[X] > " + move.toString())
        print()
        ttt.move(move)
    if curPlayer == 1:
        curPlayer = 2
    else:
        curPlayer = 1
    
v = ttt.evaluate()
if v > 0:
    print("Player win")
elif v < 0:
    print("PC win")
else:
    print("Draw")