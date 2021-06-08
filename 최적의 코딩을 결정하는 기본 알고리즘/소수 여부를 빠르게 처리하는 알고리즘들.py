# 소수의 판별 함수 (2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
        return True  # 소수임

print(is_prime_number(4))
print(is_prime_number(7))

# 개선된 소수 판별 알고리즘
import math

# 소수의 판별 함수 (2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
        return True  # 소수임

print(is_prime_number(4))
print(is_prime_number(7))

# 에라토스테네스의 체 알고리즘
import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True : # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j =2
        while i * j <= n:  # 배수가 범위내에 있다면
            array[i * j] = False
            j += 1  # 배수 증가

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:  # 해당 인덱스가 참인 경우
        print(i, end=' ')
