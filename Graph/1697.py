#앞뒤 출구가 있어 stack,queue를 유연하게 사용할 수 있는 deaue import
from collections import deque 
#bfs 탐색을 위한 함수 정의
def bfs(): 
    #탐색해야할 위치를 저장하는 큐 선언
    q = deque()
    #해당 큐에 탐색 시작 위치인 N을 저장 
    q.append(N) 
    #더이상 탐색해야할 위치가 없을 때까지 반복
    #if조건에 의해 조기 종료되지 않고, q = empty로 종료시, 탐색 대상이 존재x
    while q:
        #popleft로 가장 앞에 저장된(가장 먼저 저장된) 위치를 불러옴
        v = q.popleft()
        #불러온 위치가 탐색 대상일때
        if v == K:
            #visited의 해당 인덱스에 저장된 것은 해당 노드에 도달하기 위해 필요한 최단 이동 횟수
            print(visited[v])
            #함수 종료
            return
        #다음 노드 후보군에 대해(각각 뒤로 걷기, 앞으로 걷기, 순간이동을 의미)
        for next_node in (v-1, v+1, v*2):
            #다음 노드가 유효값의 범위 안에 있고
            #다음 노드가 이전에 탐색된 적이 없을 때
            if(0 <= next_node < MAX and visited[next_node] == 0):
                #다음 노드의 방문기록에 이전 노드의 방문기록 +1 (이전노드 -> 다음노드로 이동을 의미)
                visited[next_node] = visited[v] + 1
                #큐에 다음 노드의 새끼 노드들을 등록
                q.append(next_node)
#유효값의 최대범위를 저장하는 MAX 변수    
MAX = 100001              
#수빈과 동생의 위치를 입력받기
N, K = map(int, input().split())
#각 노드들에 도달하기 위한 최단 이동 횟수를 저장하는 list(방문기록) 
visited = [0]*MAX 
#해당 함수 호출
bfs()

#인사이트
#BFS는 탐색과정에서 한번에 목표로 직진하는 것이 아니라
#노드의 레벨을 다운그레이드 하면서 목표 노드에 도달할 때까지 모든 노드를 탐색하고
#이 과정에서 해당 노드에 도달하기 위한 경로, 혹은 필수 이동횟수를 기록
#최종적으로 목표 노드에 도달했을 때, 목표 노드의 인덱스에 저장된 방문기록을 호출
