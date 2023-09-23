# 다리길이 = bridge_length
# 최대 하중 = weight
# 트럭 배열 = truck_weights

# 다리를 줄줄이 소세지로 건너는것이 아닌 넓은 다리를 여러 차선으로 하나씩 건넌다고 생각해야 함
# 1.접근방법
# 3가지 조건 st비어있을 때, st에 트럭을 더 추가할 수 있을 때, 그것도 아닐 때
# 한 트럭이 지나는데 소요되는시간은 다리 길이

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    t_q = deque(truck_weights)
    st = deque([0] * bridge_length)
    total = 0
    while t_q:
        answer += 1
        total -= st.popleft()
        if total + t_q[0] > weight:
            st.append(0)
        else:
            w = t_q.popleft()
            total += w
            st.append(w)
            
    answer += bridge_length
            
    return answer