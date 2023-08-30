# 전체 길이 n, 롤러의 길이 m, 칠해야 하는 구역 배열 section
import math
def solution(n, m, section):
    start = 0
    answer = 1
    for i in range(1, len(section)):
        if section[i] - section[start] + 1 > m:
            answer += 1
            start = i
    return answer