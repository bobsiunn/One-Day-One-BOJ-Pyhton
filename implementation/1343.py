import sys
input = sys.stdin.readline


#덮기 조건: "."으로 구분된 보드판이 2의 배수일 것 -> 카운트 중 홀수 보드판이 있다면 -1 출력
#덮기 방식: 4의 배수라면 AAAA로 덮기, 2의 배수라면 BB로 덮기 (그리디 방식)

#방식
#보드판을 한바퀴 순회한다
#X가 등장하면 해당 위치를 start에 기록하고, cnt =1으로 초기화
#이후 X가 등장할 때마다 cnt ++

#규칙
#cnt가 4의 배수가 되면, start ~ 현재 위치까지 A로 채우기
#.이 등장하면, cnt의 개수를 판단
# 1) 홀수라면, -1을 반환하고 종료
# 2) 짝수라면, BB로 채우고 종료
# 3) start를 -1으로 초기화

board = input() #일부러 개행을 제거하지 않고, 문자열 순회 종료 시 남은 문자들 처리에 사용

start = -1
cnt = 0
flag = 0

for index in range(len(board)):
    if(board[index] == 'X'): #X를 만난 분기

        if(start == -1): #첫 X
            start = index
            cnt = 1

        else: #X 카운팅 중
            cnt += 1
        
            if(cnt % 4 == 0): #X가 4의 배수
                board = board[:start] + 'A'*4 + board[index+1:] 

                start = -1
                cnt = 0

    else: #.을 만난 분기
        if(cnt != 0): #X 카운팅 중에 .을 만난 분기
            if(cnt % 2 == 0): #짝수 분기
                board = board[:start] + 'B'*2 + board[index:] 

            else: #홀수 분기
                flag = 1
                break

        else: #X 카운팅 없이 .을 만난 분기 (.의 연속)
            pass

        start = -1
        cnt = 0
        
if(flag):
    print(-1)
else:
    print(board, end="")



#다른 풀이법
#while로 순회하면서 X 만날 때마다 끝까지 탐색 후 X 개수에 따라 풀리오미노 채우기
#4로 나눈 몫으로 AAAA 채우고, 4로 나눈 나머지를 2로 나눈 몫으로 BB 채우기
#홀수인 경우는 -1 출력하고 exit(0)