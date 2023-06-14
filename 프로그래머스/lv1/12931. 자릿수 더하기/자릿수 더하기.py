def solution(n):
    answer = 0

    ch_str = str(n)
    ch_list = list(ch_str)
    for i in ch_list:
        answer += int(i)

    return answer