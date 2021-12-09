x = 50
print(x)
def func():
	global x, y

	print ('x ravno', x)
	x=2
	y=3
	print('x uzhe ravno', x)

func()
print('x ravno', x)

print(x, y)