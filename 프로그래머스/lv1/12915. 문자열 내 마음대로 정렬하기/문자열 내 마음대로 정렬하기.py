def solution(strings, n):
    
    st = [list(i) for i in strings]
    print(st)
    
    st.sort(key=lambda x:(x[n],x))
    print(st)
    
    strings.sort(key=lambda x:(x[n],x))
    
    answer = [''.join(i) for i in st]
    return strings