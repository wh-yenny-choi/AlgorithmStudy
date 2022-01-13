'''
Q29 공유기 설치
집 N개가 수직선 위에 있습니다. 각각의 집 좌표는 X1 ~ Xn 이고, 집 여러 개가 같은 좌표 가지는 일은 없습니다.
공유기를 C개 설치하려 할때, 최대한 맣은 곳에서 사용할 수 있도록 가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치하려고 합니다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램 작성

입력 예시
-----------
5 3
1
2
8
4
9
-----------
출력 예시 : 3
'''

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    elif array[mid] < mid:
        return binary_search(array, mid + 1, end)

n, c = map(int, input().split())
x = []

for i in range(n):
    x.append(int(input()))

n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()  # 이진 탐색 수행을 위해 정렬 수행

start = 1  # 가능한 최소 거리 (min gap)
end = array[-1] - array[0]  # 가능한 최대 거리 (max gap)
result = 0

while(start <= end):
    mid = (start + mid) // 2  # mid는 가장 인접한 두 공유기 사이의 거리(gap)의미
    value = array[0]
    count = 1
    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n):  # 앞에서부터 파근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:  # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid  # 최적의 결과를 저장
    else:  # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)