def func_outer():
	x = 2
	print('x ravno', x)

	def func_inner():
		global x
		x = 5

	func_inner()
	print(x)

func_outer()