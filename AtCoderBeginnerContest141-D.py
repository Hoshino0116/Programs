import heapq
import math

n,m = map(int,input().split())
a = list(map(int,input().split()))

a = [-1*num for num in a]

heapq.heapify(a)

for i in range(m):
	maximum = heapq.heappop(a)
	add = math.trunc(maximum/2)
	heapq.heappush(a,add)

print(-1 * sum(a))
