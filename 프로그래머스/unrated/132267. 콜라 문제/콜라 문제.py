# while 문으로 남은 수량이 a 미만이 될때 까지

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
        
    return answer