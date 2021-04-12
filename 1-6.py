def solution(pos):
	answer = 0
	x = ord(pos[0]) - 64
	y = int(pos[1])
	
	dx = [-2,-2,-1,-1,1,1,2,2]
	dy = [-1,1,-2,2,-2,2,-1,1]
	
	for i in range(8):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if(1 <= nx <= 8 and 1<= ny <= 8):
			answer += 1
			
	return answer

pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")