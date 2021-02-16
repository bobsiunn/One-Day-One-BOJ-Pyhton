#코드 실행 시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#상근이가 가지고 있는 카드의 개수 입력
n = int(input())
#상근이가 가지고 있는 카드를 입력하고, 오름차순 정렬
n_card = sorted(list(map(int, input().split())))
#카드의 개수 입력
m = int(input())
#각 숫자 가드 입력
m_card = list(map(int, input().split()))
#카드 존재 여부를 확인하고 저장하는 리스트
check_list = []
#상근이가 가진 카드가 숫자 카드에 있는지 확인하는 함수
def find(start, end, target):
    #탐색 시작점이 탐색 끝점보다 뒤일 때까지(탐색 결과 존재하지 않을 때까지)
    while (start <= end):
        #중간값을 시작점과 끝점 사이로 설정
        mid = (start + end)//2
        #해당 숫자 카드가 상근이가 가진 카드 중에 있을 때
        if(target == n_card[mid]):
            #체크리스트에 1을 저장(존재함)
            check_list.append(1)
            #함수 종료
            return
        #중간값보다 해당 숫자 카드가 더 클 때
        if(target > n_card[mid]):
            #새로운 시작점에 중간값 + 1을 저장
            start = mid + 1
        #중간값보다 해당 숫자 카드가 더 작을 때
        elif(target < n_card[mid]):
            #새로운 끝점에 중간값 -1을 저장
            end = mid - 1
    #체크리스트에 0을 저장(존재하지 않음)
    check_list.append(0)
    #함수 종료
    return
#주어진 모든 숫자 카드에 대해
for i in m_card:
    #상근이가 해당 숫자 카드를 가지고 있는지 검사
    find(0,n-1,i)
#체크 리스트의 검사 결과를 출력
print(*check_list)

#인사이트
#이분 탐색은 코드 시간 효율성을 높이기 위해 사용하는 탐색
#재귀를 사용하기보다 while을 사용하는 것이 더욱 범용성이 높음
#이분 탐색을 시작하기 전에는 리스트를 반드시 정렬해두어야 함