#답은 맞고, DP의 본질에는 더 가깝지만 C/C++로만 가능한 코드(시간초과)

import sys
input = sys.stdin.readline


def finder(n):
    #해당 숫자만큼 리스트 생성
    #이때 [i][0]은 해당 숫자를 1만으로 표현하는 경우
    #[i][1]은 해당 숫자를 표현하는 데 2가 사용되는 경우
    #[i][2]는 해당 숫자를 표현하는 데 3이 사용되는 경우
    dp = [[0,0,0] for i in range(n)]
    
    
    #해당 숫자에 각각 3,2,1을 뺀 만큼 인덱스를 돌아가 값을 가져옴
    #예시: 6 = 3 + dp[3][3이 사용되지 않은 경우의 수들]
    for i in range(0,n):
        if(i == 0):
            dp[0] = [1,0,0]
        elif(i == 1):
            dp[1] = [1,1,0] 
        elif(i == 2):
            dp[2] = [1,1,1]  
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-2][1] + dp[i-2][0]
            dp[i][2] = dp[i-3][2] + dp[i-3][1] + dp[i-3][0]

    #print(dp)
    return sum(dp[n-1][:3])


for i in range(int(input())):
    a = int(input())
    print(finder(a))

