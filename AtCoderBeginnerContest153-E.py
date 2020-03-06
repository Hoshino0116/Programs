H,N= map(int,input().split())

a = []
b = []

for i in range(N):
  a_dash,b_dash = map(int,input().split())
  a.append(a_dash)
  b.append(b_dash)

#dp[i+1][j] = i番目までの魔法で体力jのモンスターに
#勝つことができる、魔力の最小値
INF = 10**9
dp = [[INF for _ in range(H+1)] for _ in range(N+1)]

#体力0のモンスターは初めからデスしている
for i in range(N+1):
  dp[i][0] = 0

for i in range(N):
  for j in range(H+1):
    if a[i] > j:
      dp[i+1][j] = min(dp[i][j],b[i])
    else:
      dp[i+1][j] = min(dp[i][j],dp[i+1][j-a[i]]+ b[i])

print(dp[N][H])
