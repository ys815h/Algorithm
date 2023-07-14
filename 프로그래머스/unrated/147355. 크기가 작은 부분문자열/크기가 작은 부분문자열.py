# 문자열 t에서 p의 길이와 같이 문자열을 잘름 
# 자른 값 p와 비교 작으면 cnt += 1

def solution(t, p):
    cnt = 0
    
    for i in range(len(t) - len(p) + 1):
        print(t[i])
        st = []
        for j in range(len(p)):
            st.append(t[i + j])
        if ''.join(st) <= p:
            cnt += 1
        
    return cnt