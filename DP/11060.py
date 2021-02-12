n = int(input())
maze = list(map(int, input().split()))

dp = [-1] * n

dp[0] = 0

for i in range(n):
    #print(f'i: {i}')
    for j in range(1,maze[i]+1):
        #print(f'i+j: {i+j}')
        if(i+j >= n):
            break

        elif(dp[i] != -1 and dp[i+j] == -1):
            dp[i+j] = dp[i]+1

        elif(dp[i] != -1 and dp[i+j] != -1):
            dp[i+j] = min(dp[i+j], dp[i]+1)
    #print(dp)

#print(dp)
print(dp[-1])