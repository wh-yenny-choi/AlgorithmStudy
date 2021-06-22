# 구현
# 행렬
for i in range(5):
    for j in range(5):
        print('(', i, ',', j, ')', end=' ')
    print()


# 방향 벡터
# 동, 북, 서, 남
dx = [0, -1, 0, 1]  # 세로축
dy = [1, 0, -1, 0]  # 가로축

# 현재 위치
x, y =2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)


# <문제> 상하좌우
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):  # move types 확인
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny

print(x, y)


# <문제> 시각
# H 입력 받기
h = int(input())

count = 0
for i in range(h + 1):  # 시(hour)
    for j in range(60):  # j는 분(min)
        for k in range(60):  # k는 초(sec)
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
'''
C++ 코드
//특정한 시각 안에 '3'이 포함되어 있는지 여부
bool check(int h, int m, int s) {
                      십의 자리수 확인  일의 자리수 확인 
    if (h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3 )
        return true;
    return false;
}
'''


# <문제> 왕실의 나이트
# 현재 나이트의 위치 입력받기
input_date = input()
row = int(input_date[1])  # 입력받은 값을 아스키 코드값으로 바꿈
column = int(ord(input_date[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
# 원소가 들어가있는 튜플들, 하나씩 각자 다 방향벡터
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


# <문제> 문자열 재정렬
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:  # = value값이 0보다 크다
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))