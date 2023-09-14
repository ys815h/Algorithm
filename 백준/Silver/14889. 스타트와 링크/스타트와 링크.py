# 14889 스타트와 링크 (실버 2)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N = int(input().strip())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip().split())))

visit = [0] * N
st = []
# N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.
# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치

minval = 4455

def dfs(v):
    global minval
    if len(st) == (N/2):
        team1 = 0
        team2 = 0
        for i in range(N):
            for j in range(N):
                if i != j:
                    if visit[i] != 0 and visit[j] != 0:
                        team1 += graph[i][j]
                    elif visit[i] == 0 and visit[j] == 0:
                        team2 += graph[i][j]
        minval = min(minval, abs(team1 - team2))
        return
    for k in range(v, N):
        if visit[k] == 0:
            visit[k] = 1
            st.append(k)
            dfs(k)
            st.pop()
            visit[k] = 0
            if len(st) == 0:
                return
    return
dfs(0)
print(minval)