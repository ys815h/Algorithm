# 7562 나이트의 이동 (실버1)

# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
# 첫째 줄에는 체스판의 한 변의 길이
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸

# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력

# 접근방법 1
# 말이 이동가능한 방향을 만들어 dfs 혹은 bfs로 최단횟수 를 리턴 시킴
# dfs로 이동하는곳의 방문 인덱스에 +1을 해줌


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

# 테스트 케이스 개수
N = int(input().strip())

for _ in range(N):

    M = int(input().strip())

    visit = [[0] * M for _ in range(M)]

    start = list(map(int, input().strip().split()))
    end = list(map(int, input().strip().split()))
    
    y = start[0]
    x = start[1]

    b = end[0]
    a = end[1]

    def bfs(x, y):
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]

        q = deque()
        q.append((x, y))
        
        if x == a and y == b:
            return visit[b][a]

        while q:
            x, y = q.popleft()

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < M and ny >= 0 and ny < M:

                    if visit[ny][nx] == 0:
                        visit[ny][nx] += visit[y][x] + 1
                        q.append((nx, ny))
        return visit[b][a]
    print(bfs(x, y))