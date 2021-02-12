#코드 실행 시간 단축을 위한 sys 모듈 import
import sys
#bfs 탐색 시 pop(0)보다 popleft()를 사용해 코드 실행시간 단축을 위한 deque import
from collections import deque
#sys모듈의 편하게 쓰기 위해 input 재정의
input = sys.stdin.readline
#그래프의 세로 길이 n과 가로 길이 m을 입력
n,m = map(int, input().split())
#미로를 입력받음
maze = [list(map(int, input().strip())) for _ in range(n)]
#상하좌우 탐색을 위한 x,y축 좌표 세팅
dx = [-1,1,0,0]
dy = [0,0,1,-1]
#bfs 탐색 함수 선언
def bfs(x,y):
    #세로 길이, 가로 길이를 함수 내에서 사용하기 위해 전역 변수 선언
    global n,m
    #탐색할 위치를 저장하는 큐 선언(deque) 이후 시작 root 노드를 담기
    queue = deque([[y,x]])
    #더이상 탐색할 위치가 없을 때까지
    while queue:   
        #큐에 가장 먼저 저장된 위치를 가져옴
        a = queue.popleft()
        #해당 위치의 y좌표 가져옴
        y = a[0]
        #해당 위치의 x좌표 가져옴
        x = a[1]
        #상하좌우로 탐색
        for i in range(4):
            #기존 y좌표 + (상하)를 새로운 y좌표로 저장
            ny = y + dy[i]
            #기존 x좌표 + (좌우)를 새로운 x좌표로 저장
            nx = x + dx[i]
            #새로운 좌표가 그래프 범위 안에 있을 때
            if(0 <= ny < n and 0<= nx < m):
                #새로운 좌표에 아직 탐색이 이루어지지 않은 위치가 있을 때
                if(maze[ny][nx] == 1):
                    #새로운 좌표에 root 노드에 저장된 수에 1을 더함
                    #저장된 수 = 해당 좌표에 도달하기 위해 필요한 이동의 횟수
                    maze[ny][nx] = maze[y][x] + 1
                    #큐에 새로운 좌표를 저장
                    queue.append([ny,nx])
#그래프 시작점을 root 노드로 bfs 탐색 함수 호출
bfs(0,0)
#미로의 마지막 위치(도착점)에 저장된 필요 이동의 횟수를 출력
print(maze[-1][-1])

#인사이트
#메모리 관리와 시간 관리의 중요성
#방문기록(visit), 이동 횟수 저장(DP)를 응용하여 코드를 짰고 정답이었으나
#메모리 초과로 인해, 방문기록을 사용하지 않고 구현해야 했다
#dfs,bfs 탐색을 한다고 해서 언제나 ideal한 프로세스가 이루어져야 하는 것은 아니다
#필요한 조건만 충족한다면, 기존 형식에서 벗어난 코드도 충분히 사용가능