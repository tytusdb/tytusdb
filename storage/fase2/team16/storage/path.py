from .avl import avl_mode as avl
from .b import b_mode as b
from .bplus import bplus_mode as bplus
from .dict import dict_mode as dict
from .hash import hash_mode as hash
from .isam import isam_mode as isam
from .json import json_mode as json


def actionCreator(mode: str, function: str, args=[]):
    action = mode + "." + function + "("
    if len(args) != 0:
        for x in args:
            action += x + ", "
        action = action[:-2]
    action += ")"
    return action
