from time import time as t

t1 = t()

n = range(10**4)
l = []
d = {}

for i in n:
	l.append(i)
print(t()-t1)
for i in n:
	d[str(i)] = i
print(t()-t1)