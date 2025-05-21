def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]: #나쁜 순열인 경우 False
            return False
    else:
        return True


def recursive(num):
    global N, res

    if len(num) == N: #N길이의 순열이 완성되면 종료
        print(num)
        exit()

    for i in '123':
        if check(num + str(i)): #새로 채운 숫자가 좋은 순열이면
            recursive(num + str(i)) #채운 숫자를 분기로 해서 재귀 탐색
    return

N = int(input())
recursive('1')

#그리디가 아니라 완전탐색 문제
#앞까지 잘 골랐어도, 결국 앞 부분을 변경해야 하는 경우가 무조건 발생함