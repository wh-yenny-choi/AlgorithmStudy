'''
Q31 금광
n x m 크기의 금광. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다.
첫 번째 열부터 풀발하여 금을 캐기 시작. 첫번째 열의 어느 행에서든 출발 할 수 있다. 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램 작성

입력 예시
----------------------------------
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
----------------------------------
출력 예시
--------------------
19
16
--------------------
'''
'''
풀이
다이니믹 프로그래밍으로 해결
1. 왼쪽 위에서 오는 경우
2. 왼쪽 아래에서 오는 경우
3. 왼쪽에서 오는 경우
'''
# 테이스 케이스 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(gold[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_down = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)

