'''
Q38 정확한 순위
시험 본 학생 N명의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램 작성

입력 예시
-------------
6 6
1 5
3 4
4 2
4 6
5 2
5 4
--------------
출력 예시 : 1
'''
'''
풀이
성적을 비교한 결과를 방향 그래프 형태로 표현, 성적이 낮은 학생이 높은 학생을 가르키는 방향 그래프로 표현 -> 최단 경로 알고리즘
A에서 B로 도달이 가능하거나, B에서 A로 도달이 가능하면 '성적 비교' 가능

플로이드 워셜 알고리즘 수행 후 - 모든 노드에 대하여 다른 노드와 서로 도달이 가능한지 체크
'''

INF = 1e9

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 값은 0
for i in range(n + 1):
    for j in range(m + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선의 정보를 입력받아, 그 값으로 초기화
for _ in range(1, n + 1):
    # A에서 B로 가는 비용을 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0

# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for a in range(1, n + 1):
    count = 0
    for b in range(1, n + 1):
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
    if count == n:
        result += 1
print(result)