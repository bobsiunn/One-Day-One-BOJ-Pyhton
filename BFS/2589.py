#보물섬: 육지 중 최단 거리가 가장 긴 길이
#해석: 육지 내에서 이동 동선 중 가장 


import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())

board = [list(map(str,input().rstrip())) for _ in range(N)]


dx=[1,-1,0,0]
dy=[0,0,1,-1]

treasure = 0

for row in range(N):
    for col in range(M):
        if(board[row][col] == 'L'):
            visited = [[0] * M for _ in range(N)]
            visited[row][col] = 1 #탐색 시작점은 1로 시작함 (0으로 표기된 방문x 지역과 차별화) => 마지막에 -1하기
            q = deque()
            q.append((row, col))
            cnt = 0

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < N and 0 <= ny < M:
                        if board[nx][ny] == 'L' and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1
                            cnt = max(cnt, visited[nx][ny])
                            q.append((nx, ny))

            treasure = max(treasure, cnt)

print(treasure - 1)

#배운점
#dfs는 최단 경로를 찾지 못함 (백트래킹이나, 트리 탐색에 유리함)
#bfs는 최단 경로 및 거리 계산에 유리함
#문제 풀이시, 시간 제한을 바탕으로 어느 정도 수준의 연산량이 허용되는지 
