#코드 실행시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#수열의 시작 숫자 a와 각 자리수를 반복해서 곱하는 p 입력
a,p = map(int, input().split())
#그래프를 입력받는 리스트
graph = []
#각 실행 이후의 숫자를 저장하는 변수 선언 후, 시작 숫자 a를 배정
temp = a
#무한 반복
while True:
    #새로운 숫자가 그래프에서 이미 탐색된 숫자일때,
    #직관적으로 이해는 가지 않지만, 문제 설명에 따르면, 이 경우 반복수열이 됨
    if(temp in graph):
        #해당 숫자가 있는 인데수의 위치를 반환
        index = graph.index(temp)
        #반복 종료
        break
    #새로운 숫자가 이전에 탐색된 적이 없을때
    else:
        #그래프에 새로운 숫자를 추가
        graph.append(temp)
        #각 자리수에 p제곱한 수를 저장하기 위한 리스트
        sum_list = []
        #정수를 문자열처럼 다루기 위해 str 변환
        word_temp = str(temp)
        #각 자리수 모든 숫자에 대해
        for i in word_temp:
            #sum_list에 각 자리수에 p제곱한 수를 저장
            sum_list.append(int(i)**p)
        #새로운 숫자에 sum_list의 숫자의 모든 합을 저장
        temp = sum(sum_list)

#반복 수열이 시작되는 인덱스는 곧, 반복되지 않는 수열들의 개수와 같다
# = 리스트는 0부터 카운팅하기 때문
#반복 수열이 시작되는 인덱스(반복x 수열의 개수)를 출력
print(index)

#인사이트
#단순히 수열로써 인식하기 보다는, 반복 수열 그 자체를
#dfs 탐색 시 쭉 탐색되다가 어느 시점부터 순열 사이클이 되는 사과 나무에 매달린 사과 모양의 그래프라고 인식
#dfs 함수로 구현해도 되지만, 굳이 복잡한 함수를 짜기보다 직관적으로 접근(재귀함수로 구현 가능)