#코드 실행시간 단축을 위한 sys 모듈 import
import sys
#bfs 탐색 시 pop(0) 대신 popleft()를 사용하기 위한 deque 모듈 import
from collections import deque
input = sys.stdin.readline
#상하좌우 탐색을 위한 x,y축 좌표 세팅
dx = [-1,1,0,0]
dy = [0,0,1,-1]
#bfs 탐색 함수 선언
def bfs (matrix, y, x,q):
    #그래프의 가로 길이 n과 세로 길이 m을 함수 내에서 사용하기 위한 전역 변수 호출
    global n,m
    #더이상 탐색할 위치가 남아있지 않을 때까지
    while q:
        #큐에서 가장 먼저 저장된 y,x축 좌표를 가져오고
        y,x = q.popleft()
        #해당 좌표의 방문기록을 1로 저장
        visit[y][x] = 1
        #상화좌우로 4번 반복하며 탐색
        for i in range(4):
            #기존 y축 좌표에 (좌우) 입력으로 새로운 y축 좌표 생성
            ny = y + dy[i]
            #기존 x축 좌표에 (좌우) 입력으로 새로운 x축 좌표 생성
            nx = x + dx[i]
            #새로운 좌표가 그래프의 범위 내에 있을 때
            if(0 <= ny < m and 0 <= nx < n):
                #새로운 좌표가 방문된 적이 없고, 해당 좌표에 토마토가 익지 않았을 때
                if(visit[ny][nx] == 0 and matrix[ny][nx] == 0):
                    #새로운 좌표의 토마토에 기존 좌표(익은 토마토)에 기록된 숫자에 1을 더한다
                    #기존 좌표의 숫자 + 1 = 새로운 좌표는 기존 좌표의 적인 숫자 다음날 익었다
                    matrix[ny][nx] = matrix[y][x] + 1
                    #큐에 새로운 좌표를 탐색 대상으로 추가한다
                    q.append([ny,nx])
#그래프의 가로 길이와 세로 길이를 입력받는다
n,m = map(int, input().split())
#박스 내 익힌 토마토, 안익은 토마토, 빈 칸의 위치를 입력받는다
box = [list(map(int, input().split())) for _ in range(m)]
#박스 내 익힌 토마토가 가득한지를 검사하기 위한 변수 선언
check = 0
#박스의 모든 줄에 대해
for i in box:
    #해당 줄에 안익은 토마토가 있다면
    if(0 in i):
        #검사 변수를 바꿔주고 (안익힌 토마토가 존재)
        check = 1
        #검사를 종료
        break
#검사 결과 모든 토마토가 익었다면
if(check == 0):
    #0을 출력한다
    print('0')
#검사 결과 안익은 토마토가 있다면(check == 1)
else:
    #방문기록을 작성하기 위한 2차원 리스트 선언
    visit = [[0]*n for _ in range(m)]
    #각 토마토가 익는데 걸린 요일 중 가장 큰 값을 저장하기 위한 변수 선언
    cnt = 0
    #탐색의 root 노드가 되는 익힌 토마토를 저장하기 위한 deque 선언
    queue = deque()
    #모든 세로 줄에 대해
    for i in range(m):
        #모든 가로 줄에 대해
        for j in range(n):
            #해당 좌표가 방문기록이 없고, 익힌 토마토가 존재할 경우
            if(visit[i][j] == 0 and box[i][j] == 1):
                #익힌 토마토 목록에 해당 좌표를 저장(탐색의 root 노드)
                queue.append([i,j])
    #해당 박스 내 익힌 토마토의 모든 좌표가 저장된 이후
    #각 좌표를 root 노드로 bfs 탐색 호출
    bfs(box, i, j, queue)
    #모든 박스의 세로줄에 대해
    for i in box:
        #안익은 토마토가 존재한다면
        if(0 in i):
            #토마토가 익는 데 걸리는 요일을 0으로 저장(-1 출력)
            cnt = 0
            #탐색 종료
            break
        #안익은 토마토가 없다면
        else:
            #해당 세로줄에서 익는데 가장 오래 걸리는 토마토의 요일 수를 저장
            temp = max(i)
            #해당 요일 수와 저장된 최대 요일 수 중 더 큰 값을 저장
            cnt = max(cnt,temp)
    #실제 익는데 걸리는 시간은 0일부터 시작하지만
    #익힌 토마토가 1로 기록되어 실제 요일보다 + 1이 되어 있으므로 -1해서 출력
    print(cnt-1)

#인사이트
#기계적으로 dfs를 호출하지 않고, 문제 구조를 분석해 bfs를 선택한 것은 좋았음
#but deque를 사용하지 않아 시간 초과가 발생했고
#모든 root 노드에서 동시에 탐색하는 방법을 고민하지 않고, 각 root 노드에서 따로 bfs 탐색을 호출하는 오류
#각 root 노드에서 따로 탐색 -> 각 경로를 구분하여 인식해야 하는 경우
#모든 root 노드에서 동시 탐색 -> 각 경로 사이의 구분이 필요하지 않은 경우
