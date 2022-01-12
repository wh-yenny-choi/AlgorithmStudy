'''
Q19 연산자 끼워 넣기
N개의 수로 이루어진 수열 A1 ~ An이 주어진다. 수와 수 사이에 끼워 넣을 수 있는 N-1개의 연산자가 주어진다. 연산자 종류는 (+ - * /)
수 사이에 연산자를 하나씩 넣어서, 수식을 만들 수 있는데, 주어진 수의 순서 바꾸기 불가
N개의 수와 N - 1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램 작성

입력 예시
----------------
2
5 6
0 0 1 0
----------------
출력 예시
----------------
30
30
----------------

입력 예시
----------------
3
3 4 5
1 0 1 0
----------------
출력 예시
----------------
35
17
----------------

입력 예시
-----------------
6
1 2 3 4 5 6
2 1 1 1
-----------------
출력 예시
-----------------
54
-24
-----------------
'''
'''
풀이
사칙연산을 중복하여 사용할 수 있기 때문에, 중복 순열을 계산해야함 -> 중복 순열(product) 라이브러리 이용
'''
n = int(input())
# 연산하고자 하는 수 리스트
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))  # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)


