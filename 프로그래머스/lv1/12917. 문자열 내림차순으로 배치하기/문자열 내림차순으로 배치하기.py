# 1. 문자열 리스트로 변환 후 정렬
# 2. deque에 담아 대문자 판별후 append시킴
# 3. 소문자면 break 탈출 후 문자열로 변환하여 리턴

from collections import deque

def solution(s):
    s = list(s)
    s.sort(reverse = True)
    a_q = deque(s)
    print(a_q)    
    
    for i in range(len(s)):
        if a_q[0].isupper():
            a_q.append(a_q.popleft())
        else:
            break
    return ''.join(a_q)

