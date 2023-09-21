# 2477 참외밭 (실버2)

# 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돎
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4

# 1.접근방법
# 0~5까지 변수를 통해 무한반복으로 돌리는  while문 하나 생성(가장 큰 너비를 찾을 때 까지)
# ex) 탈출 할때 변수가 x 일 경우
# 찾으면 탈출 후 해당 너비에서 뺄 빈 공간을 (x+2) % 6 에 해당하는 변 길이와 (x+3) % 6에 해당하는 변 길이 빼주면 해결됨

import sys
input = sys.stdin.readline

K = int(input().strip())
graph = []
for _ in range(6):
    graph.append(list(map(int, input().strip().split())))
side = 0
area = 0
for i in range(6):
    
    if graph[i][1] * graph[i-1][1] > area:
        side = i
        area = graph[i][1] * graph[i-1][1]

a = (side + 2) % 6
b = (side + 3) % 6
print((area - graph[a][1] * graph[b][1]) * K)