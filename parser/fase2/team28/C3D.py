from goto import with_goto
from controllers.three_address_code import ThreeAddressCode

@with_goto
def main():
	stack = ThreeAddressCode()

	t0 = "SELECT 8+6*50-10/5;"
	t1 = "SELECT * from holawhere id = 5;"
	t2 = "SELECT 10/5;"
	t3 = "SELECT 10/5;"
	t4 = 6 * 50
	t5 = 8 + t4
	t6 = 10 / 5
	t7 = t5 - t6
	t8 = 10 / 5
	t9 = 10 / 5

main()