def solution(s):
    st = []
    arr = list(s)
    for i in range(len(arr)):
        if st == []:
            if arr[0] == ")":
                return False
                break
            else:
                st.append("(")
        else:
            if st[-1] == "(" and arr[i] == ")":
                st.pop()
            else:
                st.append(arr[i])
    if st == []:
        answer = True
    else:
        answer = False
    return answer