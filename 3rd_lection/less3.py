l = [i**2 for i in range(10) if not i%2] #list v 1 stroku

s = 'wwwwwwwwwwwwwwwwwwwwwwwewwwwwwwwwwwwwwwwwwwwww'

# continue for loops
for i in s:
	if i == 'e':
		continue
	print(i)
	
# break for loops	
for i in s:
	if i == 'e':
		break
	print(i)
	
#methods .split and .join

abcd = 'a b c d'.split() # sdelaet spisok iz 'a b c d'

','.join(abcd) # soedenit spisok v stroku

s1 = 'GitHub is home to over 20 million developers working together to host and review code, manage projects, and build software together.'
s2 = ''.join([i for i in s1 if i.isalpha()])
print(s2)

s3 = 'GitHub is.....me to over 20 mil.....de, ...nage projects, an... software together.'
l2 = []
for i in s3:
	if i.isalpha():
		l2.append(i)
	else:
		l2.append(' ')

print(' '.join(l2).split())

#CRUD C-create R-read U-update D-deleter

l = [1] # create
d = {}
d['s'] = 1 # create
print(l,d) # READ
l.append(2) # UPDATE
d['s']  = 2 # UPDATE
del l[0] # DELETE
del d[s] #DELETE

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