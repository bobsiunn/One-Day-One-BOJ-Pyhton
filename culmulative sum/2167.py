import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [[0] * (M+1) for _ in range(N+1)]
cuSum = [[0] * (M+1) for _ in range(N+1)]

for row in range(N):
    line = list(map(int, input().split()))

    for col in range(M):
        mat[row+1][col+1] = line[col]

for row in range(1, N+1):
        for col in range(1, M+1):
            cuSum[row][col] = mat[row][col] + cuSum[row-1][col] + cuSum[row][col-1] - cuSum[row-1][col-1]


K = int(input())

for stage in range(K):
    i, j, x, y = map(int, input().split()) #i,j: 시작 지점 x,y: 끝 지점
    print(cuSum[x][y] - cuSum[x][j-1] - cuSum[i-1][y] + cuSum[i-1][j-1])

#2차원 배열 누적합 문제
#dp를 통해 전체 배열의 누적합을 구함 (매번 구하지 않을 것)
#구역 누적합은 = 넓은 범위 누적합 - 가로&세로 좁은 범위 누적합 + 좁은 범위 누적합




#더 좋은 코드

def answer():
    n, m = map(int, input().split())
    arr = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)] #row,col에 0 채우면서 입력 받기

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
    #arr에 그대로 dp 계산 수행

    for _ in range(int(input())):
        i, j, x, y = map(int, input().split())
        print(arr[x][y] - arr[x][j -  1] - arr[i - 1][y] + arr[i - 1][j - 1])