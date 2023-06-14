def solution(x):
    answer = list(map(int, list(str(x))))
    temp = 0
    return x % sum(answer) == 0