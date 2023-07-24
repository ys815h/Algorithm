def solution(strings, n):
    
    st = [list(i) for i in strings]
    
    st.sort(key=lambda x:(x[n],x))

    
    answer = [''.join(i) for i in st]
    return answer