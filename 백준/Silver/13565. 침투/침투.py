# 13565 침투 (실버2)

# 0에서만 전류가 흐름 -> 그래프가 0 일때 돌아야 함


import sys
sys.setrecursionlimit(10**9)
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

M, N = map(int, input().split())
visit = [[0]*N for _ in range(M)]

graph = []
for _ in range(M):
    graph.append(list(map(int, input())))

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if graph[ny][nx] == 0 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((nx, ny))
    return

for j in range(N):
    if graph[0][j] == 0 and visit[0][j] ==0:
        visit[0][j] = 1
        bfs(j, 0)

if 1 in visit[-1]:
    print('YES')
else:
    print('NO')