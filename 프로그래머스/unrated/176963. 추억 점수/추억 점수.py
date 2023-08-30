# 그리워하는 사람의 이름을 담은 문자열 배열 name
# 각 사람별 그리움 점수를 담은 정수 배열 yearning
# 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo
# 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return

# 1. key, value값을 이용
# photo의 2차원 배열속에 포함되는 key 값을 전부 더함, 그대로 answer에 append

# 2. 인덱스 번호를 이용
# photo의 2차원 배열의 값이 name안에 있으면 name의 인덱스 값을 구함,
# 동일한 yearning 인덱스의 값들의 합으로 answer에 append

# 자료형 풀이 방식
def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for j in range(len(photo)):
        temp = 0
        for k in range(len(photo[j])):
            if photo[j][k] in name:
                temp += dic[photo[j][k]];
        answer.append(temp)
    return answer

# 자료형을 만들지 않고 인덱스 번호를 이용한 풀이법
# def solution(name, yearning, photo):
#     answer = []
    
#     for j in range(len(photo)):
#         temp = 0
#         for k in range(len(photo[j])):
#             if photo[j][k] in name:
#                 temp += yearning[name.index(photo[j][k])];
#         answer.append(temp)
#     return answer

