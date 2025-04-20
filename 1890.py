import sys
input = sys.stdin.readline


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
way = [[0]*N for _ in range(N)]

# for row in range(N):
#   print(board[row])

# for row in range(N):
#   print(way[row])


#규칙
#각 칸에서 적힌 숫자만큼 오른쪽, 아래쪽으로 이동할 수 있음
#이동하는 중에 0이 있으면 그 경로로는 이동 불가함
#N-1, N-1 위치에 도달하면 종료

#구현
#way의 각 위치에 해당 위치까지 도달할 수 있는 경우의 수를 기록
#현재 위치에서 오른쪽 or 아래쪽 이동이 범위상 가능한지, 0은 없는지 체크(경로 유효 확인)
#유효한 경로인 경우 현재 위치의 경로 수 + 1을 점프할 위치에 기록함
#완전탐색 종료 이후 N-1, N-1 위치의 경로수 출력


way[0][0] = 1 #일단 시작점은 1로 설정

for x in range(N):
  for y in range(N):
    if(board[x][y] == 0): continue #제자리 점프 방지

    # cnt = way[x][y]
    jumpPower = board[x][y]

    # if(cnt == 0): continue #도달할 수 없는 경로

    nextX = x + jumpPower
    nextY = y + jumpPower

    if(nextX < N):
      way[nextX][y] += way[x][y]
    if(nextY < N):
      way[x][nextY] += way[x][y]

print(way[N-1][N-1])


#교훈
#탐색 문제가 나왔다면 언제나 dp로 풀 수 없는지 확인할 것
#dfs,bfs는 dp에 비해 동일 구간을 자주 탐색하기 때문에 오버헤드가 크다
#