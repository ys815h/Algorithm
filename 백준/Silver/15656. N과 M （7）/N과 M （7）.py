N, M = map(int, input().split())

array = list(map(int,input().split()))

array.sort()
st = []

def dfs():
    if len(st) == M:
        print(*st)
        return
    

    for i in range(len(array)):
        st.append(array[i])
        dfs()
        st.pop()
dfs()