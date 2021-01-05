from AVLMode import avlMode as avl
from BMode import BMode as b
from BPlusMode import BPlusMode as bplus
from DictMode import DictMode as dict
from IsamMode import ISAMMode as isam
from JsonMode import jsonMode as json
from HashMode.storage import HashMode as hash

def switchMode(mode):
    if mode == 'avl':
        return avl
    elif mode == 'b':
        return b
    elif mode == 'bplus':
        return bplus
    elif mode == 'dict':
        return dict
    elif mode == 'isam':
        return isam
    elif mode == 'json':
        return json
    elif mode == 'hash':
        return hash





