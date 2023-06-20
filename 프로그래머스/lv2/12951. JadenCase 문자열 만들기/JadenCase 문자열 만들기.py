def solution(s):
    a = []
    arr = s.split(" ")
    for i in range(len(arr)):
        if arr[i] != '':
            a.append(arr[i][0].upper() + arr[i][1:].lower())
        else:
            a.append(arr[i])
    return " ".join(a)