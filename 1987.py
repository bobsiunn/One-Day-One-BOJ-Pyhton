import sys
from collections import deque
input = sys.stdin.readline


#최대 경로 탐색
#조건: 방문한 적 있는 알파벳은 지나갈 수 없음 (방문한 알파벳을 기록)
#visited에 해당 위치까지 이동했을 때의 최대 알파벳 개수를 기록
#cnt에 최대 알파벳 길이를 기록하고 업데이트



R, C = map(int, input().split())

board = [list(map(str, input().rstrip())) for _ in range(R)]

# for row in range(R):
#     print(board[row])


def dfs(x,y):
    q = []
    q.append((x,y,board[x][y]))
    cnt = 1

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    while q:
        nowX, nowY, nowAlpha = q.pop()
        cnt = max(cnt, len(nowAlpha))
        # print(nowX, nowY, nowAlpha, cnt)

        if(cnt == 26): break

        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            # print(f"search {nextX} {nextY}")

            if(0 <= nextX < R and 0 <= nextY < C):
                if(board[nextX][nextY] not in nowAlpha):
                    nextAlpha = nowAlpha + board[nextX][nextY]
                    q.append((nextX, nextY, nextAlpha))
    
    print(cnt)

dfs(0, 0)


#그래프탐색 + 비트마스킹 문제
#방문한 알파벳들을 어떻게 기록하는지가 중요한 문제(메모리 제한 이슈)
#메모리가 중요한 경우에는 최단 경로 탐색이 아니라면 bfs보다 dfs가 유리하다 (bfs는 큐에 여러 개를 쌓지만, dfs를 즉시 제거를 함)
#비트마스킹을 통해 적은 메모리로 방문기록을 할 수 있다

#
def check_visited(check, before):
    i = ord(check)-ord("A")
    index = 1<<i
    if before | index != before:
        return False  # 방문안했음
    return True

def visit(check, before):
    i = ord(check)-ord("A")
    index = 1<<i
    return before | index
#알파벳 방문 여부는 26(알파벳 개수)개의 비트 마스킹으로 표현 가능함(1은 방문, 0은 방문x)
#i = ord(check)-ord("A") => 현재 알파벳이 몇번째 비트에 해당하는지 판단
#before에 i번째 비트를 or 연산해서 방문 여부 기록함