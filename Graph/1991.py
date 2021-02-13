#코드 실행 시간 단축을 위한 sys모듈 import
import sys
input = sys.stdin.readline
#트리 노드의 개수 입력
n = int(input())
#트리의 간선을 저장하기 위한 딕셔너리 선언
tree = {}
#트리 노드의 개수만큼
for i in range(n):
    #루트, 왼쪽 노드, 오른쪽 노드를 입력받기
    root, left_node, right_node = input().split()
    #루트에 해당하는 key를 만들고, 해당 value에 미리 0을 넣어 인덱스 생성
    tree[root] = ['0','0']
    #첫번째 인덱스에 왼쪽 노드를 저장
    tree[root][0] = left_node
    #두번째 인덱스에 오른쪽 노드를 저장
    tree[root][1] = right_node

#전위 순회를 저장하는 방문기록
visit_front = []
#전위 순회 함수
def front(node, visit):
    #루트->왼쪽->오른쪽 순회이므로 루트를 먼저 방문기록에 추가
    visit.append(node)
    #왼쪽 노드가 존재할 때
    if(tree[node][0] != '.'):
        #왼쪽 노드를 루트로 하는 탐색 재귀 호출
        front(tree[node][0], visit)
    #오른쪽 노드가 존재할 때
    if(tree[node][1] != '.'):
        #오른쪽 노드를 루트로 하는 탐색 재귀 호출
        front(tree[node][1], visit)

#중위 순회를 저장하는 방문기록
visit_mid = []
#중위 순회 함수
def mid(node, visit):
    #왼쪽 노드가 존재할 때
    if(tree[node][0] != '.'):
        #왼쪽 노드를 루트로 하는 탐색 재귀 호출
        mid(tree[node][0], visit)
    #왼쪽->루트->오른쪽 순회이므로 왼쪽 탐색이 끝난 이후 루트 방문기록 추가
    visit.append(node)
    #오른쪽 노드가 존재할 때
    if(tree[node][1] != '.'):
        #오른쪽 노드를 루트로 하는 탐색 재귀 호출
        mid(tree[node][1], visit)

#후위 순회를 저장하는 방문기록
visit_bot = []
#후위 순회 함수
def bot(node, visit):
    #왼쪽 노드가 존재할 때
    if(tree[node][0] != '.'):
        #왼쪽 노드를 루트로 하는 탐색 재귀 호출
        bot(tree[node][0], visit)
    #오른쪽 노드가 존재할 때
    if(tree[node][1] != '.'):
        #오른쪽 노드를 루트로 하는 탐색 재귀 호출
        bot(tree[node][1], visit)
    #왼쪽->오른쪽->루트 순회이므로 좌우 탐색이 끝난 이후 루트 방문기록 추가
    visit.append(node)
#3가지 탐색 실행
front('A', visit_front)
mid('A', visit_mid)
bot('A', visit_bot)
#탐색 결과 출력
for i in visit_front: print(i, end="")
print()
for i in visit_mid: print(i, end="")
print()
for i in visit_bot: print(i, end="")

#인사이트
#모든 그래프 문제가 bfs, dfs문제는 아님
#DP 문제의 점화식을 짜듯이 해당 그래프를 탐색하는 로직을 규칙으로 작성하고
#그에 맞는 탐색 함수를 짜는 것이 중요
#재귀는 분명 그래프의 크기가 커질 경우, 시간초과를 유발하기 쉽지만
#재귀로 풀었을때 1991번 문제처럼 훨씬 효율적인 경우도 존재
