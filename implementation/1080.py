import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())

A = [input().rstrip() for _ in range(N)]
B = [input().rstrip() for _ in range(N)]

# for row in range(N):
#     print(A[row])
# print()
# for row in range(N):
#     print(B[row])

check = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if(A[i][j] == B[i][j]):
            check[i][j] = 1

# print()
# for row in range(N):
#     print(check[row])


cnt = 0

for x in range(N):
    for y in range(M):
        
        if(check[x][y] == 0):
            if(x+2 < N and y+2 < M):
                for i in range(3):
                    for j in range(3):
                        check[x+i][y+j] = 1 - check[x+i][y+j]
                cnt += 1

        # print()
        # print(cnt)
        # for row in range(N):
        #     print(check[row])

flag = True

for x in range(N):
    for y in range(M):
        if(check[x][y] == 0): 
            flag = False
            break

if(flag): print(cnt)
else: print(-1)