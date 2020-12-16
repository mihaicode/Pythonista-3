x = (1, 'two', 3.0, 4, False)
y = (1, 'two', 3.0, 4, False)

print('x is {}'.format(x))

# x and y are both tuple
# each element has it's own type
print(type(x))
print(type(x[4]))
print(type(y))

# unique id's'
print(id(x))
print(id(y))

# use is:instance(x, type)
if isinstance(x, tuple()):
	print('x is tuple'.format(x))
else:
	print('Nope')
	
if isinstance(x, list()):
	print('x is list')
else:
	print('Nope')
