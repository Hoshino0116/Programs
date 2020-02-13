import math

a,b,x = map(int,input().split())

v = a*a*b

h = x / (a*a)

if 2*x <= v:
	#x = a*b*num/2
	num = (2*x) / (a*b)
	#tan(ans) = b / num
	ans = math.degrees(math.atan(b/num))
	print('{:.12g}'.format(ans))
else:
	#v-x = a*num*a/2
	num = 2*(v-x) / (a*a)
	#tan(ans) = num / a
	ans = math.degrees(math.atan(num/a))
	print('{:.12g}'.format(ans))
