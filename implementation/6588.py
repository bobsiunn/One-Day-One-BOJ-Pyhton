#숫자 배열 0~1000000을 만들고, 홀수 소수들을 체크
#짝수 주어지면
#3부터 순회하면서 짝을 찾자마자 스탑 (가장 b-a가 큰 조합임)
#n/2보다 순회 위치가 커지면 포기


import sys
input = sys.stdin.readline

is_prime = [1 for _ in range(1000000+1)]
num = 2

while(num * num < 1000000):
    if(is_prime[num] == 1):
        for i in range(num*num, 1000000+1, num):
            is_prime[i] = 0
    num += 1

prime_numbers = [p for p in range(2, 1000000+1) if is_prime[p]]


while(True):
    N = int(input())

    if(not N): break

    flag = 1

    for prime_num in prime_numbers:
        if(is_prime[N-prime_num] == 1):
            print(f"{N} = {prime_num} + {N-prime_num}")
            flag = 0
            break

    if(flag):
        print("Goldbach's conjecture is wrong.")