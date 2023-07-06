N, M = map(int, input().split(' '))

alist = [a for a in range(1, N+1)]

st = []
start = 0

def dfs():
    if len(st) == M:
        print(' '.join(map(str, st)))
        return

    if st:
        start = st[-1]
    else:
        start = 0
    for i in range(start, N):
        if alist[i] not in st:
            st.append(alist[i])
            dfs()
            st.pop()
dfs()