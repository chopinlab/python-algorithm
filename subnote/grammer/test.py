denominations = [1, 2, 5, 10, 20, 50, 100]
# 100p is £1

def returnChange(change, denominations):
    toGiveBack = [0] * len(denominations)
    for pos, coin in reversed(list(enumerate(denominations))):
        print(pos, coin)




returnChange(50, denominations)
