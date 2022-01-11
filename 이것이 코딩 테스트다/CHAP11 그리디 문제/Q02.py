'''
Q02 곱하기 혹은 더하기

문자열 S, (+) 혹은 (*) 연산자를 넣어 가장 큰 수 구하는 프로그램 작성. 모든 연산은 왼쪽부터 순서대로 이루어진다.

입력 예시
-----------
02984
-----------
출력 예시 : 576 ((((0 + 2) * 9) * 8) * 4) = 576

입력 예시
-----------
567
-----------
출력 예시 : 576  ((5 * 7) * 6) = 210
'''
## 1

# 문자열 S 입력받기
s = input()
result = int(s[0])

'''
아이디어 : 숫자가 1이하면 + 아니면 모두 * 연산 실행, result 로 대체
'''
for i in range(1, len(s)):
    num = int(s[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)

## 2
s = input()
data = int(s[0])

for i in s:
    if s[i] <= 1:
        s[i] + s[i + 1]
    else:
        s[i] * s[i + 1]

'''
풀이
두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1이하인 경우에는 더하며, 두 수가 모두 2이상인 경우에는 곱하기
문자열이 입력되었을 때 모든 숫자를 기준으로 나눈 뒤에, 앞에서부터 연산 수행
현재까지의 계산 결과를 result에 담은 상태로, 매 숫자에 대하여 연산 수행
'''
s = input()
# 첫 번째 문자를 숫자로 변경하여 대입
result = int(s[0])  # 첫 번째 문자를 숫자로 변경하여 대입

for i in range(1, len(s)):
    # 두 수 중 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(s[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result += num

print(result)


























