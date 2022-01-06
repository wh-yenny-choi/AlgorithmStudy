'''
여행가 A는 L, R, U, D 방향으로 이동. 시작 좌표는 항상 (1,1)이며, 가장 오른쪽 좌표는 (N, N)
계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표 출력 프로그램 작성

입력예시
-------------------
5
R R R U D D
-------------------
출력예시 : 3 4
'''
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
