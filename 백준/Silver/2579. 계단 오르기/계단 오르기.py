import sys
input = sys.stdin.readline

n = int(input().strip())
stairs = [int(input().strip()) for _ in range(n)]
dp = [0 for _ in range(n)]

# 처음 이동시 경우의 수 와 이후 경우의 수를 나눠 점화식을 만드는 것이 포인트!

# 첫칸 이동
dp[0] = stairs[0]

if n >= 2:
    # 첫칸 이동 후 한칸 이동
    dp[1] = dp[0] + stairs[1]
if n >= 3:
    # 첫칸 이동후 두칸 이동과 처음 두칸이동후 한칸이동 비교
    dp[2] = max(dp[0]+stairs[2], stairs[1]+stairs[2])
if n >= 4:
    for i in range(3, n):
        # 4번째 칸에서부터 생각해야 할 조건
        # 1,3,4 칸이동과 2,4칸이동을 비교 (2에는 1이 포함됨 즉, 1,2,4가 됨)
        # 1은 0을 포함하므로 스킵 즉 (1,3,4칸이동 비교 or 1,2 4칸이동)
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[-1])