n = int(input())

s = []
dp = []

for i in range(n):
    s.append(int(input()))

for i in range(n):
    if(i == 0):
        dp.append(s[0])
    elif(i == 1):
        dp.append(s[0] + s[1])
    elif(i == 2):
        dp.append(max(s[0]+s[2], s[1]+s[2]))
    else:
        dp.append(max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i]))

#print(dp)
print(dp[n-1])