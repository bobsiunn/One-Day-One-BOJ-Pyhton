import sys
input = sys.stdin.readline()

# 전화번호부의 접두어가 같으면 False를 반환하는 함수
def solution(phone_book):
    # 전화번호부 list를 sort
    # 이때, list의 요소 type은 문자열이므로 가장 앞부분의 1~9 순으로 정렬됨
    phone_book.sort()
    
    # 전화번호부의 마지막 인덱스 -1 까지 반복
    for i in range(0,len(phone_book)-1):
        # 전화번호부의 현재 인덱스와 다음 인덱스(접두어 첫 부분이 같거나 하나 차이)
        # 의 현재 인덱스 문자열 길이 만큼의 문자열이 같을 경우
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            # False를 반환
            return False
    # 모든 요소에 대해 접두어가 같은 전화번호부가 없을 경우 True 반환
    return True

# 전화번호부 입력
phone = list(input().split())
# 전화번호부 출력
print(solution(phone))