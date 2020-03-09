from collections import deque

H,W = map(int,input().split())
c =[]
c.append(['×' for _ in range(W+2)])
ans = []
ans.append([0 for _ in range(W+2)])
q = deque()
for i in range(H):
    tmp = list('×'+input()+'×')
    ans_tmp = []
    for j in range(W+2):
        if tmp[j] == '#':
            ans_tmp.append(0)
            q.append([j,i+1])
        elif tmp[j] == '×':
            ans_tmp.append(0)
        else:
            ans_tmp.append(10**4)
    c.append(tmp)
    ans.append(ans_tmp)

c.append(['×' for _ in range(W+2)])
ans.append([0 for _ in range(W+2)])


def bfs(q):
    while q:
        x,y = q.popleft()
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

bfs(q)
max_ans = 0
for i in range(H+2):
    #print(ans[i])
    max_ans = max(max_ans,max(ans[i]))

print(max_ans)
