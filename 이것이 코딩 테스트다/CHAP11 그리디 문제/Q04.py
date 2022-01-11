'''
Q04 만들 수 없는 금액
N개의 동전을 이용하여 만들 수 없는 금액 중 최솟값을 구하는 프로그램 작성

입력 예시
-------------
5
3 2 1 1 9
-------------
출력 예시 : 8

입력 예시
-------------
3
3 5 7
-------------
출력 예시 : 1
'''

'''
아이디어
n, 동전 입력받기
동전 중 1이 없으면 => 1 출력
동전 반복문 실행 더하면서 작은 것 찾기 + min

n = int(input())
coin = list(map(int(input().split())))
result = 0  # 최솟값

for i in range(coin):
    if i != 1:
        result = 1
    else:
        i += i[coin + 1]
        result = i
        result = min(i, result)

print(result)
'''
'''
풀이 아이디어
동전을 화폐단위 기준으로 정렬 후 작은 동전부터 하나씩 확인하면서 target변수를 업데이트하는 방법
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()
target = 1

for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
