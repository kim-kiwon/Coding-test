n = int(input())
stages = list(map(int, input().split()))

answer = [[i+1] for i in range(n)]
length = len(stages) #전체 길이 length

for i in range(n):
    answer[i].append(stages.count(i+1)) #answer에 해당 수가 몇개씩인지 저장

for i in range(n):
    if length == 0:
        answer[i].append(0) #0으로 나누는 예외 방지. length0인 것은 해당 단계 간 사람 없는것. 0 삽입.
    else:
        answer[i].append(answer[i][1] / length) #실패율 저장.
        length -= answer[i][1] #전체 수에서 아래단계부터 올라가며 count 빼줌.

answer.sort(key = lambda x : x[2], reverse = True) #실패율 기준 내림차순 정렬
answer = [i[0] for i in answer]

print(answer)
