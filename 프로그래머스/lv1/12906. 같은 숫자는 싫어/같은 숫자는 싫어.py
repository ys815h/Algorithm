# 0과 1을 비교 같으면 popleft 다르면 append(popleft)

from collections import deque

def solution(arr):
    answer = []
    q_a = deque(arr)
    
    for i in range(0, len(arr)-1):
        
        if q_a[0] == q_a[1]:
            q_a.popleft()
        else:
            answer.append(q_a[0])
            q_a.append(q_a.popleft())
            # q_a.append(q_a.popleft())
    answer.append(q_a[0])
    return answer