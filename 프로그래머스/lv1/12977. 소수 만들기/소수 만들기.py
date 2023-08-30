# 재귀함수 조합을 이용하여 temp배열을 만듬
# temp 배열을 만들었을 때 소수 조건 식을 만들어 
def solution(nums):
    answer = 0
    st = []
    start = 0
    cnt = 0
    def dfs(start):
        nonlocal answer
        if len(st) == 3: #여기서 소수 판별
            a = sum(st)
            for i in range(2, int(a**(1/2))+1):
                if a % i == 0:
                    return
            answer += 1
            return
        
        for i in range(start, len(nums)):
            if nums[i] not in st:
                st.append(nums[i])
                dfs(i)
                st.pop()
    dfs(start)
    return answer