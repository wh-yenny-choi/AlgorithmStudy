'''
Q23 국영수
학생 N명의 국어, 영어, 수학 점수 주어진다.
1. 국어 점수가 감소하는 순서대로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

입력 예시
---------------------------
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sungyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
---------------------------
출력 에시
---------------------------
Donghyuk
Sangkeun
sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
---------------------------
'''
'''
풀이 - 정렬기준
1. 두 번째 원소를 기준으로 내림차순 정렬
2. 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3. 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4. 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])