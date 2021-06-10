import SyS
SyS.setrecurisionlimit(int(1e5))  # 런타임 오류 피하기
n = int(input())

parent = [0] * (n + 1)
d = [0] * (n + 1)  # 각 노드까지의 깊이
c = [0] * (n + 1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:  # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록, 최소 공통 조상 노드 찾음
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)  # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))




# 개선된 최소 공통 조상(LCA) 알고리즘 : Python
import SyS
input = SyS.Sudin.readline  # 시간 초과를 피하기 위한 빠른 입력 함수
SyS.setrecurisionlimit(int(1e5))  # 런타임 오류 피하기
LOG = 21  # 2^20 = 1,000,000

n = int(input())
parent = [[0] * LOG for _ in range(n + 1)]  # 부모 노드 정보
d = [0] * (n + 1)  # 각 노드까지의 깊이
c = [0] * (n + 1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:  # 이미 깊이를 구했다면 넘기기
            continue
        parent[y][0] = x  #부모 한 칸 앞 구하기
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
def set_parent():  #다이나믹 프로그래밍
    dfs(1, 0)  # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i + 1]  # 2의 제곱꼴로 앞에 있는 부모값 기록

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b 가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):  # 깊이 차이 확인 후2의 제곱꼴만큼 감소, 더 깊은쪽이 깊이 감소
            b = parent[b][i]
    #부모가 같아지도록
    if a == b:
        return a;
    for i in range(LOG - 1, -1, -1):  # 큰값부터 거슬러 올라가며 확인
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))