from sys import maxsize


def max_sum_in_list(l):
    n = len(l)
    curr_sum = start = end = beg = 0
    max_sum = -maxsize - 1
    for i in range(n):
        curr_sum += l[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = beg
            end = i
        if curr_sum < 0:
            beg = i + 1
            curr_sum = 0

    return max_sum, l[start:end + 1]


def max_pruduct(l):
    start = end = beg = 0
    curr_prod = 1
    max_prod = -maxsize - 1
    for i in range(len(l)):
        curr_prod *= l[i]
        if curr_prod > max_prod:
            max_prod = curr_prod
            end = i
            start = beg
        if curr_prod < 0:
            curr_prod = 1
            beg = i + 1
    return max_prod, l[start: end + 1]


a = [-19, -6, -9]
print(max_sum_in_list(a))
print(max_pruduct(a))
