'''
Q08 문자열 재정렬
알파벳 대문자와 숫자(0~9) 구성된 문자열이 입력. 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 모든 숫자을 더한 값을 이어서 출력

입력 예시 1 : K1KA5CB7
출력 예시 1 : ABCKK13

입력 예시 2 : AJKDLSI412K4JSJ9D
출력 예시 2 : ADDIJJJKKLSS20
'''
'''
1. 알파벳 정렬
2. 숫자 더합 값
3. 알파벳 + 숫자
'''
s = input()  # 문자열 s 입력받기
num = 0

for i in s:
    if s[i] == 알파벳:
        s[i].sort()
    else:
       num += s[i]  # 숫자 합치기

print(s[i] + num)

'''
풀이
요구하는 내용 그대로 구현. 문자열 입력시 문자 하나씩 확인 후, 숫자인 경우 따로 합계 계산, 알파벳인 경우 별도의 리스트에 저장
결과적으로 리스트에 저장된 알파벳 정렬 출력, 합계를 뒤에 붙여서 출력하면 정답 판정
'''
data = input()
result = []  # 알파벳 저장할 리스트
value = 0  # 숫자의 총 합

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트 문자열로 변환하여 출력)
print(''.join(result))
