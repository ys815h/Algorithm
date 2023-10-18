# 14888 연산자 끼워넣기 (실버 1)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input().strip())

a = list(map(int, input().strip().split()))
cal_list = list(map(int, input().strip().split()))
visit = [0 for _ in range(n)]

cal = []
for i in range(4):
    if (i+1) % 4 == 1:
        for _ in range(cal_list[i]):
            cal.append('+')
    elif (i+1) % 4 == 2:
        for _ in range(cal_list[i]):
            cal.append('-')
    elif (i+1) % 4 == 3:
        for _ in range(cal_list[i]):
            cal.append('*')
    elif (i+1) % 4 == 0:
        for _ in range(cal_list[i]):
            cal.append('/')
max_v = -1000000000
min_v = 1000000000
st = []

def dfs(v):
    global max_v, min_v
    
    if len(st) ==  n-1:
        cnt = a[0]
        for j in range(1, n):
            if st[j-1] == '+':
                cnt += a[j]
            elif st[j-1] == '-':
                cnt -= a[j]
            elif st[j-1] == '*':
                cnt *= a[j]
            elif st[j-1] == '/':
                cnt = int(cnt / a[j])

        if cnt > max_v:
            max_v = cnt
        if cnt < min_v:
            min_v = cnt
        return
    
    log = ''
    for x in range(n-1):
        if visit[x] == 0 and log != cal[x]:
            log = cal[x]
            visit[x] = 1
            st.append(cal[x])
            dfs(x)
            visit[x] = 0
            st.pop()
    return
dfs(0)
print(max_v)
print(min_v)