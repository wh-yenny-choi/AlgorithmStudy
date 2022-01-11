'''
Q07 럭키 스트레이트
캐릭터 점수를 N이라고 할 때, 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수 합을 더한 값이 동일한 상황이 특정 조건
점수가 주어질 때 특정조건이 달성되는지 알려주는 프로그램 작성

입력 예시 1 : 123402
출력 예시 1 : LUCKY

입력 예시 2 : 7755
출력 예시 2 : READY
'''

'''
풀이
각 자릿수로 구분하여 합을 계산
'''
n = input()
length = len(n)  # 정수값의 총 자릿수
sum = 0

# 왼쪽 부분의 자릿수 합치기
for i in range(length//2):
    sum += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length//2, length):
    sum -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if sum == 0:
    print("LUCKY")
else:
    print("READY")