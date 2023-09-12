# 6118 숨바꼭질(실버1)

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

from collections import deque

N, M = map(int, input().strip().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().strip().split())
    graph[s].append(e)
    graph[e].append(s)

for g in range(1, N+1):
    graph[g].sort()

visit = [0] * (N+1)
st = []
def bfs(v):
    q = deque()
    q.append(v)
    visit[1] = 1
    while q:
        v = q.popleft()

        for j in graph[v]:
            if visit[j] == 0:
                visit[j] = visit[v] + 1
                q.append(j)
                # st.append([j, visit[j]-1])

bfs(1)

m = max(visit)
print(visit.index(m), m-1, visit.count(m))

# cnt = 1
# for i in range(len(st)):
#     if i > 0:
#         if st[i][1] == st[i-1][1]:
#             cnt += 1
#         else:
#             break
# st.sort()
# st.sort(reverse=True, key=lambda x:(x[1]))
# print(st[0][0], st[0][1], cnt)
