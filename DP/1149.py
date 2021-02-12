#코드 실행시간 단축을 위한 sys 모듈 import
import sys
input = sys.stdin.readline

#주어진 집의 숫자
n = int(input())
#각 집마다 RGB로 색칠하는데 드는 비용으로 이중 리스트 생성
house = [list(map(int, input().split())) for _ in range(n)]
#해당 집을 각각 R, G, B로 색칠할때 드는 비용의 최솟값을 저장하는 DP 리스트
dp = [[0,0,0] for i in range(n)]

#1번째 줄의 경우 RGB 색칠 비용과 그 값이 같음
dp[0] = house[0]

#2번째 줄부터 n번째 줄까지 반복
for i in range(1,n):
    #i번째 줄 집을 R 색칠 최소 비용은 i-1번째 줄 집을 G,B로 색칠하는 비용 중 작은 값
    dp[i][0] = min(dp[i-1][1] + house[i][0], dp[i-1][2] + house[i][0])
    #i번째 줄 집을 G 색칠 최소 비용은 i-1번째 줄 집을 R,B로 색칠하는 비용 중 작은 값
    dp[i][1] = min(dp[i-1][0] + house[i][1], dp[i-1][2] + house[i][1])
    #i번째 줄 집을 B 색칠 최소 비용은 i-1번째 줄 집을 R,G로 색칠하는 비용 중 작은 값
    dp[i][2] = min(dp[i-1][0] + house[i][2], dp[i-1][1] + house[i][2])

#n번째 줄 집을 R,G,B로 색칠할때 드는 비용의 최솟값 중 가장 작은 값 출력
print(min(dp[n-1]))

#인사이트
# DP 무조건 해당 줄의 최적해를 보관하려 하기보단 모든 경우의 수를 저장한 후
# 목표 줄까지 왔을 때 해당 줄에서 최적해를 찾을 것
# 어느 정도는 뇌빼기하고 풀어보는 것도 좋을 듯
