from goto import with_goto
@with_goto
def c3d():
	t0=0
	label .begin
	if t0 == 10: goto .end
	print(t0)
	t0=t0+1
	goto .begin
	label .end
c3d()