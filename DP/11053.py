#실행시간 단축을 위한 sys 모듈 도입
import sys
input = sys.stdin.readline

#수열 길이 입력
n = int(input())

#수열을 입력받음
array = list(map(int, input().split()))

#인덱스를 사용하기 위해 리스트에 0을 미리 할당
dp = [0]*n

#array 수열을 처음부터 끝까지 탐색
for i in range(n):
    #array 수열을 처음부터 i까지 탐색
    for j in range(i):
        #array에서 지정된 위치의 수보다 그 j 인덱스의 수가 작고, j 인덱스에 기록된 dp의 값이 더 클때
        if(array[j] < array[i] and dp[j] > dp[i]):
            #j인덱스의 수를 i dp 값으로 받아옴
            dp[i] = dp[j]
    #그 자체로 이미 길이가 1이기 때문에 1을 더해줌
    dp[i] += 1


print(max(dp))

# 메인 인사이트: 
# dp는 각 인덱스 위치를 최장 수열의 마지막 위치로 했을 때의 길이를 저장
# 이전 인덱스의 값에 이어 현 인덱스 값이 증가하는 경우, 이전 인덱스에 기억된 값을 받아옴
# 정방향 연산이 아니라 역방향 연산을 신경 썼어야 함