from collections import deque

s = list(input())
s2 = deque(list(reversed(s)))
s = deque(s)
Q = int(input())
q = []
f = []
c = []
count = 0

for _ in range(Q):
    tmp = list(map(str,input().split()))
    if len(tmp) == 1:
        count += 1
        q.append(int(tmp[0]))
        f.append(0)
        c.append('')
    else:
        q.append(int(tmp[0]))
        f.append(int(tmp[1]))
        c.append(tmp[2])


for i in range(Q):
    if q[i] == 1:
        tmp = s
        s = s2
        s2 = tmp
    else:
        if f[i] == 1:
            s.appendleft(c[i])
            s2.append(c[i])
        else:
            s.append(c[i])
            s2.appendleft(c[i])

for i in range(len(s)):
    print(s.popleft(),end="")
print("")

