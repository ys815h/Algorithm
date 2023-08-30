# 카드 뭉치에서 카드를 순서대로 한 장씩 사용
# 중복 불가능
# 모든 카드를 사용
# 목표의 배열을 달성 해야 함

# 접근방법 1.
# 접근방법 2. 모든 경우의 수의 순열을 구하여 st에 담고 st안에 goal이 있으면 "Yes" return 없으면 "No"
from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    
    q1 = deque(cards1)
    q2 = deque(cards2)
    st = []
    # for i in goal:
    #     if len(q1) > 0:
    #         if q1[0] == i:
    #             st.append(q1.popleft())
    #             continue
    #     if len(q2) > 0:
    #         if q2[0] == i:
    #             st.append(q2.popleft())
    
    for i in goal:
        if len(q1) > 0 and q1[0] == i:
            st.append(q1.popleft())
            continue
        if len(q2) > 0 and q2[0] == i:
            st.append(q2.popleft())
                
    if st == goal:
        answer = "Yes"
    else:
        answer = "No"

#     def permutation(q1, q2, goal):
#         if len(st2) == len(goal):
#             st.append(st2)
#             return
        
#         for i in q1:
#             st2.append(q1.popleft())
#             permutation(q1, q2, goal)
                       
#         for i in q2:
#             st2.append(q2.popleft())
#             permutation(q1, q2, goal)
#         print(st2)
#         st2.pop()
#     permutation(q1, q2, goal)    
    return answer