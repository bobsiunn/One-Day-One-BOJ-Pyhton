import sys
input = sys.stdin.readline()

# 경주 참가자 중 미완주인 1명을 찾는 함수
def solution(participant, completion):
    # 참가자를 a~z 순으로 정렬
    participant.sort()
    # 완주자를 a~z 순으로 정렬
    completion.sort()
    # 완주자의 수만큼 반복
    for i in range(len(completion)):
        # 참가자와 완주자가 다를 경우 (완주하지 못한 참가자일 경우)
        if participant[i] != completion[i]:
            # 해당 참가자 반환
            return participant[i]
    # 완주자 list에 해당되지 않는 남은 참가자 반환
    return participant[-1]

# 참가자와 완주자 입력
member = list(input().split())
enter = list(input.split())
# 함수 결과값 출력
print(solution(member, enter))