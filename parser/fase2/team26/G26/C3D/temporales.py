import sys
sys.path.append('../G26/C3D')

class Code3D():
    def __init__(self):
        self.index = -1
        self.indexif = -1
        self.index2 = -1

    def newTemp(self) -> str:
        self.index += 1
        return 't'+str(self.index)
    
    def newTempif(self) -> str:
        self.indexif += 1
        return 'if'+str(self.indexif)

    def newLabel(self):
        self.index2 += 1
        return 'L_case_'+str(self.index2)

    def getindex2(self):
        return self.index2

    def getcurrent(self) -> str:
        return 't'+str(self.index)

    def restartTemp(self):
        self.index = -1
