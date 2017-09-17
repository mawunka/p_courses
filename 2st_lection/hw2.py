x = '1234'
x = x.rjust(3, '0')
c, z = 3,len(y)

while c>-1:
	print(y[c:z])
	c-=1
	z-=1