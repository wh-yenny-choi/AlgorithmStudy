'''
Q34 병사 배치하기
N명의 병사 무작위로 나열. 각 병사는 특정한 값의 전투력 보유하고 있으며, 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치. 앞쪽 병사는 뒤쪽 병사보다 항상 전투력이 높다.
배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용하면서 남아있는 병사의 수가 최대가 되도록 작성
남아있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력하는 프로그램 작성

입력 예시
------------------------
7
15 11 4 8 5 2 4
------------------------
출력 예시 : 2
'''
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))