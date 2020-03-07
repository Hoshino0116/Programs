n,k = map(int,input().split())

p = list(map(int,input().split()))

iter_num = n - k + 1

num = sum(p[0:k])
ans = [(num+k)/2]
for i in range(iter_num-1):
	num = num - p[i] + p[k+i]
	ans.append((num+k)/2)

print(max(ans))
