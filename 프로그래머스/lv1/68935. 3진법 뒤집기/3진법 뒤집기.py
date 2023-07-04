from collections import deque

def solution(n):
    answer = 0
    d_q = deque([])
    
    # 3진수 변환
    while n > 0:
        if n % 3 == 0:
            d_q.appendleft(0)
            n = n / 3
        else:
            d_q.appendleft(int(n % 3))
            n = (n-n%3)/3
    print(d_q)
    for i in range(len(d_q)):
        answer += d_q[i] * 3**i
    return answer