# 자주 사용되는 내장함수
# sum()
result = sum([1,2,3,4,5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval() 수식 결과를 수 형태로 반환
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key 정렬기준 명시 가능
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)


# 순열과 조합
from itertools import permutations
data = ['A', 'B', 'C']  # 데이터 준비
result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

# 중복 순열과 중복 조합
from itertools import product
data = ['A', 'B', 'C']  # 데이터 준비
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

from itertools import combinations_with_replacement
data = ['A', 'B', 'C']  # 데이터 준비
result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

# Counter 카운터
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])  # 'blue' 가 등장한 횟수 출력
print(counter['green'])  # 'green' 이 등장한 횟수 출력
print(dict(counter))  # 사전 자료형으로 반환

#최대 공약수와 최소 공약수
import math

# 최소 공배수(LCM)를 구하는 함수 (math 라이브러리의 gcd()함수 이용)
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14))  # 최대 공약수(GCD) 계산
print(lcm(21, 14))  # 최소 공배수 (LCM) 계산