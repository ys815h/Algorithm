# 총금액을 만들어 탄횟수 만큼 곱해서 총금액에 더함
# 총금액 - money > 0 이면 그 값을 리턴 else 0 리턴

def solution(price, money, count):
    totalM = 0
    
    for i in range(1, count+1):
        totalM += i * price
    answer = totalM - money
    if answer > 0:
        return answer
    else:
        return 0
