# 2차원 배열 board
# 위에서 부터 뽑아서 bucket에 담음
# 인형이 아무것도 없을 때는 아무일도 일어나지 않음 continue
# bucket에 담을 때 앞뒤로 같은 숫자면 pop 시킴 그리고 answer + 2 최종적으로 사라진 총 수 answer 리턴

# 예시를 통한 예시
# 1번째 줄에는 
# 1 [0,0,0,4,3] 담겨 있고
# 2 [0,0,2,2,5]
# 3 [0,1,5,4,1]
# 4 [0,0,0,4,3]
# 5 [0,3,1,2,1]
# moves에 따라 [1,5,3,5,1,2,1,4]
# bucket엔 [4,(3,(1,1),3),2,4]

def solution(board, moves):
    answer = 0
    bucket = []
    
    for i in moves:
        
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(bucket) > 0:
                    if bucket[-1] == board[j][i-1]:
                        bucket.pop()
                        board[j][i-1] = 0
                        answer += 2
                        break
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                break
    
    return answer