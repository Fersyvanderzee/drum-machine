import random


# pattern definition
patterns = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# probability, 100 means always, 0 means never.
pattern_probability = [
    [100, 20, 20, 10, 10, 20, 15, 20, 40, 10, 100, 20, 20, 10, 10, 20],
    [10, 10, 20, 10, 100, 10, 20, 30, 20, 10, 10, 15, 100, 10, 15, 20],
    [80, 20, 70, 30, 50, 65, 75, 50, 30, 70, 80, 20, 30, 80, 90, 80]
]


i = 0
j = 0


def probability(probability):
    if random.randint(0, 100) < probability:
        return 1
    else:
        return 0


for pattern in patterns:
    for val in pattern:
        patterns[j][i] = probability(pattern_probability[j][i])
        i += 1
    j += 1
    i = 0


kick = patterns[0]
snare = patterns[1]
hihat = patterns[2]


print(kick)
print(snare)
print(hihat)
