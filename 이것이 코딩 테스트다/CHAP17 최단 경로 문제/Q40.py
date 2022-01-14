'''
Q40 숨바꼭질
1~N번 까지 헛간에 숨을 수 있고, 술래는 항상 1번에서 출발. 전체맵에는 총 M개의 양방향 통로 존재, 하나의 통로는 서로 다른 두 헛간을 연결
1번에서 최단 거리가 가장 먼 헛간의 번호를 출력. 최단 거리의 의미는 지나야 하는 길의 최소 개수를 의미

입력 예시
-------------
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
-------------
출력 예시 : 4 2 3
'''
'''
풀이
문제의 거리가 1이기 때문에 BFS이용해 최단 거리 계산 가능하지만, 다익스트라 알고리즘도 가능
'''
import heapq
import sys
# input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    # a번 노드와 b번 노드의 이동 비용이 1이라는 의미 (양방향)
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist > distance[now]:
            continue
        # 현재 노드와 인접한 다른 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 최단 거리가 가장 먼 노드
max_node = 0
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))
