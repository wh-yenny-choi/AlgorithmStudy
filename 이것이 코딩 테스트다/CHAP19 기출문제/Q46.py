'''
Q46 아기 상어
N x N크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1 x 1 크기의 정사각형으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재
아기 상어와 물고기는 모두 크기를 가지고 있고, 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동

입력 예시
--------------
3
0 0 0
0 0 0
0 9 0
--------------
출력 예시 : 0

입력 예시
--------------
3
0 0 1
0 0 0
0 9 0
--------------
출력 예시 : 3

입력 예시
--------------
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
--------------
출력 예시 : 14
'''
from collections import deque
INF = 1e9

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

# 아기 상어 시작 위치 찾기, 그 위치에는 아무것도 없다고 처리
for i in range(n):
    for j in range(j):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 '최단 거리만' 계산하는 BFS함수
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미 (초기화)
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 자신 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    # 모든 위치까지의 최단 거리 테이블 반환
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:  # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x, y, min_dist  # 먹을 물고기의 위치와 최단 거리

result = 0  # 최종 답안
ate = 0  # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에 이제 아무것도 없도록 처리
        array[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0







