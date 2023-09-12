from collections import deque

# 길이는 n
# arr1 배열의 값들을 이진법으로 변환 후 1이면 '#' 0이면 ' ' answer에 넣어줌
# arr2 배열의 값들을 이진법으로 변환 후 1일때 해당 인덱스의 answer 값이 0 일때 '#' 넣어줌 0이면 그냥 넘어감
# 2진법으로 변환 후 담은 st의 길이가 n이하일때 n-len(st) 만큼 2차원 배열중 st[][]에 ' '넣어줌

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        temp = ''
        a1 = list(format(arr1[i], 'b').rjust(n, '0'))
        a2 = list(format(arr2[i], 'b').rjust(n, '0'))
        for j in range(n):
            if a1[j] == '1' or a2[j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer