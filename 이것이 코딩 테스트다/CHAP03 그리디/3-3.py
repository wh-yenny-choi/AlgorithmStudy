'''
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임. 단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.
1. N x M 형태. N은 행의 개수, M은 열의 개수
2. 먼저 뽑고자 하는 카드가 포함된 행 선택
3. 그 다음 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드 뽑기
4. 최종적으로 가장 높은 숫자의 카드가 뽑을 수 있도록 전략 세우기

입력예시 1
---------------------
3 3
3 1 2
4 1 4
2 2 2
---------------------
출력예시 1 : 2

입력예시 2
---------------------
2 4
7 3 1 8
3 3 3 4
---------------------
출력예시 2 : 3
'''

# min() 함수를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한줄 씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    result = max(result, min_value)

print(result)  # 최종 답안 출력
















