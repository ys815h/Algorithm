N, M = map(int, input().strip().split(' '))

alist = [a for a in range(1, N+1)]

st = []

def dfs():
    
    if len(st) == M:
        
        print(' '.join(map(str, st)))
        return

    
    for i in alist:
        if i not in st:
            st.append(i)
            dfs()
            st.pop()
dfs()