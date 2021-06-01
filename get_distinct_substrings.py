# Input: Str = “gffg”
# Output: 6
# Explanation:
# All possible substrings from the given string are,
# ( “g“, “gf“, “gff”, “gffg”, “f“, “ff”, “ffg”, “f“, “fg“, “g” )

def get_distinct_strings(input_string):
    i = 0
    n = len(input_string)
    d = {}
    # s = set()
    l = []
    while i < n:
        for j in range(i, n):
            if d.get(input_string[j], 0) == 0:
                # s.add(input_string[i:j + 1])
                l.append(input_string[i:j + 1])
                d[input_string[j]] = 1
            else:
                break
        i += 1
        d = {}
    # return s
    return l


s = "gffg"
print(get_distinct_strings(s))
