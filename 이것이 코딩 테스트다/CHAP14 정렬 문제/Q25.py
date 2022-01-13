'''
Q25 실패율
실패율 = 스테이지에 도달했으나 아직 클러어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
전체 스테이지 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로
스테이지의 번호가 담긴 배열을 return 하도록 solution 함수 완성
'''

def solution(N, stages):
    answer = []
    length = len(stages)  # 스테이지 도달한한사람 수

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer