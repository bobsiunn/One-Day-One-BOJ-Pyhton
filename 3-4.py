def solution(s1, s2):
	answer = 0
	dp = []
	for i in range(len(s1)):
		if(s1[:i] == s2[-i:]):
			dp.append(s2+s1[i:])
			#print(dp)
			
	for j in range(len(s2)):
		if(s2[:j] == s1[-j:]):
			dp.append(s1+s2[j:])
			#print(dp)
	dp.sort()
	answer = len(dp[0])
			
	return answer

s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")