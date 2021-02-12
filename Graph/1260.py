#실행시간 단축을 위한 sys모듈 import
import sys
input = sys.stdin.readline
#정점의 개수, 간선의 개수, 시작점을 입력
n,m,root = map(int, input().split())
#간선을 저장하기 위한 2차원 리스트 생성(실제 숫자와 맞추기 위해 n+1로 생성)
graph = [[0]*(n+1) for _ in range(n+1)]
#간선의 개수만큼 반복하면서
for j in range(m):
    #간선의 시작점과 종료점을 입력받고
    start,end = map(int, input().split())
    #그래프에 시작점-종료점, 그리고 그 역을 저장한다
    graph[start][end] = 1
    graph[end][start] = 1
#dfs 함수 선언
def dfs(visit, root):
    #방문기록에 탐색 노드를 추가한다
    visit += [root]
    #해당 노드에서 모든 정점들에 대해
    for i in range(len(graph[root])):
        #해당 정점이 방문된 적이 없고, 해당 노드과 간선이 존재할때
        if(graph[root][i] == 1 and (i not in visit)):
            #방문기록을 추가하고, 입력받은 노드에 대해 간선을 탐색하는 재귀함수 호출
            dfs(visit,i)
    #모든 재귀가 끝났을때, 방문기록을 호출
    return visit

#bfs 함수 선언
def bfs(root):
    #방문기록에 시작 노드를 저장
    visit = [root]
    #탐색해야 하는 노드들을 저장하는 queue에 시작 노드 저장
    queue = [root]
    #더이상 탐색해야 할 노드가 없을 때까지 반복
    while queue:
        #탐색해야 하는 노드 목록 중 가장 먼저 저장된 노드를 호출
        n = queue.pop(0)
        #해당 노드에서 모든 정점들에 대해
        for i in range(len(graph[root])):
            #해당 정점이 방문된 적이 없고, 해당 노드와 간선이 존재할때
            if(graph[n][i] == 1 and (i not in visit)):
                #방문기록에 해당 정점을 추가하고
                visit.append(i)
                #탐색해야 하는 노드에 해당 정점을 추가
                queue.append(i)
    #더이상 탐색할 노드가 없을 때, 방문기록 호출
    return visit
#아직 방문이 이루어지지 않았으므로 빈 리스트와 시작 노드를 입력해 함수 호출
print(*dfs([], root))
#재귀호출이 아니므로 시작 노드만을 입력해 함수 호출
print(*bfs(root))

#인사이트
#기계적으로 딕셔너리와 set을 쓰게 되면, 조건이 추가되었을 경우 대응하기 어려움
#bfs와 dfs의 개념을 확실히 알고, 문제에 맞춰 구현하는 근성이 필요
#효율화에 지나치게 집착할 필요가 없다 (과한 그리디 사고는 독)
