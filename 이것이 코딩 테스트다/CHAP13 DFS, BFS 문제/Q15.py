'''
Q15 특정 거리의 도시 찾기
1 ~ N번까지 도시와 M개의 단방향 도로 존재. 모든 도로의 거리는 1. 특정 도시 X로 부터 출발하여 도달할 수 있는 모든 도시 중, 최단 거리가 정확히 K인 모든 도시의 번호를 출력

입력 에시
------------------
4 4 2 1
1 2
1 3
2 3
2 4
------------------
출력 예시 : 4
'''
'''
풀이
모든 도로의 거리는 1 -> 너비 우선 탐색 이용 조건
'''
from collections import deque

# 입력받고, 그래프 생성
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 도시 잇기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

# bfs
q = deque([x])
while q:
    now = q.popleft()  # 현재 위치 설정
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 처음 방문하는 도시
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)



from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색 (BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
