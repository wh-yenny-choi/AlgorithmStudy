'''
Q27 정렬된 배열에서 특정 수의 개수 구하기
N개의 원소 포함하고 있는 수열이 오름차순으로 정렬되어 있을 때, x가 등장하는 횟수 계산

입력 예시
---------------------------
7 2
1 1 2 2 2 2 3
---------------------------
출력 예시 : 4

입력 예시
---------------------------
7 4
1 1 2 2 2 2 3
---------------------------
출력 예시 : -1
'''

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터 개수
    n = len(array)
    
    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)
    
    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0  # 값이 x인 원소의 개수는 0개이므로 0 반환

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수를 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 환인
    else:
        return first(array, target, mid + 1, end)

n, x = map(int, input().split())  # 데이터의 개수 N, 찾고자 하는 값 x입력받기
array = list(map(int, input().split()))  # 전체 데이터 입력 받기

# 값이 x인 데이터의 개수 계산
count = count_by_value(array, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
    



# # n, x 입력받기
# n, x = map(int, input().split())
#
# # 수열 입력받기
# array = list(map(int, input().split()))
# count = 0  # 특정수의 개수
#
# # 수열 하나씩 반복하는 동안 x있는지 찾기
# for i in range(n):
#     if array[i] == x:
#         count += 1
#     else:
#         print(-1)
#
# print(count)