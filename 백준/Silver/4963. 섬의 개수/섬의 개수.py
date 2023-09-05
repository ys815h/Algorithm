# 4963 섬의 개수
# 섬(1)과 바다(0) 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 접근방법 1.
# 연결되는 경로들의 개수를 구하면 됨
# 방문하지 않은 곳들을 시작으로 bfs함수를 돌림

import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 밖으로 나가지 않는 조건
            if nx >= 0 and nx < w and ny >= 0 and ny < h:
                # 지도에서 지나갈 수 있는 조건
                if graph[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((nx, ny))
    return


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    
    graph = []
    cnt = 0
    visit = [[0] * w for _ in range(h)]

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and graph[i][j] == 1:
                visit[i][j] = 1
                bfs(j, i)
                cnt += 1
    print(cnt)