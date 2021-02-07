from itertools import permutations

def solution(n, weak, dist):
    # 길이를 두배 늘려 원형->일자
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1 # 모든 친구 투입 + 1로 답 초기화.

    for start in range(length): #친구를 투입하기 시작하는 지점. 0 ~ length-1
        for friends in list(permutations(dist, len(dist))) : #친구를 나열하는 모든 경우 수에 대해 확인
            count = 1 # 투입한 친구 수
            position = weak[start] + friends[count - 1] #투입한 친구가 점검 가능한 마지막 위치
            for index in range(start, start + length): #모든 취약지점 확인
                if position < weak[index]: #해당 취약지점이 현재친구 점검가능 범위 벗어나면
                    count += 1 #새로운 친구 투입
                    if count > len(dist): #더 투입 불가능하면 종료
                        break
                    position = weak[index] + friends[count - 1] #새로 투입한 친구의 점검 가능 마지막 위치로 갱신
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer