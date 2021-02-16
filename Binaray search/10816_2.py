#코드 실행 시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#상근이가 가진 카드의 수
n = int(input())
#상근이가 가진 카드들의 정렬 목록
n_card = sorted(list(map(int, input().split())))
#주어진 카드들의 수
m = int(input())
#주어진 카드들의 목록
m_card = list(map(int, input().split()))

#이분탐색 함수 선언
def binaray_search(start, end, target, card_list):
    #탐색 시작점이 끝점보다 뒤일때까지(더이상 탐색이 무의미할 때까지)
    while(start <= end):
        #중간점을 시작점 + 끝점을 2로 나눈 몫으로 설정
        mid = (start + end)//2
        #중간점이 탐색 대상과 같을 때
        if(card_list[mid] == target):
            #시작점과 끝점을 범위로 탐색 대상의 수를 세서 반환
            return card_list[start:end+1].count(target)
        #중간점이 탐색 대상보다 작을 때
        elif(card_list[mid] < target):
            #탐색 시작점을 중간점 다음으로 설정
            start = mid + 1
        #중간점이 탐색 대상보다 클 때
        elif(card_list[mid] > target):
            #탐색 끝점을 중간점 이전으로 설정
            end = mid - 1
    #탐색 결과 탐색 대상이 없을 시 0을 반환
    return 0
#탐색 대상의 개수를 저장하는 리스트
result_list = []
#주어진 모든 카드들에 대해
for i in m_card:
    #해당 카드를 상근이가 가지고 있는 개수를 리스트에 저장
    result_list.append(binaray_search(0, n-1, i, n_card))
#리스트를 괄호 없이 출력
print(*result_list)