import sys
sys.path.append('../G26/C3D')

class Code3D():
    def __init__(self):
        self.index = -1

    def newTemp(self) -> str:
        self.index += 1
        return 't'+str(self.index)

    def getcurrent(self) -> str:
        return 't'+str(self.index)

    def restartTemp(self):
        self.index = -1
