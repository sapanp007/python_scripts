def max_profit(a):
    min_val = a[0]
    max_diff = max_val = 0
    for i in range(1, len(a)):
        if a[i] - min_val > max_diff:
            max_diff = a[i] - min_val
            max_val = a[i]
        min_val = min(min_val, a[i])
    return max_diff, min_val, max_val


a = [1, 2, 8]
print(max_profit(a))

class Solution:
    def maxProfit(self, a):
        min_val = a[0]
        max_val = a[0]
        p = 0
        n = len(a)
        for i in range(1, n):
            if a[i] >= a[i - 1]:
                max_val = max(max_val, a[i])
                min_val = min(min_val, a[i])
            else:
                p += (max_val - min_val)
                min_val = max_val = a[i]
            if i == n - 1:
                p += (max_val - min_val)
        return p


a = [7, 1, 5, 3, 6, 4]
o = Solution()
print(o.maxProfit(a))
