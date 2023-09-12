def solution(numbers):
    answer = []
    visit = [0] * len(numbers)
    st = []
    # numbers.sort()
    def dfs(v):
        if len(st) == 2:
            # st의 합이 정답 배열에 없다면 추가 함
            if sum(st) not in answer:
                answer.append(sum(st))
            return
        temp = -1

        for i in range(v, len(numbers)):
            if visit[i] == 0 :
                # 1이 두개 있을 때, 1 + alpha의 중복을 피하기 위함
                if temp != numbers[i]:
                    temp = numbers[i]
                    visit[i] = 1
                    st.append(numbers[i])
                    dfs(i)
                    st.pop()
                    visit[i] = 0
    dfs(0)
    answer.sort()
    return answer