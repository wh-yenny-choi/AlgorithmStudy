# 호출되는 함수 확인
d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    # 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]

pibo(6)