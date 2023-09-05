from collections import deque
def solution(maps):
    
    dx = [0, 1, 0 ,-1]
    dy = [-1, 0, 1, 0]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵 길이 안에서만 이동할 경우
                if nx >= 0 and nx < len(maps) and ny >= 0 and ny < len(maps[0]):
                    # 이동한 지점이 벽이 아닐 경우
                    if maps[nx][ny] == 1:
                        # 이동할 지점에 + 1을 해줌 -> 마지막에 최종 도착한 지점이 최단거리가 됨
                        maps[nx][ny] = maps[x][y] + 1 
                        q.append((nx, ny))
                    
        if maps[-1][-1] == 1:
            return -1
        else:
            return maps[-1][-1]
        
    return bfs(0, 0) # 초기 시작점 0,0으로 지정 후 시작