def solution(n):
    answer = 0
    
    for i in range(2, n+1):

        answer += 1
        for j in range(2, int(i ** (1/2))+1 ):
            if i % j == 0:
                answer -= 1
                break
    return answer