#bool

print('True or False: ',True or False)
print('False or False: ',False or False)
print('False or True: ',False or True)
print('True or True: ',True or True)
print('\n\n')
print('True and False: ', True and False)
print('False and False: ',False and False)
print('False and True: ',False and True)
print('True and True: ',True and True)


print('True ^ False: ',True ^ False)
print('False ^ False: ',False ^ False)
print('False ^ True: ',False ^ True)
print('True ^ True: ',True ^ True)

''' 
0 == 000
1 == 001
2 == 010
3 == 011
4 == 100 == 3^7

7 == 111 
'''

#lists

l = [1,6,[4,{'r':['abc',True]}, 0,0]] #vivesti b
print(l[2][1]['r'][0][1])

'''list(range(x)) - generator srazu v spisok'''


#LOOPs
n= 5
while n>0:
	print(n)
	n-=1

a,b,c = 0,5,1
while a<b:
	print(a, end=' ')
	a+=c

l = list(range(15))
z = 0
while z<len(l):
	print(l[z]**2, end=' ')
	z+=1
 
l2 = []
for i in range(5):
	l2.append(i**2)
print(l2)