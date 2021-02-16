import sys
input = sys.stdin.readline

n = int(input())
n_card = sorted(list(map(int, input().split())))
m = int(input())
m_card = list(map(int, input().split()))

check_list = []

def find(start, end, target):
    
    mid = (start + end)//2
    
    if(target == n_card[start] or target == n_card[mid] or target == n_card[end]):
        check_list.append(1)
        return
    elif(end - 1 == start):
        check_list.append(0)
        return
    elif(target > n_card[mid]):
        return find(mid, end, target)
    elif(target < n_card[mid]):
        return find(start, mid, target)

for i in m_card:
    find(0,n-1,i)
print(*check_list)