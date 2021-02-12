#코드 실행시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#정점의 개수와 간선의 개수 입력
n,m = map(int, input().split())
#각 정점에 해당하는 간선을 입력받기 위한 2차원 리스트 선언
graph = [[] for _ in range(n+1)]
#간선의 개수만큼 반복
for i in range(m):
    #간선의 시작점과 끝점을 입력받고
    u,v = map(int, input().split())
    #그래프의 각 정점 위치에 간선을 저장
    graph[u].append(v)
    graph[v].append(u)
#각 노드에 대한 방문기록 작성을 위한 리스트
visit_list = [0]*(n+1)
#dfs 선언
def dfs(v):
    #dfs는 스택 구조로 돌아가기에 스택을 선언하고, 시작 노드를 추가
    stack = [v]
    #해당 노드의 모든 정점에 대해 탐색이 이루어졌을때
    while stack:
        #가장 최근에 저장된 위치를 불러와 탐색
        n = stack.pop()
        #불러온 위치에 해당하는 모든 간선에 대해
        for i in graph[n]:
            #해당 정점이 방문된 적이 없다면
            if(visit_list[i] == 0):
                #해당 정점을 스택에 저장해 다음 탐색 후보 노드로 등록
                stack.append(i)
                #해당 노드의 방문기록에 1을 저장
                visit_list[i] = 1
#연결 노드의 수를 세는 변수
cnt = 0
#모든 범위 내 노드에 대해
for j in range(1,n+1):
    #방문된 적이 없는 노드가 있다면
    if(visit_list[j] == 0):
        #해당 노드를 root로 dfs 탐색을 실행
        dfs(j)
        #연결 노드의 수를 하나 증가
        cnt += 1
#모든 노드에 대해 탐색이 이루어졌을 때, 변수 출력
print(cnt)

#인사이트
#set을 중심으로 하는 그래프 탐색은 당분간 봉인
#2차원 리스트를 활용해 직관적으로 접근하는 자세가 필요함
#해당 문제처럼, 굳이 각 root 노드로 dfs 탐색 시의 방문기록이 필요하지 않고
#각 노드에 대한 방문 여부만 필요하다면, 과감하게 해당 부분을 제외하는 센스가 필요
#dfs와 bfs 모두 완전탐색에 사용이 가능하지만, 속도 자체는 bfs가 빠름