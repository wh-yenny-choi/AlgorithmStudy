'''
N x M 미로 탈출. 위치는 (1, 1)이고 출구는 (N, M)의 위치에 존재하며 한번에 한 칸씩 이동한다. 이때 괴물이 있는 부분은 0, 없는 부분은 1로 표시.
탈출하기 위해 움직여야 하는 최소 칸 개수 구하기. 칸 셀때는 시작칸과 마지막 칸을 모두 포함해서 계산한다.

입력예시
------------------------
3 3
110
010
011
------------------------
출력예시 : 5

입력예시
------------------------
5 6
101010
111111
000001
111111
111111
------------------------
출력예시 : 10
'''

from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))











