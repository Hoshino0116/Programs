from collections import deque

H,W = map(int,input().split())
c =[]
c.append(['×' for _ in range(W+2)])
ans = [[10**9 for _ in range(W+2)] for _ in range(H+2)]

for i in range(H):
    tmp = list('×'+input()+'×')
    c.append(tmp)
    for j in range(W+2):
        if tmp[j] == 's':
            sx = j
            sy = i+1
        elif tmp[j] == 'g':
            gx = j
            gy = i+1


c.append(['×' for _ in range(W+2)])
q = deque()

#01bfs
def bfs(x,y):
    ans[y][x] = 0;
    q.append([x,y])
    while q:
        x,y = q.popleft()
        if x < 1 or x > W or y < 1 or y > H:
            continue
        if c[y][x-1] == '#':
            cost = 1
        else:
            cost = 0
        if ans[y][x-1] > ans[y][x] + cost:
            ans[y][x-1] = ans[y][x] + cost
            if cost == 0:
                q.appendleft([x-1,y])
            else:
                q.append([x-1,y])

        if c[y][x+1] == '#':
            cost = 1
        else:
            cost = 0
        if ans[y][x+1] > ans[y][x] + cost:
            ans[y][x+1] = ans[y][x] + cost
            if cost == 0:
                q.appendleft([x+1,y])
            else:
                q.append([x+1,y])

        if c[y-1][x] == '#':
            cost = 1
        else:
            cost = 0
        if ans[y-1][x] > ans[y][x] + cost:
            ans[y-1][x] = ans[y][x] + cost
            if cost == 0:
                q.appendleft([x,y-1])
            else:
                q.append([x,y-1])

        if c[y+1][x] == '#':
            cost = 1
        else:
            cost = 0
        if ans[y+1][x] > ans[y][x] + cost:
            ans[y+1][x] = ans[y][x] + cost
            if cost == 0:
                q.appendleft([x,y+1])
            else:
                q.append([x,y+1])

bfs(sx,sy)
if ans[gy][gx] < 3:
    print('YES')
else:
    print('NO')
