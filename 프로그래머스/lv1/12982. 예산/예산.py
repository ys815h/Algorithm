# 신청한 금액이 들어있는 배열 d, 예산 budget
# 예산내에서 최대 개수를 구해야 함

# 방법1 오름차순 정렬 후 구매 해줄 수 있을 때까지 cnt++

def solution(d, budget):
    cnt = 0
    
    d.sort()
    for i in range(len(d)):
        
        if budget >= d[i]:
            budget -= d[i]
            cnt += 1
    
    return cnt