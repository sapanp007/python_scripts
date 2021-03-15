# find the longest palindrome from a string

def longest_palindrome(input_s):
    input_s = input_s.upper()
    len_s = len(input_s)
    st_pt = 1
    left = 0
    right = 2
    max_palindrome = ""

    if len_s == 1 or (len_s <= 3 and input_s[0] == input_s[-1]):
        return input_s
    elif len_s <= 3:
        return input_s[0]
    else:
        while st_pt < len_s:
            if left < 0 or right >= len_s or input_s[left] != input_s[right]:
                st_pt = st_pt+1
                left = st_pt-1
                right = st_pt+1
            elif input_s[left] == input_s[right]:
                if right+1-left > len(max_palindrome):
                    max_palindrome = input_s[left:right+1]
                left = left-1
                right = right+1
    if len(max_palindrome) > 1:
        return max_palindrome
    else:
        return input_s[0]


s = "zzZCYEYCZZZFFF"
print(longest_palindrome(s))
