import sys
input = sys.stdin.readline

MAX_E = (1024 * 64) + 1
prefix = [0] * MAX_E #현재 K 기준으로 1~K까지의 누적합을 저장

def solve(x, y):
    global prefix
    x += 1
    res = 1
    k = 1
    dist = y - x

    while dist > 0:
        if (prefix[k + 1] == 0): prefix[k + 1] = prefix[k] + (k + 1) #누적합 업데이트

        if x + prefix[k + 1] <= y: #현재 x에서 K+1을 하고, 그 이후로 K를 1까지 줄여도 y에 도달할 수 있을 경우 k+1
            k += 1
        elif x + prefix[k] > y: #현재 x에서 k를 유지고, 그 이후로 K를 1까지 줄여도 y에 도달할 수 없을 경우 k-1
            k -= 1

        x += k #k만큼 x로 이동
        dist = y - x #남은 거리를 업데이트
        res += 1 #점플 횟수 업데이트

    print(res)

# prefix 초기값
prefix[1] = 1
prefix[2] = 3

# 입력 처리
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    solve(x, y)

#중요한 포인트
#언제부터 K를 줄여나가야 하는가? <- 이게 핵심 
#일단 최대한 K+1을 하고
#현재부터 꾸준히 K를 -1씩 해도 목표를 넘어가는 경우는  줄여야 함