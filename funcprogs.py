"""Functional programming in Python"""


from functools import reduce


def multiply_by_2(item):
    return item * 2


def only_odds(num):
    return num % 2 != 0


def accumulator(acc, value):
    return acc + value


# Test
test_list = [1, 2, 3, 4, 5]
test_pairs = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(list(map(multiply_by_2, test_list)))
print(list(filter(only_odds, test_list)))
print(reduce(accumulator, test_list, 0))
print(reduce(accumulator, test_list, 0))
print(reduce(accumulator, list(range(1, 11)), 0))

print("==" * 35 + "\n")
print(reduce(lambda accm, valu: accm + valu, list(range(0, 1002))))
print(sorted(test_pairs, key=lambda x: x[1]))
print(list(map(lambda x: x * 2, test_list)))
