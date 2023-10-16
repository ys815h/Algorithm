# 1003 피보나치 함수
import sys
input = sys.stdin.readline

T = int(input().strip())


for _ in range(T):
    N = int(input().strip())

    dp = [[0, 0] for _ in range(N+1)] 

    dp[0] = [1, 0]
    if N >= 1:
        dp[1] = [0, 1]
    if N >= 2:
        for i in range(2, N+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(dp[N][0], dp[N][1])
