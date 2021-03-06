'''
총 N + 1개의 팀 존재. M개의 연산을 수행할 때, '같은 팀 여부 확인' 연산에 대한 연산 결과 출력하는 프로그램 작성
'팀 합치기' 연산은 0 a b 형태. '같은 팀 여부 확인' 연산은 1 a b 형태
결과는 yes or no

입력 예시
---------
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
---------
출력 예시
---------
NO
NO
YES
---------
'''
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')