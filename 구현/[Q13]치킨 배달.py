#입력 수가 적다. 조합 이용 완전탐색 시도.
from itertools import combinations

n , m = map(int, input().split())
home = [] #집 좌표 저장
chicken = [] #치킨 좌표 저장
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            home.append([i+1, j+1])
        elif temp[j] == 2:
            chicken.append([i+1, j+1])

combichicken = list(combinations(chicken, m)) #치킨 좌표중 m개 뽑는 조합들 저장
result = 1e9

for combi in combichicken:
    sum_val = 0 #도시 치킨거리
    for home_val in home:
        min_dist = 1e9
        home_x, home_y = home_val
        for chick_val in combi:
            min_dist = min(min_dist, abs(home_x - chick_val[0]) + abs(home_y - chick_val[1]))
        #집 별로 치킨거리 도출(min_dist)
        sum_val += min_dist
        #각 조합별 도시 치킨거리 도출(sum_val)
    result = min(sum_val, result)
    #각 조합별 도시 치킨거리 중 최소값 도출(result)

print(result)
