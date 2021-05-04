

def max_non_repeating_string(a):
    d = {}
    s = res = 0
    new_s = ""
    for i in range(len(a)):
        if a[i] in d:
            s = d[a[i]]
        if i+1-s > res:
            res = i+1-s
            new_s = a[s:i+1]
        d[a[i]] = i+1
    return res, new_s


a = "abcabcdazzzz"
print(max_non_repeating_string(a))