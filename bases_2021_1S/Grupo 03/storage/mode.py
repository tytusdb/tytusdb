from storage.AVL import avlMode
from storage.BTree import BMode as bMode
from storage.BPTree import BPlusMode as bPlusMode
from storage.ISAM import ISAMMode as isamMode
from storage.Hash.storage import HashMode as hashMode
from storage.JSON import jsonMode


def mode(mode):
    if mode == 1:
        return avlMode
    elif mode == 2:
        return bMode
    elif mode == 3:
        return bPlusMode
    elif mode == 4:
        return isamMode
    elif mode == 5:
        return hashMode
    elif mode == 6:
        return jsonMode

    return None
