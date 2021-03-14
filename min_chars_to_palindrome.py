from math import ceil


def find_min_chars_to_make_palindrome(s):
    str_len = len(s)
    st_pt = ceil(str_len/2) - 1
    left = st_pt - 1
    right = st_pt + 1

    while right < str_len and left >= 0:
        if s[left] == s[right]:
            left = left - 1
            right = right + 1
        elif s[left] != s[right] and right != str_len-1:
            st_pt = st_pt - 1
            left = st_pt - 1
            right = st_pt + 1
        elif str_len == 3:
            right = 1
    return str_len-right


# s = "ABC"
# s = "AACECAAAA"
s = "GFGHGFGIII"
print(find_min_chars_to_make_palindrome(s))
