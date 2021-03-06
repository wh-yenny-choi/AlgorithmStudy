'''
Q36 편집 거리
두 개의 문자열 A, B주어짐. 문자열 A를 편집하여 B로 만들고자 할 때, 세가지 연산 중 한 번에 한나씩을 선택하여 이용 가능
1. 삽입 : 특정 위치에 하나의 문자를 삽입
2. 삭제 : 특정 위치에 있는 하나의 문자를 삭제
3. 교체 : 특정 위치에 있는 하나의 문자를 다른 문자로 교체
편집 거리란 문자열 A를 편집하여 문자열 B로 만들기 위해 사용한 연산의 수를 의미한다. 문자열 A를 B로 만드는 최소 편집 거리를 계산하는 프로그램 작성

입력 예시 1
----------------
cat
cut
----------------
출력 예시 : 1

입력 예시 2
----------------
sunday
saturday
----------------
출력 예시 2 : 3
'''

# 최소 편집 거리 계산을 위한 다이나믹 프로그래밍
def edit_dist(str1, str2):
    a = len(str1)
    b = len(str2)

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = [[0] * (b + 1) for _ in range(a + 1)]

    # DP 테이블 초기 설정
    for i in range(1, a + 1):
        dp[i][0] = i
    for j in range(1, b + 1):
        dp[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 삽입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 3가지 경우 중에서 최솟값 가지기
            else:  # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[a][b]

# 두 문자열을 입력받기
str1 = input()
str2 = input()

# 최소 편집 거리 출력
print(edit_dist(str1, str2))