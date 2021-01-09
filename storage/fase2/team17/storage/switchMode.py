# File:     switchMode
# License:  Released under MIT License
# Notice:   Copyright (c) 2020 TytusDB Team

from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.dict import DictMode as dict
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as json
from storage.hash.storage import HashMode as hash

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

