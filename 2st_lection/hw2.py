x = '1234'
x = x.rjust(len(x)+3, '0')
c, z = 3,len(x)

while c>=0:
	print(x[c:z])
	c-=1
	z-=1