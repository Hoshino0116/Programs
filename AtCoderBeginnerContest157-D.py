import sys

class UnionFind():
	def __init__(self, n):
		self.n = n
		#self.parents = -1 : 親が自分で子も自分(独立)
		#self.parents = n(>0) : 親が自分でなく頂点n
		#self.parents = n(<0) : 親が自分で、子が-n個(自分含める)
		self.parents = [-1] * n
	#自分の親を求める
	def find(self, x):
		if self.parents[x] < 0:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]
	#xとyを同じ親に属させる
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		#同じ親ならもうunion済み
		if x == y:
			return
		#親が違うなら、サイズの大きい親を親とする
		if self.parents[x] > self.parents[y]:
			x, y = y, x

		self.parents[x] += self.parents[y]
		self.parents[y] = x
	#同じ親だったらTrue
	def same(self, x, y):
		return self.find(x) == self.find(y)
	#サイズ(グループの所属数)を返す
	def size(self, x):
		return self.parents[self.find(x)] * -1

#UnionFindのfind関数は再帰するため、これを設定しておく
sys.setrecursionlimit(10**9)

n,m,k = map(int,input().split())

a = []
b = []
c = []
d = []
for _ in range(m):
	tmp = list(map(int,input().split()))
	a.append(tmp[0]-1)
	b.append(tmp[1]-1)
for _ in range(k):
	tmp = list(map(int,input().split()))
	c.append(tmp[0]-1)
	d.append(tmp[1]-1)

uf = UnionFind(n)
ans = []

for i in range(m):
	uf.union(a[i],b[i])

for i in range(n):
	ans.append(uf.size(i)-1) #-1してるのは、自分自身を除くため

for i in range(m):
	if uf.find(a[i]) == uf.find(b[i]):
		ans[a[i]] -= 1
		ans[b[i]] -= 1

for i in range(k):
	if uf.find(c[i]) == uf.find(d[i]):
		ans[c[i]] -= 1
		ans[d[i]] -= 1

for i in range(n):
	print(ans[i],end=" ")
