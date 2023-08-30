def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        st = []
        for j in range(commands[i][0]-1, commands[i][1]):
            st.append(array[j])
        st.sort()
        answer.append(st[commands[i][2]-1])
    return answer