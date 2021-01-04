from goto import with_goto
from interpreter import execution
from c3d.stack import  Stack

stack = {}


@with_goto
def principal():
	t0 = "use test;"
	stack['t0'] = t0
	funcionIntermedia()



def funcionIntermedia(tn):
	execution(stack['tn'])
principal()