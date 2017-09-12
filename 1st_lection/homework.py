def d(a,b,c):
	dis = b**2-4*a*c
	if dis < 0:
		return 'нет явных корней'
	if dis == 0:
		x = -b/2*a
		return round(x, 3)
	else:
		dis = dis**0.5
		x1 = (-b+dis)/(2*a)
		x2 = (-b-dis)/(2*a)
		return round(x1,3), round(x2,3)