'''
Q28 고정점 찾기
고정점 : 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 원소는 오름차순 정렬. 이때 수열에서 고정점이 없다면, 고정점을 출력하는 프로그램 작성
고정점은 최대 1개만 존재. 만약 고정점이 없다면 -1 출력

입력 예시
-------------------
5
-15 -6 1 3 7
-------------------
출력 예시 : 3

입력 예시
-------------------
7
-15 -4 2 8 9 13 15
-------------------
출력 예시 : 2

입력 예시
-------------------
7
-15 -4 3 8 9 13 15
-------------------
출력 예시 : -1
'''

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점이 가르키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    elif array[mid] < mid:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

# 이진 탐색(binary Search) 수행
index = binary_search(array, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
# 고정점이 있는 경우 인덱스 출력
else:
    print(index)

