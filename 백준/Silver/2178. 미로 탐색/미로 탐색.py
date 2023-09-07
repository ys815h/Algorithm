# 2178 미로탐색 (실버1)
# N개의 줄에 M개의 정수 미로가 주어짐
# 1은 이동가능 0은 벽
# -1,-1 칸으로 최소 이동 횟수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

N, M = map(int, input().strip().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().strip()))))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < M and ny >= 0 and ny < N:
                if graph[ny][nx] == 1:
                    graph[ny][nx] += graph[y][x]
                    q.append((nx, ny))
    print(graph[-1][-1])
    return
bfs(0, 0)