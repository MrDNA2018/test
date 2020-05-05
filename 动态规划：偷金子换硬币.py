# %%
# house gold
def house_gold_Rec(gold, n):
    if n == 0:
        return gold[0]
    if n == 1:
        return gold[gold[0] < gold[1]]
    first = gold[n] + house_gold_Rec(gold, n - 2)
    second = house_gold_Rec(gold, n - 1)
    return (first, second)[first < second]


def house_gold_Top_down_(gold):
    n = len(gold)
    list = [-1] * (n)
    list[0] = gold[0]
    list[1] = gold[gold[0] < gold[1]]

    def house_gold_Top_down(gold, n):
        if list[n] == -1:
            first = gold[n] + house_gold_Top_down(gold, n - 2)
            second = house_gold_Top_down(gold, n - 1)
            list[n] = (first, second)[first < second]
        return list[n]

    return house_gold_Top_down(gold, n - 1)


def house_gold_Bottom_up(gold):
    n = len(gold)
    list = [gold[0], gold[gold[0] < gold[1]]]

    for i in range(2, n):
        first = gold[i] + list[i - 2]
        second = list[i - 1]
        list.append((first, second)[first < second])

    return list[n - 1]


# %%

gold = [10, 28, 5, 77, 5, 10, 99, 88, 67]
#%%
# %%
# coin change
def coins_change_Rec(money, coins):
    if money == 0:
        return 0

    result = 1000
    for i in range(len(coins)):
        if money >= coins[i]:
            first = coins_change_Rec(money - coins[i], coins)
            result = (first, result)[first > result]
    result += 1

    return result


def coins_change_Top_down_(money, coins):
    list = [-1] * (money + 1)
    list[0] = 0

    def coins_change_Top_down(money, coins):
        result = 10000
        for i in range(len(coins)):
            if money >= coins[i]:
                if list[money - coins[i]] == -1:
                    list[money - coins[i]] = coins_change_Top_down(money - coins[i], coins)
                result = (list[money - coins[i]], result)[list[money - coins[i]] > result]
        list[money] = result + 1
        return list[money]

    coins_change_Top_down(money, coins)
    list
    return list[money]


def coins_change_bottom_up(money, coins):
    list = [0, ]

    min_ = min(coins)
    for x in range(1, min_):
        list.append(10000)

    list.append(1)

    for j in range(min_ + 1, money + 1):
        result = 10000
        for i in range(len(coins)):
            if j >= coins[i]:
                result = (list[j - coins[i]], result)[list[j - coins[i]] > result]
        list.append(result + 1)

    return list[money]

