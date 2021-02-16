#코드 실행 시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#상근이가 가진 카드의 수
n = int(input())
#상근이가 가진 카드들의 목록
n_card = list(map(int, input().split()))
#주어진 카드들의 수
m = int(input())
#주어진 카드들의 목록
m_card = list(map(int, input().split()))
#상근이가 가진 카드 각각의 개수를 저장하는 딕셔너리
result = {}
#주어진 카드 각각에 대해 상근이가 가지고 있는 카드의 수를 저장하는 리스트
result_list = []
#상근이가 가진 모든 카드에 대해
for i in n_card:
    #우선적으로 시도
    try:
        #해당 카드가 key인 value에 1을 더함
        result[i] += 1
    #우선 시도 실패 시(해당 카드가 탐색된 적이 없을 때)
    except:
        #해당 카드를 key로 하는 요소 생성 후 1을 value로 저장
        result[i] = 1
#주어진 모든 카드에 대해
for i in m_card:
    #해당 카드를 상근이가 1개 이상 가지고 있을 때
    try:
        #해당 카드를 상근이가 가지고 있는 개수를 리스트에 저장
        result_list.append(result[i])
    #해당 카드를 상근이가 1개도 가지고 있지 않을 때
    except:
        #리스트에 0개를 저장
        result_list.append(0)
#각 카드에 대해 상근이가 가지고 있는 카드의 개수를 출력
print(*result_list)

#인사이트
#이분탐색이 순차탐색 등보다 효율적일 때는 두 가지 조건이 필요하다
#탐색의 대상이 하나일때 & 요소들에 대해 정렬이 가능할 때
#순차 탐색이 어렵다면 딕셔너리 등 자료구조를 사용하는 것도 검토해봐야 한다
#문제 유형을 그대로 따라가려 하지 말고 더 효율적인 방법을 고민하자