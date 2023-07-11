# 최소 공배수와 같은 느낌 최소한의 길이로 모든 사이즈를 담을 수 있는 지갑 만들기
# 1. 모든 배열을 정렬 시킨다
# [i][0] 인덱스의 값들을 w배열에 담음
# [i][1] 인덱스의 값들을 h배열에 담음
# max(w)*max(h) = result
# 2. 람다식으로 풀이법 생각해 보기
# -x[0]인덱스 w로 담음
# 8,4   6,5     6,3     3,7
# 14,7  12,3    10,7    8,15    5,15

# -x[1]인덱스 h로 담음?
# 3,7   6,5     8,4     6,3
# 8,15  5,15    14,7    10,7    12,3
# if w[0] > h[0] -> 


def solution(sizes):
    # sizes.sort(key = lambda x: -x[1])
    
    w = []
    h = []
    for i in range(len(sizes)):
        sizes[i].sort()
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    
    answer = max(w) * max(h)
    return answer