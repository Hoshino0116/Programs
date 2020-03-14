n = int(input())
s = input()

def z_algo(S):
    N = len(S)
    A = [0]*N
    i = 1; j = 0
    A[0] = l = len(S)
    while i < l:
        while i+j < l and S[j] == S[i+j]:
        	j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A
ans = 0
for i in range(n-1):
	tmp = z_algo(s[i:])
	for j,zj in enumerate(tmp):
		if j+1 > zj:
			ans = max(ans,zj)

print(ans)
