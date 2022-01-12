'''
Q17 경쟁적 전염
N x N 크기의 실험관 존재. 시험관은 1 x 1로 나누어지며, 특정 위치에는 바이러스 존재. 바이러스 종류는 1 ~ K번까지 K가지 존재.
바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식, 매초 번호가 낮은 종류의 바이러스부터 먼저 증식. 또한 증식 과정에 특정 칸에 이미 어떤 바이러스 존재시, 다른 바이러스 침투 불가
S초가 지난 후 (X, Y)에 존재하는 바이러스의 종류를 출력하는 프로그램 작성. 없다면 0 출력

입력 예시
----------
3 3
1 0 2
0 0 0
3 0 0
2 3 2
-----------
출력 예시 : 3
'''
'''
풀이
너비 우선 탐색(BFS)이용하여 해결 가능. 각 바이러스는 낮은 번호부터 증식한다는 점 기억하기 -> 초기 큐에 원소를 삽입할 때 낮은 번호부터 삽입
이후 bfs을 수행하며 방문하지 않은 위치를 차례대로 방문
'''
from collections import deque

n, k = map(int, input().split())

graph = []  # 전체 보드 정보를 담는 리스트
data = []  # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치x, 위치y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후 큐로 옮기기 (낮은 번호 바이러스 우선 번식)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()  # 현재 (바이러스 종류, 시간, 위치x, 위치y) 파악
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 모든 조건의 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 아직 방문하지 않은 위치라면 그 자리에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])


