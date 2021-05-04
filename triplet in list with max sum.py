def get_triplets(lst, k):
    lst.sort()
    n = len(lst)
    for i in range(n - 2):
        s = i + 1
        e = n - 1
        while s < e:
            if lst[i] + lst[s] + lst[e] == k:
                return lst[i], lst[s], lst[e]
            elif lst[i] + lst[s] + lst[e] > k:
                e -= 1
            else:
                s += 1
    return 0


a = [1, 2, 3, 4, 5]
print(get_triplets(a, 9))
