def solution(n, m):
    answer = []
    
#   최대 공약수 두 수를 비교하여 작은 수만큼 for문을 돌려 최대 공약수를 구한다
#   최대 공약수는 소인수분해를 하여 공통인 소수 중 지수가 더 작은 걸 사용

#   최소 공배수 두 수를 곱하여 최대 공약수로 나눈다
    if n <= m:
        a = n
        b = m
    else:
        a = m
        b = n
    ans = 0
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            ans = i
    answer.append(ans)
    answer.append(a*b/ans)
    return answer