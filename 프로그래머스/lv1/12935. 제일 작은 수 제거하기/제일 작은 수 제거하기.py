def solution(arr):
    answer = 0
    if len(arr) == 1:
        return [-1]
    arr.pop(arr.index(min(arr)))
    return arr