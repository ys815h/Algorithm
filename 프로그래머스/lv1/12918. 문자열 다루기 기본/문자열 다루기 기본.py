# list로 변환후 len()이 4 OR 6 이면 다음 조건문 실행 아니면 false
# 숫자 or 문자 판별 (islower or isupper로 true면 false를 리턴하고 아니면 true리턴)

def solution(s):
    if s.isdecimal():
        list(s)
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    else:
        return False
