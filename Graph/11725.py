#코드 실행 시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline

#노드의 개수 입력
n = int(input())
#트리의 간선을 저장하는 2차원 리스트
tree = [[] for _ in range(n+1)]
#각 인덱스의 숫자에 해당하는 root를 저장하기 위한 리스트
root = [0]*(n+1)
#각 노드에 대한 방문 기록을 저장하는 리스트
visit = [0]*(n+1)
#n-1번 동안 반복
for i in range(n-1):
    #간선의 시작점, 끝점을 입력
    u,v = map(int, input().split())
    #트리의 시작점에 끝점을 저장(방향성이 없는 간선)
    tree[u].append(v)
    #트리의 끝점에 시작점을 저장(방향성이 없는 간선)
    tree[v].append(u)

#dfs 탐색 함수
def dfs():
    #탐색해야할 노드들을 저장하는 stack
    stack = [1]
    #더이상 탐색해야할 노드가 남아 있지 않을 때까지
    while stack:
        #가장 최근에 저장된 노드를 꺼냄
        n = stack.pop()
        #해당 노드에 대한 방문기록을 표시
        visit[n] = 1
        #해당 노드에 연결된 모든 노드에 대해
        for i in tree[n]:
            #연결된 노드가 방문된 적이 없다면
            if(visit[i] == 0):
                #연결된 노드의 root를 해당 노드로 저장
                root[i] = n
                #연결된 노드를 탐색 필요 노드 리스트에 추가
                stack.append(i)
#1부터 아래로 내려가며 dfs 탐색
dfs()
#2부터 n까지 root 출력
for i in range(2,n+1): print(root[i])

#인사이트
#문제 독해를 제대로 하고 로직을 짜는 것이 중요
#메모리와 시간의 제한이 촉박할 때는 그래프의 단순화, 방문기록의 단순화가 핵심
#그리고 not in 같은 내장 함수는 편리하지만 실행시간을 많이 잡아먹는 함수이므로 되도록이면 방문기록은 바로 인덱스에 접근할 수 있도록 설정
#bfs와 dfs 중 해당 문제에 유리한 탐색방식을 차용하는 것은 중요