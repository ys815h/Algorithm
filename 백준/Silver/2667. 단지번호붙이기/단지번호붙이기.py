# 2667 단지번호 붙이기 (실버1)

# 단지 개수를 첫 줄에 출력
# 단지내 집 수를 오름차순 정렬하여 하나씩 출력

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

from collections import deque

N = int(input().strip())

graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().strip()))))
visit = [[0]*N for _ in range(N)]

dx = [0, 1, 0 ,-1]
dy = [-1, 0, 1, 0]

# 단지 내 집의 수 배열
st = [] 
def bfs(x, y):
    # 총 단지 수
    cnt = 1 

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N:

                if visit[ny][nx] == 0 and graph[ny][nx] == 1:

                    visit[ny][nx] = 1
                    q.append((nx, ny))
                    cnt += 1
    st.append(cnt)
    return


# 그래프 전체를 순회하면서 방문안 한 곳을 bfs 돌림
for j in range(N):
    for k in range(N):
        if visit[j][k] == 0 and graph[j][k] == 1:
            visit[j][k] = 1
            bfs(k, j)
st.sort()
print(len(st))
for i in st:
    print(i)