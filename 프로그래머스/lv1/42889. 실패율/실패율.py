# 실패율 = 스테이지 도달했으나 아직 클리어하지 못한 p의 합 / 스테이지 도달한 p의 합
# 사용자가 현재 멈춰있는 스테이지 번호 배열 = stages
# 실패율 높은 스테이지부터 내림차순
# 실패율이 같은 스테이지가 있을 때 작은 번호의 스테이지가 먼저 온다.
# ex.1
# 1번 스테이지 실패율 = (1/8)
# 2번 스테이지 실패율 = (3/7)
# 3번 스테이지 실패율 = (2/4)
# 4번 스테이지 실패율 = (1/2)
# 5번 스테이지 실패율 = (0/1)
# result = [3,4,2,1,5]

# 접근 방법 1
# 스테이지별 실패율 자료형 dic을 만듬 실패율을 키 값으로 내림차순 정렬
# dic for문돌려서 [0]인덱스 값 answer.append 후 리턴

# 중복제거를 해주는 조건문이 필요함
# from collections import deque
def solution(N, stages):
    answer = []
    # dic = []
    
    dic = [[_,0] for _ in range(1, N+1)]
    start = 0
    length = len(stages)
    stages.sort()
    # s_q = deque(stages)
    
    for i in range(1, N+1):
        cnt = 0
        if length > 0:
            for j in range(start, len(stages)):
                if stages[j] == i:
                    cnt += 1
                    start += 1
                else:
                    break
            dic[i-1][1] = cnt/length
            length -= cnt
        else:
            break

    # for i in range(1, N+1):
    #     temp = []
    #     length = len(s_q)
    #     cnt = 0
    #     while s_q:
    #         if s_q[0] == i:
    #             s_q.popleft()
    #             cnt += 1
    #         else:
    #             break
    #     # dic[i] = cnt/length
    #     temp.append(i)
    #     temp.append(cnt/length)
    #     dic.append(temp)
    # print(dic)
    dic.sort(reverse=True, key=lambda x:x[1])
    for k in dic:
        answer.append(k[0])
    return answer