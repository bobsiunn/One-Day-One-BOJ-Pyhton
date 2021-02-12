#코드실행시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#컴퓨터의 개수 입력
n = int(input())
#컴퓨터 간의 연결선의 수 입력
k = int(input())
#그래프 선언
graph = {}
#1번 컴퓨터부터 탐색을 시작하므로 root를 1로 설정
root_node = 1
#해당 딕셔너리에 모든 컴퓨터의 번호에 해당하는 key를 생성
for i in range(1,n+1):
    graph[i] = set()
#k번 동안 반복하며 컴퓨터와 컴퓨터 사이의 연결성을 입력
for _ in range(k):
    #key와 value값을 입력받고
    key, value = map(int, input().split())
    #딕셔너리의 key로 접근해 value값을 추가
    graph[key].add(value)
    #상하 관계가 아닌 그래프이므로 딕셔너리의 value에도 접근해 key를 추가
    graph[value].add(key)

#dfs 함수 선언
def DFS_with_adj_list(graph, root):
    #방문한 노드를 순서대로 저장하기 위한 리스트
    visited = []
    #노드의 탐색이 막혔을때, 다시 돌아오기 위한 리스트 선언, 또한 root 노드를 추가
    stack = [root]
    #추가로 탐색해야하는 노드가 하나도 남지 않고 막힘없이 탐색이 이루어졌을때 종료 (stack = empty)
    while stack:
        #stack에 저장된 가장 최신 노드를 꺼냄
        n = stack.pop()
        #꺼낸 노드가 이미 방문하지 않은 노드일때
        if n not in visited:
            #방문 목록에 꺼낸 노드를 추가하고
            visited.append(n)
            #추가로 탐색해야 할 노드에
            #꺼낸 노드와 연결된 노드들 중 이미 방문한 노드를 제외하고 추가함
            stack += graph[n] - set(visited)
    #모든 연결된 노드에 대한 탐색이 끝났을때, 방문목록 반환
    return visited
#원하는 값은 root 노드에게 감염된 컴퓨터의 수 이므로
#전체 방문 목록에서 -1을 한 값을 출력
print(len(DFS_with_adj_list(graph, root_node))-1)