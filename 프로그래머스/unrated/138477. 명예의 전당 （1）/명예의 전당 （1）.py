# 명예의 전당 점수 중 가장 낮은 점수를 발표점수로 나타냄
# 1. score 길이 만큼 for문 array에 append (이 때 정렬을 해야 하는가?)
# 2. min(score)값을 answer에 append
# 3. 길이가 3일때 min값과 비교 크면  append

def solution(k, score):
    answer = []
    st = []
    for i in score:
        if len(st) == k:
            if min(st) < i:
                st.pop(st.index(min(st)))
                st.append(i)
                answer.append(min(st))
            else:
                answer.append(min(st))
        else:
            st.append(i)
            answer.append(min(st))
    return answer