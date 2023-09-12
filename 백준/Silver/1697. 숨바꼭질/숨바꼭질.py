# 1697 숨바꼭질(기초 실버1)

# import sys
# input = sys.stdin.readline
from collections import deque
N, K = map(int, input().strip().split())

graph = [0 for _ in range(100001)]
graph[N] = 0
# print(graph)

dx = [1, -1, 2]
# dy = [0, 0, 2]

def bfs(x):
    q = deque()
    q.append((x))
    while q:
        # print('q상태', q)
        x = q.popleft()

        if x == K:
            return

        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]

            if nx >= 0 and nx <= 100000:
                if graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    q.append((nx))

    return
bfs(N)
print(graph[K])
