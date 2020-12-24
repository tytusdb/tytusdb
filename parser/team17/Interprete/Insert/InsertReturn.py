
from enum import Enum

class InsertReturn(Enum):
	success = 0 ,
	failed = 1,
	notExistDatabase = 2,
	notExistTable = 3,
	duplicatePrimarykey = 4,
	arrayOutOfBounds = 5,
