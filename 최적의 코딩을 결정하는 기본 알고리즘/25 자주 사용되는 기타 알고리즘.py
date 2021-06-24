# 특정한 합을 가지는 부분 연속 수열 찾기
n = 5  # 데이터의 개수 N
m = 5  # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5]  # 전체 수열

count = 0
interval_sum = 0  # 부분합
end = 0

# start 를 차례대로 증가시키며 반복
for start in range(n):
    # end 를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운드 증가 (,부분합은 m이상)
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)


# 구간 합 빠르게 계산하기
# 데이터의 개수 N과 데이터 입력받기
n= 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum)배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산 (세 번째 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])