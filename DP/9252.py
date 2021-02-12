#첫번째 문자열 입력
l1 = input()
#두번째 문자열 입력
l2 = input()

#첫번째 문자열의 길이
len1 = len(l1)
#두번째 문자열의 길이
len2 = len(l2)

#dp = 해당 지점까지의 가장 긴 공통 부분 수열의 길이를 저장
#단, i,j가 각각 0일때 dp의 값을 0으로 미리 채움 (인덱스 에러 방지용)
dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
new = [['' for _ in range(len2+1)] for _ in range(len1+1)]

#i(l1의 각 문자)를 중심으로
for i in range(1,len1+1):

    #j(l2 각 문자)에 대해 탐색
    for j in range(1,len2+1):

        #ㅣ1의 문자와 l2의 문자가 같을 때
        if(l1[i-1] == l2[j-1]):
            #dp[i-1][j] = l1의 직전 문자, l2의 해당 인덱스까지 최고 수열
            #dp[i][j-1] = l1의 해당 문자, l2의 인덱스 직전까지 최고 수열
            #dp[i-1][j-1]+1 = l1의 직전 문자, l2의 인덱스 직전까지 최고 수열에 길이를 더함
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            new[i][j] = new[i-1][j-1] + l1[i-1]

        else:
            #dp[i-1][j-1] = l1의 직전 문자, l2의 직전 인덱스까지 최고 수열
            #dp[i][j-1] = l1의 해당 문자, l2의 직전 인덱스까지 최고 수열
            #dp[i-1][j] = l1의 직전 문자, l2의 해당 인덱스까지 최고 수열
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

            if(dp[i][j-1] >= dp[i-1][j]):
                new[i][j] = new[i][j-1]
            else:
                new[i][j] = new[i-1][j]


#세번째 문자열 입력
#l3 = input()
print(dp[-1][-1])
print(new[-1][-1])
