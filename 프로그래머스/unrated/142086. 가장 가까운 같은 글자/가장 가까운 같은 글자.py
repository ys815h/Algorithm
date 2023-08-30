# st을 for문을 돌림
# d_q를 두개 만들어 하나는 s의 배열 array의 값들을 담고 하나는 인덱스 값들을 담음

# from collections import deque

# def solution(s):
#     answer = []
#     array = list(s)
#     p_q = deque([])
    
#     for i in array:
#         if i in p_q:
#             answer.append(p_q.index(i)+1)
#             p_q.appendleft(i)
#         else:
#             p_q.appendleft(i)
#             answer.append(-1)
        
#     return answer


def solution(s):
    answer = []
    dic = {}

    for i in range(len(s)):
        if s[i] in dic:
            answer.append(i - dic[s[i]]);
            dic[s[i]] = i;
        else:
            answer.append(-1);
            dic[s[i]] = i;

    return answer