#min heap을 사용하기 위한 heapq 모듈 import
import heapq
#코드 실행 시간 단축을 위한 sys 모듈 import
import sys
#강의실의 수 n 입력
N = int(input())
#각 강의의 시작시간과 끝시간 입력
course = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
#강의들을 시작시작을 기준으로 정렬
course.sort(key=lambda x: x[0])
#각 강의실에서 사용되고 있는 강의의 끝나는 시간을 저장하는 리스트
room = []
#첫번째 강의실에 가장 먼저 시작하는 강의를 배정(해당 강의가 끝나는 시간을 저장)
heapq.heappush(room,course[0][1])
#2번째 강의부터 마지막 강의까지
for i in range(1,N):
    #강의가 가장 먼저 끝나는 강의실보다 해당 강의의 시작시간이 빠를 때(해당 강의의 시작시간에 모든 강의실이 사용중일 때)
    if room[0] > course[i][0]:
        #해당 강의를 새로운 강의실에 배정
        heapq.heappush(room,course[i][1])
    #강의가 가장 먼저 끝나는 강의실보다 해당 강의의 시작시간이 같거나 늦을 때(해당 강의실에서 해당 강의를 다음 강의로 사용가능할 때)
    else:
        #해당 강의실에 저장된 강의종료시간을 삭제하고
        heapq.heappop(room)
        #해당 강의실에 해당 강의를 배정 (강의종료시간을 업데이트)
        #모든 강의실에 저장된 강의종료시간을 가장 빨리 끝나는 시간을 기준으로 min heap 정렬한다
        heapq.heappush(room,course[i][1])
#사용되고 있는 강의의 수를 저장
print(len(room))

#인사이트
#핵심은 얼마나 적은 탐색으로 강의가 배정되기에 적합한 강의실을 찾을 수 있는가이다
#min heap의 경우, O(nlogn)으로 탐색하기 때문에 적은 탐색으로 강의실을 찾을 수 있다
#pythonic한 코딩은 로직을 코드로 구현하는 것을 넘어 적절한 모듈을 적재적소에 활용하는 것이다