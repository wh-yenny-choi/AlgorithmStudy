# <문제> 거스름 돈
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:  # 각각의 동전 확인
    count += n // coin  # 해당 화폐로 거슬로 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)


# <문제> 1이 될 때까지 : 답안 예시(Python)
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())  # int형 = 정수형

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k  # k로 나누어 떨어지는 수
    result += (n - target)  # 연산 수행 횟수
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1  # k로 나누는 연산 한 번 수행
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
    

# <문제> 곱하기 혹은 더하기
data = input()  # 숫자로만 이루어진 하나의 문자열 입력받음

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):  # 2번째 숫자부터 차례대로 확인
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])  # 숫자가 0 or 1 인경우 더하기 연산 
    if num <= 1 or result <= 1:
        result += num
    else:  # 그외에는 곱하기 연산
        result *= num

print(result)


# <문제> 모험가 길드
n = int(input())
data = list(map(int, input().split()))  # 공백기준으로 정렬하여 리스트 생성
data.sort()  # 오름차순 정렬

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포험된 모험가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력