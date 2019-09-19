class Node:
    def __init__(self):
        self.val = 0
        self.move = None
        self.children = []

    def newInit(self, val):
        self.val = val
        self.move = None
        self.children = []

    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val = val
    
    def getMove(self):
        return self.move

    def setMove(self, move):
        self.move = move

    def getChildren(self):
        return self.children

    def setChildren(self, children):
        self.children = children

    def addChild(self, node):
        self.children.append(node)
