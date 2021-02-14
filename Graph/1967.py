#코드 실행 시간 단축을 위한 sys 모듈 import
import sys
#bfs 탐색을 위해 deque 모듈 import
from collections import deque
input = sys.stdin.readline
#노드의 개수 입력
n = int(input())
#시작 노드, 끝노드, 가중치를 저장하는 트리
tree = [[] for _ in range(n+1)]
#n-1번 동안
for i in range(n-1):
    #시작 노드, 끝 노드, 가중치를 입력받고
    root, node, rate = map(int, input().split())
    #시작노드의 인덱스에 (끝 노드, 가중치)를 저장
    tree[root].append((node,rate))
    #끝노드의 인덱스에 (시작 노드, 가중치)를 저장
    tree[node].append((root,rate))
#첫번째 방문기록(각 노드까지 도달했을 때 가중치의 합을 저장)
visit1 = [-1 for _ in range(n+1)]
#두번째 방문기록(첫번째 방문기록 중 가장 큰 가중치를 가지는 위치를 중심으로 각 노드에 도달했을 때 가중치의 합의 저장)
visit2 = [-1 for _ in range(n+1)]
#bfs 함수 선언
def bfs(start, visit):
    #탐색 시작점은 가중치가 0이므로 0으로 저장
    #탐색 시작점이 0이기 때문에 visit1,2를 -1로 초기화하지 않으면,
    #탐색 시작점을 아직 탐색이 이루어지지 않은 점으로 판단해 오류가 발생할 수 있음
    visit[start] = 0
    #탐색 필요 노드들을 저장하는 리스트를 선언하고, 해당 리스트를 deque로 덮어 popleft() 사용 가능
    queue = deque([start])
    #더이상 탐색이 필요가 노드가 남아 있지 않을 때까지
    while queue:
        #가장 먼저 저장된 노드를 꺼냄
        temp = queue.popleft()
        #해당 노드와 연결된 모든 노드와 간선의 가중치에 대해
        for node, w in tree[temp]:
            #연결된 노드가 방문된 적이 없을 경우
            if(visit[node] == -1):
                #연결된 노드의 방문기록에 해당 노드 가중치 + 간선의 가중치를 저장
                visit[node] = visit[temp] + w
                #연결된 노드를 탐색 필요 노드에 추가
                queue.append(node)
#1을 탐색 시작점으로 하는 bfs 호출
bfs(1,visit1)
#bfs 호출 결과 생성된 각 노드 도달 필요 가중치 중 가장 큰 값(가장 멀리 있는)의 인덱스를 새로운 bfs 탐색의 시작점으로 저장
new_start = visit1.index(max(visit1))
#새로운 탐색 시작점에서 bfs 함수 다시 호출
bfs(new_start,visit2)
#bfs 호출 결과 각 노드 도달 필요 가중치 중 가장 큰 값(가장 멀리 있는)을 출력
print(max(visit2))

#인사이트
#모든 문제를 단 한번의 탐색만으로 해결해야 하는 것은 아님
#문제에서 요구하는 목표가 어떤 방식으로 구성되는지 고민하자(가장 긴 노드-노드 연결선 = 가장 멀리 있는 노드 - 가장 멀리 있는 노드 연결선)
#방문기록 저장을 위해 not in을 쓰지 않고, 인덱스를 사용하는 경우에는 초기화 값의 설정에 유의하자
#재귀함수로 풀이하는 것도 가능하나, 역시 트리의 사이즈가 커지면 최대 재귀 깊이를 넘기므로 while-queue로 대체(pythonic 코드를 작성하자)