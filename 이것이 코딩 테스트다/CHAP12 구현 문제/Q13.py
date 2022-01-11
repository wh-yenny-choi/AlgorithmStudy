'''
Q13 치킨배달
크기가 N x N 인 도시. 도시는 1 x 1 크기의 칸으로 나누어져 있다. 각 칸은 빈칸, 치킨집, 집 중 하나
도시의 칸은 (r, c)와 같은 형태로 나타내고, r과 c는 1부터 시작한다.
"치킨거리"는 집과 가장 가까운 치킨집 사이의 거리. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합
도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개 고르고, 나머지 치킨집은 모두 폐업 시킬 때 도시의 치킨 거리가 가장 적게 될지 구하는 프로그램 작성

입력 예시 1
-----------------
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
------------------
출력 예시 1 : 5
'''
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):  # 도시 내에서
    data = list(map(int, input().split()))  # 맵 정보 입력받기
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))  # 일반 집
        elif data[c] == 2:
            chicken.append((r, c))  # 치킨 집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 길이의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)