# 16173 쩜프왕 쩰리(Small) (실버4)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
from collections import deque

N = int(input().strip())

visit = [[0]*N for _ in range(N)]
visit[0][0] = 1
graph = []

for _ in range(N):
    graph.append(list(map(int, input().strip().split())))

# if graph[0][0] < 5:
#     # dfs 풀이법
#     def dfs(x, y):
#         if x >= N or y >= N or visit[y][x] == 1:
#             return

#         visit[y][x] = 1

#         if graph[y][x] == -1:
#             return

#         move = graph[y][x]
#         dfs(x+move, y)
#         dfs(x, y+move)
#     dfs(0, 0)
# if  visit[-1][-1] == 1:
#     print('HaruHaru')
# else:
#     print('Hing')
# visit = [[0]*N for _ in range(N)]
    
#bfs 풀이법
def bfs(x, y):
    dx = [1,0]
    dy = [0,1]

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        move = graph[y][x]
        if visit[-1][-1] == 1:
            return

        for i in range(2):
            nx = x + dx[i]*move
            ny = y + dy[i]*move
            if nx <= N-1 and ny <= N-1:
                if visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((nx, ny))


    return

bfs(0, 0)
if  visit[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')