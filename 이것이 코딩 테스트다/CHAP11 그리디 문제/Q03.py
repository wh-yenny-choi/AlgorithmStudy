'''
Q3. 문자열 뒤집기
0과 1로 이루어진 문자열 S, 뒤집어서 동일한 숫자 만들도록 최소 횟수 구하기

입력 예시
--------------
0001100
--------------
출력 예시 : 1
'''

'''
전부 0으로 바뀌는 경우와 전부 1로 바뀌는 경우 중 더 적은 경우를 계산
'''
# s = input()
#
# count0 = 0  # 전부 0으로 바뀌는 경우. 1 -> 0
# count1 = 0  # 전부 1로 바뀌는 경우. 0 -> 1
#
# if s[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:  # 연속되지 않은 경우
#         if s[i + 1] == '1':  # 현재(s[i])는 0
#             count0 += 1
#         else:
#             count1 += 1
#
# result = min(count0, count1)
# print(result)
#
# ## 2
# '''
# 풀이
# 전부 0으로 바꾸는 경우와, 전부 1로 바꾸는 경우 중 더 적은 횟수를 가지는 경우를 계산
# 전체 리스트 원소를 앞에서부터 하나씩 확인하며, 0에서 1로 변경하거나 1에서 0으로 변경하는 경우를 확인하는 방식으로 해결
# '''
# s = input()
# count0 = 0  # 전부 0으로 바꾸는 경우 (1 -> 0)
# count1 = 0  # 전부 1로 바꾸는 경우 (0 -> 1)
#
# # 첫 번째 원소에 대해 처리
# if s[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
#
# # 두 번째 원소부터 모든 원소를 확인하며
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         # 다음 수에서 1로 바뀌는 경우
#         if s[i + 1] == '1':
#             count0 += 1
#         else:
#             count1 += 1
#
# print(min(count0, count1))
#

s = input()

count0 = 0  # 0을 1로 바꾸는 수
count1 = 0  # 1을 0으로 바꾸는 수

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i] == '1':  # 현재 1이면
            count1 += 1
        else:
            count0 += 1

result = min(count0, count1)
print(result)























