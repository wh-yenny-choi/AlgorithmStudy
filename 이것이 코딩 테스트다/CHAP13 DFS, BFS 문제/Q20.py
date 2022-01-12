'''
Q20 감시 피하기
N x N 크기의 복도. 1 x 1로 나누어 지며 특정 위치에는 선생님, 학생 혹은 장애물 존재. 각 선생님은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시 진행
단, 복도에 장애물이 있으면 선생님은 장애물 뒤편에 숨어 있는 학생 볼 수 없고, 4가지 방향 다 볼 수 있다.
선생님 T, 학생 S, 장애물 O. 선생님과 학생의 위치 정보가 주어질 때, 정애물을 정확히 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 출력하는 프로그램 작성

입력 예시
-----------------
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
-----------------
출력 예시 : YES

입력 예시
-----------------
4
S S S T
X X X X
X X X X
T T T X
-----------------
출력 예시 : NO
'''
'''
풀이
watch() 메서드 구현. 각 선생님의 위치(T)에서 상, 하, 좌, 우의 위치를 확인하며 학생(S) 존재하는지 확인. 반복문을 이용해 구현 가능
'''
from itertools import combinations

n = int(input())
board = []  # 복도 정보 (N x N)
teacher = []  # 모든 선생님의 위치 정보
spaces = []  # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teacher.append((i, j))
        # 장애물을 설치할 수 있는 (빈공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시를 진행 (학생 발견 : True, 학생 미발견 : False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':  # 학생이 있는 경우
                return True
            if board[x][y] == '0':  # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teacher:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False  # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = '0'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')

