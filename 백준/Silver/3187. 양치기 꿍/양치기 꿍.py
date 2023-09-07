# 3187 양치기 꿍 (실버1)
# 입력 첫 줄에 R,C가 주어짐 (세로, 가로)
# 빈 공간을 '.'(점) 울타리를 '#', 늑대를 'v', 양을 'k'
#  몇 마리의 양과 늑대가 살아남는가?
# 울타리 안에 양이 더 많을 경우 늑대는 없어지고 반대의 경우엔 늑대만 남는다

# 접근방법
# 1. 울타리가 아닌 곳은 모두 방문
# 조건문을 통해 v와 k의 수를 계산
# 울타리 안에서 v와 k를 비교 많은쪽만 남김

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

R, C = map(int, input().strip().split())

graph = []
for _ in range(R):
    graph.append(list(input().strip()))

visit = [[0]*C for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 양과 늑대의 수를 담는 배열
st = [0, 0]

def bfs(x, y):
    k = 0   # 해당 울타리안 양의 수
    v = 0   # 해당 울타리안 늑대 수
    q = deque()
    q.append((x, y))

    if graph[y][x] == 'k':
        k += 1
    elif graph[y][x] == 'v':
        v += 1

    while q:
        x, y = q.popleft()
        

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < C and ny >= 0 and ny < R:

                if visit[ny][nx] == 0 and graph[ny][nx] != '#':
                    visit[ny][nx] = 1
                    q.append((nx, ny))

                    if graph[ny][nx] == 'k':
                        k += 1
                    elif graph[ny][nx] == 'v':
                        v += 1
    if k > v:
        v = 0
    elif k <= v:
        k = 0
    st[0] += k
    st[1] += v

    return

for y in range(R):
    for x in range(C):
        if visit[y][x] == 0 and graph[y][x] != '#':
            visit[y][x] = 1
            bfs(x, y)
print(st[0], st[1])