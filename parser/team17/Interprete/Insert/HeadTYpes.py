from enum import Enum


class HEAD(Enum):
	nameColumn = 0
	typeColumn = 1
	default = 2
	notnull = 3
	null = 4
	unique_state = 5
	unique_name = 6
	fk_state = 7
	fk_reference= 8
	fk_columnref= 9
	pk_state = 10
	check_name = 11
	check_expression = 12


