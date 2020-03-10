from collections import deque

H,W = map(int,input().split())
c =[]
c.append(['#' for _ in range(W+2)])
ans = [[0 for _ in range(W+2)]for _ in range(H+2)]
score = 0
for i in range(H):
    tmp = list('#'+input()+'#')
    c.append(tmp)
    for j in range(W+2):
        if tmp[j] == '.':
            score += 1

c.append(['#' for _ in range(W+2)])
q = deque()

def bfs(x,y):
    q.append([x,y])
    while q:
        x,y = q.popleft()
        if [x,y] == [W,H]:
            return ans[H][W]
        if c[y][x-1] == '.':
            q.append([x-1,y])
            ans[y][x-1] = ans[y][x] + 1
            c[y][x-1] = '#'
        if c[y][x+1] == '.':
            q.append([x+1,y])
            ans[y][x+1] = ans[y][x] + 1
            c[y][x+1] = '#'
        if c[y-1][x] == '.':
            q.append([x,y-1])
            ans[y-1][x] = ans[y][x] + 1
            c[y-1][x] = '#'
        if c[y+1][x] == '.':
            q.append([x,y+1])
            ans[y+1][x] = ans[y][x] + 1
            c[y+1][x] = '#'
    return -1

tmp = bfs(1,1)
if tmp == -1:
    print(-1)
else:
    print(score - tmp - 1)
