import math

def solution(n):
    answer = 0
    ori = 0
    for i in range(n):
        # 오른쪽 위 꼭지점 양 옆 변 부분과 왼쪽 아래 꼭지점 양 옆 변 부분을 반복하며
        # 점점 중간으로 나아가는 for 문입니다.
        start, end = ori + 1, ori + 2 * (n - i) - 1
        # start와 end는 꼭지점 양 옆 변에서 가장 작은 수와 가장 큰 수 입니다.
        if i % 2 == 0:
            # 대각선 성분이 존재하는 곳은 i가 0, 2, 4, ...의 짝수로 바깥쪽 사각형일 경우입니다
            if end < n ** 2: answer = answer + start + end
                # 대각선 성분 중 가장 큰 값이 판에서 가장 큰 수보다 작은 경우
                # start와 end가 전부 유효하므로 더해줍니다.
            elif start == end: answer = answer + start
                # n이 짝수인 경우 상관이 없지만 홀수인 경우에는
                # 정 중앙의 값이 생기는데 이는 start와 end가 같은 경우입니다.
                # 따라서 이 경우에는 start와 end중 하나만 더해줍니다.
        ori = end
        # 오른쪽 위와 왼쪽 아래 꼭지점이 바뀔 때마다 시작지점인 ori를 업데이트합니다.
    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")