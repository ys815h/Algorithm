def solution(number):
    
    st = []
    cnt = 0
    
    for i in range(len(number)):
        
        st.append(number[i])
        for j in range(i+1 ,len(number)):
            
            st.append(number[j])
            for k in range(j+1, len(number)):
                
                st.append(number[k])
                if sum(st) == 0:
                    cnt += 1
                    st.pop()
                else:
                    st.pop()
                
            st.pop()
        st.pop()
            
    return cnt