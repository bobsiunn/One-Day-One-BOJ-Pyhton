#코드 실행시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline
#포도주 잔의 갯수 input
n = int(input())
#각 포도주 잔의 양으로 구성된 리스트
grape = [int(input()) for _ in range(n)]
#i번째 포도주 잔까지 있다고 할때, 마실 수 있는 최대 포도주의 양을 저장하는 DP 선언
dp = [0 for _ in range(n)]


for i in range(n):
    #i가 0일때는 한잔뿐이므로 grape를 그대로 받아옴
    if(i == 0):
        dp[i] = grape[0]
    #i가 1일때는 2잔이므로 두 잔을 모두 마심
    elif(i == 1):
        dp[i] = grape[0] + grape[1]
    #i가 2일때는 3잔이므로, 12잔, 13잔, 23잔 중 가장 많은 양의 포도주 마심
    elif(i == 2):
        dp[i] = max(grape[0]+grape[2], grape[1]+grape[2], grape[0] + grape[1])
    #i잔일때, 바로 위 코드를 dp를 활용해 일반화
    else:
        dp[i] = max(dp[i-2]+grape[i], dp[i-3]+grape[i-1]+grape[i],dp[i-1])
#가장 뒤에 있는 dp 출력
print(dp[n-1])

#인사이트
#dp를 사용해 일반화할 수 있는 코드를 작성하자
#유사한 유형의 문제와 다른 조건 등을 찾을 수 있다면 반례는 거기에 존재할 것

