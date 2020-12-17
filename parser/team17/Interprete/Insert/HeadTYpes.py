from enum import Enum


class HEAD(Enum):
	nameColumn = 0
	typeColumn = 1
	default = 2
	notnull = 3
	null = 4
	unique = 5
	fk = 6
	pk = 7
	check = 8


class Foreign(Enum):
	state = 0
	references = 1
