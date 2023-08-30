# answer 초기 값을 1로 설정 -> number가 2이상일 때 조건으로 변경
# 약수의 개수 cnt를 answer에 계속 담음 마지막으로 answer return
# cnt > limit일 경우 temp에 power를 담음

# 시간초과 문제 해결 방법
# 1. 
# 제곱근까지 범위 설정(for문 탐색 범위 줄이기)
# 제곱근일때는 cnt*2-1 아닐땐 cnt*2조건을 걸어줌

def solution(number, limit, power):
    answer = 1
    cnt = 0
    
    if number > 1:
        for i in range(2, number+1):
            cnt = 0
            
            for j in range(1, int((i**(1/2))+1 )):
                if i % j == 0:
                    cnt += 1
            
            if int((i ** (1/2))) * int((i ** (1/2))) == i:
                cnt = cnt * 2 - 1
            else:
                cnt *= 2
            if cnt > limit:
                cnt = power
            answer += cnt
    return answer