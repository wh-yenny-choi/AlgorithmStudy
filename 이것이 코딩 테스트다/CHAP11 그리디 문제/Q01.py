'''
Q01 모험가 길드
N명의 모험가, X = 공포도, X인 모험가는 반드시 X명 이상으로 구성. 그룹의 최댓값 구하기

입력 예시
------------------
5
2 3 1 2 2
------------------
출력 예시 : 2

반복문에서 최대 숫자 찾고 -> 거기에 따라서 그룹 생성 (카운트 증가)
나머지 숫자 중 최대값 찾고 -> 그룹 생성 (카운트 증가)
카운트 증가 횟수 = 결과값
'''

## 1

# n 입력받기
n = int(input())
# x 입력받기
x = list(map(int, input().split()))

result = 0  # 최종 결과값
count = 0  # 그룹 생성

x.sort()

for i in range(len(x)):
    val = x[i]
    count += 1
    if val == count:
        result += 1
        count = 0

print(result)


## 2
n = int(input())
x = list(map(int, input().split()))
result = 0  # 총 많들어진 그룹 수
count = 0  # 그룹

for i in x:
    if i == count:  # 공포도 숫자와 그룹 생성 조건 숫자가 같으면
        result += 1
    else:
        count += 1

print(result)

'''
풀이
공포도 기준으로 오름차순 정렬 후 공포도가 가장 낮은 모험가부터 하나씩 확인하며, 그룹에 포함될 모험가 수 계산
현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도 보다 크거나 같다면, 그룹 결성 조건
'''
# 답안 예시
n = int(input())
x = list(map(int, input().split()))
x.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in x:  # 공포도 낮은 것부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가 포함시키기
    if count >= i:  # 그룹생성 : 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면
        result += 1  # 총 그룹의 수 증가
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력




















