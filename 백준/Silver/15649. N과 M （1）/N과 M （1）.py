from collections import deque

N, M = map(int,input().split())

st = deque()
# 재귀함수
def dfs(N, M):

    if len(st) == M:
        print(*st)
        return  # 마지막으로 실행된 함수 종료 이제 그 위로 올라감
    
    for i in range(1, N+1):

        if i not in st:
            st.append(i)
            dfs(N, M)
            # print와 return 이후 여기로 와서 진행됨
            st.pop()
dfs(N, M)