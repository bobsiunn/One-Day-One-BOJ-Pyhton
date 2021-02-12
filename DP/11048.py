import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for i in range(m)] for j in range(n)]

dp[0][0] = maze[0][0]

for i in range(n):
    if(i == 0):
        for j in range(1,m):
            dp[i][j] = dp[i][j-1] + maze[i][j]
            #print(dp)

    else:
        for j in range(m):
            if(j == 0):
                dp[i][j] = dp[i-1][j] + maze[i][j]

            else:
                temp = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                dp[i][j] = temp + maze[i][j]
    #print(dp)

print(dp[n-1][m-1])