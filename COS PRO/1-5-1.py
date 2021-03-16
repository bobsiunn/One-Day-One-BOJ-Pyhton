import math

def solution(n):
	pane = [[0 for j in range(n)] for i in range(n)]
	dy = [0, 1, 0, -1]
	dx = [1, 0, -1, 0]
	ci, cj = 0, 0
	num = 1
	while 0 <= ci < n and 0<= cj < n and pane[ci][cj] == 0:
		for k in range(4):
			if not (0 <= ci < n and 0<= cj < n) or pane[ci][cj] != 0:
				break
			while True:
				pane[ci][cj] = num
				num += 1
				ni = ci + dy[k]
				nj = cj + dx[k]
				if not (0 <= ni < n and 0<= nj < n) or pane[ni][nj] != 0:
					ci += dy[(k + 1) % 4]
					cj += dx[(k + 1) % 4]
					break
				ci = ni
				cj = nj
	ans = 0
	for i in range(n):
		ans += pane[i][i]
	return ans

n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")