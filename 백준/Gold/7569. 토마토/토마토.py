# 7569 토마토2 (골드5)

# 가로 M 세로 N의 높이 H상자 창고의 모든 토마토가 익으려면 몇일이 걸리는가?

# 전체 탐색하여 마지막 지점을 return 시키면 됨

# 접근방법 1.
# 3차원 배열로 한다...?

# 접근방법 2.
# 3차원으로 할 필요없이 2차원 배열 내에서 H크기에 따라 변수의 값을 변동 시켜 주면 됨
# ex). (5 3 2)이 값으로 주어 졌을 때 2차원 배열의 graph[4][2] 지점이 스타트일 때
#      위아래 방향 판별을 y값 기준으로 +N -N 해서 0인 값을 찾아내면 됨

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

from collections import deque

M, N, H = map(int, input().strip().split())

start = []
graph = [[] for _ in range(H)]

for z in range(H):
    for y in range(N):
        graph[z].append(list(map(int, input().strip().split())))
        for x in range(M):
            if graph[z][y][x] == 1:
                start.append([x, y, z])

dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(start):
    q = deque(start)
    x, y, z = 0, 0, 0
    while q:
        # print('시작 q 상태', q)
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx >= 0 and nx < M and ny < N and ny >= 0 and nz < H and nz >= 0:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nx, ny, nz))

    for j in range(H):
        for k in range(N):
            if 0 in graph[j][k]:
                return -1
    return graph[z][y][x] -1

print(bfs(start))