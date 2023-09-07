# 10026 적록색약 (골드5)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

# 접근방법
# 1. 색약이 아닌 사람과 색약인 사람의 bfs를 나누어 st에 담는다?

N = int(input().strip())

graph = []
for _ in range(N):
    graph.append(list(input().strip()))

n_visit = [[0]*N for _ in range(N)]
c_visit = [[0]*N for _ in range(N)]


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt1 = 0
cnt2 = 0
# 일반 사람 nomal bfs
def n_bfs(x, y, start):
    global cnt1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N:

                if n_visit[ny][nx] == 0 and graph[ny][nx] == start:
                    n_visit[ny][nx] = 1
                    q.append((nx, ny))
    cnt1 += 1
    return

# 색약 사람 color bfs
def c_bfs(x, y, start):
    global cnt2

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if nx >= 0 and nx < N and ny >= 0 and ny < N and c_visit[ny][nx] == 0:
                
                if start == 'B' and graph[ny][nx] == start:
                    c_visit[ny][nx] = 1
                    q.append((nx, ny))
                elif start != 'B' and graph[ny][nx] != 'B':
                    c_visit[ny][nx] = 1
                    q.append((nx, ny))

    cnt2 += 1
    return

for y in range(N):
    for x in range(N):
        if n_visit[y][x] == 0:
            n_visit[y][x] = 1
            n_bfs(x, y, graph[y][x])
        if c_visit[y][x] == 0:
            c_visit[y][x] = 1
            c_bfs(x, y, graph[y][x])
print(cnt1, cnt2)