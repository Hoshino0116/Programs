import sys

f = open('input.txt')
line = f.readline()
l_list = []
while line:
	l = line.split(':')
	if len(l) == 1:
		m = int(l[0])
		break
	l_list.append(l)
	line = f.readline()
f.close

a = []
b = []
for n in range(len(l_list)):
	if m % int(l_list[n][0]) == 0:
		a.append(int(l_list[n][0]))
		b.append(l_list[n][1])
if len(a) == 0:
	print(m)
	sys.exit()

c = zip(a,b)
c = sorted(c)

for i,s in c:
	print(s.rstrip('\n'),end="")
print("")