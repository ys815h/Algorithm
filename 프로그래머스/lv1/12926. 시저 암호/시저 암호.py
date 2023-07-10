# 숫자로 바꿔서 계산 하되 z,Z는 그 다음숫자를 a, A로 바꿔주는 로직 필요
# 아스키 코드 변환 ord
# 공백 유무를 어떻게 처리할 것인지에 대한 고민 필요

def solution(s, n):
    array=list(s)
    
    for i in range(len(array)):
        
        
        x = ord(array[i])
        if x <= 122 and x >= 97:
            x += n
            if x > 122:
                array[i] = chr(x - 26)
            else:
                array[i] = chr(x)
            
        if x <= 90 and x >= 65:
            x += n
            if x > 90:
                array[i] = chr(x - 26)
            else:
                array[i] = chr(x)
    answer = ''.join(array)
        
    return answer