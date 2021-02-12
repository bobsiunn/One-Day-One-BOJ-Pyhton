#파이썬 풀이

import sys
input = sys.stdin.readline

#반복 횟수 입력
t = int(input())

#dp의 값을 1로 초기화
dp = [1 for i in range(10001)]

#입력받는 숫자 리스트
lst = []

for i in range(t):
    lst.append(int(input()))

# 점핑 점핑의 응용: i-2 인덱스에서 +2 해서 1을 더해줌 (2를 한번 사용)
for i in range(2, 10001):
    dp[i] += dp[i - 2]

# 점핑 점핑의 응용: i-3 인덱스에서 +3 해서 1을 더해줌 (3을 한번 사용)    
for i in range(3, 10001):
    dp[i] += dp[i - 3]
    
#입력받은 숫자의 위치에 있는 dp 출력    
for i in lst:
    print(dp[i])

