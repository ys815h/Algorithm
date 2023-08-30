# 최고 점수순으로 사과 m개를 담은 상자들에서 각 상자의 가장 낮은 점수 * m 을 합친 값을 리턴

# 1. score 내림차순 정렬
# 2. 2차원 배열에 m개가 될때까지 담음
def solution(k, m, score):
    answer = 0
    box = []
    st = []
    score.sort(reverse = True)
    for i in score:
        if len(st) == m:
            box.append(st)
            st = []
        st.append(i)
    if len(st) == m:
        box.append(st)
    for j in box:
        answer += min(j)*m
    return answer