# 2016년 1월 1일은 금요일
# 윤달은 2월이 29일까지 있다

# 접근방법 1. 자료형으로 만들기
# 접근방법 2. 1월 1일부터 시작하는 날짜 배열을 만들고 홀수달 짝수달 윤달에 따른 총 날짜를 구하고 날짜 배열의 인덱스를 정해줌

# 1. 자료형으로 만들어 풀기
def solution(a,b):
    # 해당 달의 날짜
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]

# def solution(a, b):
#     answer = ''
#     dic = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
#     if a > 1:
#         for i in range(1, a):
#             if i < 8:
#                 if i % 2 == 1:
#                     b += 31
#                 elif i == 2:
#                     b += 29
#                 else:
#                     b += 30
#             if i > 7:
#                 if i % 2 == 0:
#                     b += 31
#                 else:
#                     b += 30
#     answer = dic[(b % 7) - 1]    
#     return answer

