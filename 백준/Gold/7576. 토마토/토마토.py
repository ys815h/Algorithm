# 7576 토마토 (골드5)

# 가로 N 세로 M의 상자 창고의 모든 토마토가 익으려면 몇일이 걸리는가?

# 전체 탐색하여 마지막 지점을 return 시키면 됨

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

from collections import deque

N, M = map(int, input().strip().split())
graph = []
start = []


for y in range(M):
    graph.append(list(map(int, input().strip().split())))
    for x in range(N):
        if graph[y][x] == 1:
            start.append([x, y])

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(s):
    q = deque(s)
    x = 0
    y = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:

                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((nx, ny))
    for j in range(M):
        if 0 in graph[j]:
            return -1
    return graph[y][x] -1

print(bfs(start))