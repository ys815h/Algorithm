N, M = map(int, input().split())
array = list(map(int,input().split()))
array.sort()

st = []

def dfs(start):
    if len(st) == M:
        print(*st)
        return
    
    for i in range(start, N):
        st.append(array[i])
        dfs(i)
        st.pop()
dfs(0)