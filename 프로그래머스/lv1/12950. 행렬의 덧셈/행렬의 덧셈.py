# 이중 배열 풀이법은 for문을 돌려 

def solution(arr1, arr2):
    
    ans = []
    
    for i in range(len(arr1)):
        ans.append([])
        for j in range(len(arr1[i])):
            ans[i].append(arr1[i][j] + arr2[i][j])
    return ans