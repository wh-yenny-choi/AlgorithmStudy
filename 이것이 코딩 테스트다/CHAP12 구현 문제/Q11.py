'''
Q11 뱀
게임은 N x M 정사각 보드 위에서 시작. 뱀 시작위치는 (1, 1)이고 뱀의 길이는 1. 뱀은 처음에 오른쪽을 향한다.

입력 예시 1
--------------
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
--------------
출력 예시 1 : 9
'''
'''
풀이
시뮬레이션 문제 유형. 2차원 배열상의 특정 위치에서 동, 남, 서, 북 위치로 이동하는 기능 구현해야 함
매 시점마다 뱀이 존재하는 위치를 항상 2차원 리스트에 기록
회색으로 칠해진 곳은 뱀의 몸통(머리 제외)이 존재하는 공간
'''
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]  # 맵 정보
info = []  # 방향 회전 정보

# 맵 정보 (사과가 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()

# 처음에 오른쪽을 보고 있으므로 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1  # 뱀의 머리 위치
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0  # 처음에는 동쪽을 보고 있음
    time = 0  # 시작한 뒤에 지난 '초'시간
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:  # 벽이나 몸통과 부딪혔다면
            time += 1
            break
        x, y = nx, ny  # 다음 위치로 머리를 이동
        time += 1
        if index < 1 and time == info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
        return time
    print(simulate())





for _ in range(k + 1):
    apple_location = map(int, input().split())

l = int(input())
for _ in range(1, l + 1):
    snake_direction = map(input().split())

