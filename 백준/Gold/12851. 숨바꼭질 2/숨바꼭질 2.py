# 12851 숨바꼭질(골드 4)

# import sys
# input = sys.stdin.readline
from collections import deque
N, K = map(int, input().strip().split())

graph = [0 for _ in range(100001)]
graph[N] = 0
dx = [-1, 1, 2]
cnt = 0
max = 0
def bfs(x):
    
    global cnt, max

    if x == K:
        cnt = 1
        return

    q = deque()
    q.append((x))
    while q:
        # print('q상태', q)
        x = q.popleft()

        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]

            if nx == N:
                continue
            if N > K:
                if nx >= 2*K and nx >= N:
                    continue
            else:
                if nx >= 2*K:
                    continue

            if nx >= 0 and nx <= 100000:
            # if nx >= 0 and nx <= 10:

                if graph[nx] == 0:
                    if nx == K:
                        if graph[x] + 1 == max:
                            cnt += 1
                        if max == 0:
                            max = graph[x] + 1
                            cnt += 1
                        continue
                    graph[nx] = graph[x] + 1
                    q.append((nx))
                elif graph[nx] != 0 and graph[nx] == graph[x] + 1:
                    q.append((nx))

    return
bfs(N)
print(max)
print(cnt)
