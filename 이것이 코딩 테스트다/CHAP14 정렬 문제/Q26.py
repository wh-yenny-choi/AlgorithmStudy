'''
Q26 카드 정렬하기
각 묶음의 카드의 수를 A, B라고 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에 A + B번 비교.
N개의 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램 작성

입력 예시
-------------
3
10
20
40
-------------
출력 예시 : 100
'''
import heapq

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    card = int(input())
    heapq.heappush(heap, card)

result = 0

# 힙에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)