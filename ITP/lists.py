x = (1, 2, 3, 4, 5, 6)

for i in x:
	print('-----')
	print(type(i))
	print(type('i {}'.format(i)))
	
y = ('cat', 'dog', 4, True, 0.5)
for i in y:
	print('------')
	print(i)

z = range(10)
for i in z:
	print('------')
	print(i)
