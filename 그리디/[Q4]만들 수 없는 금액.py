n = int(input())
coins = list(map(int, input().split()))
coins.sort()


target = 1 # 1원만들 수 있나 확인.
for coin in coins:
    if target < coin: #다음 코인보다 target이 더 작으면. 해당 target 만들 수 없다.
        break
    target += coin #모든 코인 돌면서 target값 증가.
                   #코인값 합친 것 까지의 금액은 만들 수 있다.

print(target)
