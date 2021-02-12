#코드 실행시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#dfs 탐색 함수(계속해서 탐색하다가 처음 시작 노드로 돌아오면 함수 종료)
def dfs(graph, v):
    #시작 노드의 방문기록을 1로 변경(방문함)
    visit_list[v] = 1
    #그래프에서 다음 노드를 가져옴 (인덱스의 경우 실제 숫자에 비해 1 작으므로 v-1)
    next_node = graph[v-1]
    #다음 노드가 이전에 방문된 적이 없는 경우
    # =아직 시작 노드로 돌아오지 않은 경우
    if(visit_list[next_node] != 1):
        #다음 노드를 기준으로 재귀함수 호출
        return dfs(graph, next_node)
    #다음 노드가 이전에 방문기록이 있는 경우
    # = 시작 노드로 돌아온 경우
    else:
        #순열 사이클이므로 1을 반환
        return 1

#순열의 개수 입력
t = int(input())
#순열의 개수만큼 반복
for i in range(t):
    #해당 순열의 순열 사이클을 세는 변수
    cnt = 0
    #순열의 길이 입력
    n = int(input())
    #방문기록을 저장하는 리스트 선언
    visit_list = [0]*(n+1)
    #순열을 입력받는 리스트
    graph = list(map(int, input().split()))
    #1부터 순열의 마지막 숫자까지
    for i in range(1,n+1):
        #해당 노드가 방문된 적이 없다면
        if(visit_list[i] == 0):
            #순열 사이클 변수에 해당 노드에 대한 dfs 함수 반환값을 더함
            cnt += dfs(graph, i)
    #해당 순열의 총 순열 사이클의 개수를 출력
    print(cnt)

#인사이트
#순열의 경우, 한 노드는 다른 노드와 1대1로 매칭될 수 밖에 없음
# = dfs 탐색 시 방문 기록이 있는 노드로 돌아오는 것은 사이클 외엔 경우의 수가 없음
#무작정 2차원 리스트나 set을 쓰는 것이 아니라 최소한의 메모리 소모로 솔루션을 찾는 것이 중요
#여러가지 리스트를 동시에 사용할 시 인덱스 관리가 매우 중요 (손그림을 그려볼 것!) 