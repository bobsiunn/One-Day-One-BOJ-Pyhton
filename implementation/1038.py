import sys
from collections import deque

input = sys.stdin.readline
N = int(input())


q = deque([i for i in range(10)])
res = []


while q:
    x = q.popleft()
    res.append(x)

    lastNum = x % 10

    for num in range(lastNum):
        q.append(x * 10 + num)

res.sort()

if(N >= len(res)):
    print(-1)
else:
    print(res[N])


#반성문

#직관적인 풀이를 먼저 시도해볼 것
#메모리가 넉넉하게 주어졌기 때문에 정렬을 시도해도 됐음
#가능한 감소 경우의 수를 모두 생성하고 정렬하면 된다.

