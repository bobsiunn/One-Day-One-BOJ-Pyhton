def solution(bishops):
	answer = 0
	dp = []
	chase = [[0 for _ in range(9)] for _ in range(9)]
	for i in range(9):
		chase[0][i] = -1
		chase[i][0] = -1
	
	for i in bishops:
		x = ord(i[0]) - 64
		y = int(i[1])
		
		dx = [0,-1,-1,1,1]
		dy = [0,1,-1,1,-1]
		
		for i in range(1,9):
			for j in range(5):
				nx = x + (dx[j]*i)
				ny = y + (dy[j]*i)
				if(1 <= nx < 9 and 1<= ny < 9):
					if([nx,ny] not in dp):
						dp.append([nx,ny])
				

		answer = 64 - len(dp)
		
	return answer

bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")