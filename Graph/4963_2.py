#코드 실행시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#상하좌우 대각선 모두 탐색해야 하기 때문에 시계반대 방향으로 360도 좌표 세팅
dx = [-1,1,-1,-1,1,1,0,0]
dy = [0,0,1,-1,1,-1,1,-1]
#dfs 탐색을 위한 함수 선언
def dfs(matrix, y, x, y_len, x_len):
    #해당 노드의 방문기록을 1로 저장 (방문함)
    visit[y][x] = 1
    #반시계 방향 360도 탐색
    for i in range(8):
        #탐색할 새로운 노드의 y좌표
        ny = y + dy[i]
        #탐색할 새로운 노드의 x좌표
        nx = x + dx[i]
        #탐색할 새로운 노드의 좌표가 그래프 범위 내 있을 때
        if(0 <= ny < y_len and 0 <= nx < x_len):
            #해당 노드가 방문된 적이 없고, 섬이 해당 좌표에 존재할 때
            if(visit[ny][nx] == 0 and matrix[ny][nx] == 1):
                #해당 노드를 중심으로 dfs 함수 재귀 호출
                dfs(matrix, ny, nx, y_len, x_len)


#무한 반복                
while True:
    #그래프의 길이(w)와 높이(h)를 입력
    w,h = map(int, input().split())
    #(0,0)을 입력 시
    if(w == 0 and h == 0):
        #반복 종료
        break
    #(0,0)이 아닌 길이와 높이를 입력했을 때
    else:
        #해당 그래프 상 섬의 위치를 기록하는 2차원 리스트 생성
        graph = [list(map(int, input().split())) for _ in range(h)]
        #각 좌표에 대한 방문기록을 저장하는 2차원 리스트 생성
        visit = [[0]*w for _ in range(h)]
        #섬의 개수를 세기 위한 변수
        cnt = 0
        #각 높이에 대해 순차적으로 탐색
        for i in range(h):
            #각 길이에 대해 순차적으로 탐색
            for j in range(w):
                #해당 좌표가 방문된 적이 없고, 섬이 존재할 경우
                if(visit[i][j] == 0 and graph[i][j] == 1):
                    #해당 좌표를 노드로 하는 dfs 탐색 호출
                    dfs(graph, i, j, h, w)
                    #섬의 개수를 하나 더함
                    cnt += 1
        #해당 그래프 상에 존재하는 섬의 개수를 출력
        print(cnt)