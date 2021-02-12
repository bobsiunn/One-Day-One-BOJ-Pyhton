#코드 실행시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#단지의 개수 n 입력
n = int(input())
#아파트의 위치를 입력받기 위한 2차원 리스트 선언, 입력받기
graph = [list(map(int, input().strip())) for i in range(n)]
#방문기록을 저장하기 위한 2차원 리스트 선언
visit = [[0]*n for _ in range(n)]
#x축 방향 탐색(좌우)을 위한 좌표 리스트
dx = [-1,1,0,0]
#y축 방향 탐색(상하)를 위한 좌표 리스트
dy = [0,0,1,-1]
#dfs 탐색 함수 선언 (bfs는 속도가 느린 케이스)
def dfs(x,y,c):
    #해당 좌표에 대해 방문기록을 1로 기록(방문함)
    visit[x][y] = 1
    #전역 변수 nums(단지 내 아파트의 개수)를 가져옴
    global nums
    #만약 해당 좌표에 아파트가 있다면
    if(graph[x][y] == 1):
        #단지 내 아파트의 개수에 1을 더함
        nums += 1
    #그리고 해당 좌표에서 상하좌우로 탐색을 진행
    for i in range(4):
        #현재 좌표 + 좌우 = 새로운 좌표
        nx = x + dx[i]
        #현재 좌표 + 상하 = 새로운 좌표
        ny = y + dy[i]
        #새로운 좌표가 graph의 범위 내에 있고
        if(0 <= nx < n and 0 <= ny < n):
            #새로운 좌표가 방문된 적이 없으며, 아파트가 존재할때
            if(visit[nx][ny] == 0 and graph[nx][ny] == 1):
                #새로운 좌표를 기준으로 dfs 탐색을 재개(재귀호출)
                dfs(nx,ny,c)
#아파트 단지의 번호
cnt = 1
#각 아파트 단지 내 아파트의 개수를 저장하는 리스트
num_list = []
#단지 내 아파트의 개수를 저장하는 변수(단지가 바뀔 때마다 초기화 필요)
nums = 0
#x축 모든 방향으로
for i in range(n):
    #y축 모든 방향으로
    for j in range(n):
        #해당 좌표에 아파트가 존재하고, 방문된 적이 없다면
        if(graph[i][j] == 1 and visit[i][j] == 0):
            #해당 좌표에 대해 dfs 탐색을 실시
            dfs(i,j,cnt)
            #dfs 탐색 결과, 탐색된 단지 내 아파트의 개수를 num_list에 추가
            num_list.append(nums)
            #단지 내 아파트의 개수를 0으로 초기화
            nums = 0

#서로 다른 단지의 개수를 출력(각 단지 내 아파트의 개수를 저장한 리스트의 길이)            
print(len(num_list))
#각 단지 내 아파트의 개수를 저장한 오름차순 리스트에서
for a in sorted(num_list):
    #각 단지 내 아파트의 개수를 출력
    print(a)

#인사이트
#방문기록을 작성해서 이중 for문에서도 불필요한 탐색 횟수를 줄이는 것이 중요
#위아래로 탐색하는 과정에서 미리 좌표의 한계치를 선언해 인덱스 에러 방지
#재귀를 쓰면 무조건 어떤 값을 리턴해야 한다는 편견을 버리기
#dfs 탐색의 구현 뿐만 아니라 문제에서 요구하는 변수를 적재적소에 끼워넣는 센스가 필요