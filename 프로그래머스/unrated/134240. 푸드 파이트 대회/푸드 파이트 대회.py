def solution(food):
    answer = ''
    st = ''
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            st += str(i)
    answer += st
    array = list(st)
    array.sort(reverse=True)
    answer += '0'
    answer += ''.join(array)
    
    return answer