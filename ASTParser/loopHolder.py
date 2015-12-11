from statementHolder import Statement

#loop inherits statement
class Loop(Statement):
    #Loop has a special attribute, looptype(For, while, do)
    def __init__(self, name, parent, loopType, lineNo):
        Statement.__init__(self, name, parent, lineNo)
        self.loopType = loopType
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    #Override
    def printNode(self):
        print (self.name)
        for currentStatement in self.children:
            currentStatement.printNode()
        print ("}")

    def getLoopType(self):
        return self.loopType
