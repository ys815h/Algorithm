# 제곱근으로 나눈 나머지가 0이면 홀수 임 이것만 빼면됨
# 범위는 left부터 right까지 if문을 통해 덧셈 뺄셈 결정


def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if i % (i ** (1/2)) == 0:
            answer -= i
        else:
            answer += i
    return answer

# print(solution(13, 17))