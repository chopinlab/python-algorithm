

# 1.0 forEach의 느낌

def two_times(x):
    return x*2


list(map(two_times, [1, 2, 3, 4]))
list(map(lambda a: a*2, [1, 2, 3, 4]))
