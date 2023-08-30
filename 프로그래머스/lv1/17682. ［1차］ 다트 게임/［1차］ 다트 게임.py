# 총 3번의 기회, 각 기회 점수 범위(0~10), S는 그대로 D는 제곱 T는 세제곱 (보너스는 하나씩)
# 옵션으로 *은 해당 점수와 직전에 얻은 점수를 각 2배로 만듬(*은 처음으로 나올 수도 있음)
# 중첩으로 첫번째 * 두번째 * 이 뜬다면 첫번째 점수는 4배
# #은 해당 점수를 마이너스로 만듬
# *과 #도 중첩 가능 (첫번째 # 두번째 *의 경우 첫번째 는 2배의 마이너스 점수가 됨)
# *과 #은 있을수도 없을수도 있음
# 점수|보너스|[옵션] 순임
def solution(dartResult):
    answer = 0
    a = list(dartResult)
    temp = 0
    preTemp = 0
    nowTemp = 0
    testTemp = 0
    for i in range(len(a)):
        if a[i].isdigit():
            if a[i-1].isdigit():
                nowTemp = 10
                continue
            answer += temp # 모든 경우의 수를 통과 후 불변의 값을 answer에 더함
            temp = preTemp
            preTemp = nowTemp
            nowTemp = int(a[i])
            # testTemp = int(a[i])
            # nowTemp = testTemp
        elif a[i] == 'S':
            continue
        elif a[i] == 'D':
            nowTemp = nowTemp ** 2
        elif a[i] == 'T':
            nowTemp = nowTemp ** 3
        elif a[i] == '*':
            preTemp *= 2
            nowTemp *= 2
        else:
            nowTemp *= -1

    answer += preTemp + nowTemp + temp
    return answer