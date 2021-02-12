#코드 실행시간 단축을 위한 sys모듈 import
import sys
input = sys.stdin.readline
#센서의 개수
n = int(input())
#집중국의 개수
k = int(input())
#센서의 좌표 입력받기
sensor = list(map(int, input().split()))
#센서의 좌표를 오름차순으로 정렬
sensor.sort()
#각 센서 간의 거리를 저장하는 리스트 선언
length = []

#집중국의 개수가 센서의 개수보다 많은 경우
#각 센서에 집중국을 하나씩 두면 되므로 거리 총합은 0
if(n <= k):
    print('0')
#집중국의 개수가 센서의 개수보다 적은 경우
#적어도 하나 이상의 집중국은 1개 이상의 센서를 커버해야 함
elif(n > k):
    #센서 사이의 거리를 length 리스트에 추가
    for i in range(n-1):
        length.append(sensor[i+1]-sensor[i])
    #거리를 내림차순으로 정렬
    #가장 거리가 먼 센서-센서 사이가 그루핑의 기준이 되기 때문
    length.sort(reverse=True)
    #k개의 그룹을 만들기 위해서 k-1개의 그루핑 시점을 찾아 제거
    for i in range(k-1):
        length.pop(0)
    #남은 거리들의 합이 총 거리의 합임
    print(sum(length))

#인사이트
#그룹화 문제는 직접 하나하나 요소들을 그룹에 넣기보다
#그룹화가 되는, 필요한 지점들을 찾으면 그 지점을 중심으로 양옆에 2개 그룹이 형성
#문제의 흐름을 똑같이 코드로 구현하려하기보다 더 효과적인 접근법을 생각하기
