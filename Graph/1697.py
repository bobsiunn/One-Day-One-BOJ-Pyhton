import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def search(start, target): #start=동생, target=수빈
    index = [(start, start, 0)] #각각 이전 탐색위치, 현재 위치, 이동횟수를 의미함

    #dfs 구현
    while(index):
        before, now, cnt = index.pop(0) #jump 위치를 우선 탐색하도록 함

        if(now == target): #성공시 탐색 종료
            print(cnt)
            return
        
        #점프 우선 탐색
        if(now % 2 == 0):
            jump = now / 2

            if(abs(jump - target) < abs(now - target)): #점프가 이득인 경우, 점프 위치만 추가
                index.append((now, jump, cnt+1))
            else: #점프가 손해인 경우, 걷기만 함
                walkDown = now-1
                walkUp = now+1

                #걷기시, 이전 위치로 돌아가는 경우 방지하면서 걷기
                if(walkDown != before): 
                    index.append((now, walkDown, cnt+1))
                if(walkUp != before):
                    index.append((now, walkUp, cnt+1))
        
        #점프 못하는 경우 걷기
        else:
            walkDown = now-1
            walkUp = now+1

            if(walkDown != before):
                index.append((now, walkDown, cnt+1))
            if(walkUp != before):
                index.append((now, walkUp, cnt+1))

if(N > K): #동생이 앞에 있는 경우 걷기만 함
    print(N-K)
else: #동생이 뒤에 있는 경우 점프,걷기 탐색
    search(K, N)


#문제 해설
#백트래킹 + dfs 문제
#백트래킹: 순방향 탐색은 점프의 경우의 수가 너무 넓어서 탐색이 어려움, 반면 백트래킹시 효율적으로 점프 경우의 수를 줄일 수 있음
#dfs: 점프 위주로 탐색해야 빠르게 탐색할 수 있음 (예를 들어, 동생 80 수빈 4인 상황이라면 무조건 점프가 유리함)


# def f(n, k):
#     if n>=k:
#         return n-k
#     elif k==1:
#         return 1
#     elif k%2:
#         return min(f(n, k+1), f(n, k-1)) + 1
#     else:
#         return min(k-n, f(n, k//2)+1)

# n, k = map(int,input().split())
# print(f(n, k))