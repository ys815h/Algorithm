# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
# 전체 학생의 수 n, (전체 학생의 수는 2명 이상 30명 이하)
# 도난당한 학생들의 번호가 담긴 배열 lost, (1명 이상 n명 이하이고 중복되는 번호는 없습니다.)
# 여벌의 체육복 가져온 학생들의 배열 reserve (중복되는 번호는 없습니다.)
# (여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다)
# (이때 이 학생은 다른 학생에게는 체육복을 빌려줄 수 없습니다.)
# 체육수업을 들을 수 있는 학생의 최댓값을 return

def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    st = reserve.copy()
    for i in reserve:
        if i in lost:
            lost.pop(lost.index(i))
            st.pop(st.index(i))
                
    for i in st:
        for j in lost:
            if i + 1 == j or i - 1 == j:
                lost.pop(lost.index(j))
                break
                
    answer = n - len(lost)
    return answer