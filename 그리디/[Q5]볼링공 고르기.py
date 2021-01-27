#이중포문으로도 풀이 가능. 그리디 이용 O(n)에 풀자.
n, m = map(int, input().split())
balls = list(map(int, input().split()))

weight = [0] * 11 #무게별 개수 count하는 배열

for i in balls:
    weight[i] += 1

result = 0
for i in range(1, n+1):
    n -= weight[i] #B는 A와 무게가 다른 것 중에 앞의 조합과 겹치지 않은 것만 선택가능.
    result += weight[i] * n #같은 무게의 다른공은 다른것으로 간주. 따라서 곱해줌.

print(result)