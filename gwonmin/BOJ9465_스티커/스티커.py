import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stic = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1] = stic[0][0]
    dp[1][1] = stic[1][0]

    for i in range(2,n+1):
        dp[0][i] = max(dp[1][i-1],dp[1][i-2]) + stic[0][i-1]
        dp[1][i] = max(dp[0][i-1],dp[0][i-2]) + stic[1][i-1]

    print(dp)
    print(max(dp[0][-1],dp[1][-1]))