# Find out the maximum sub-array of non negative numbers from an array. The sub-array should be continuous. That is,
# a sub-array created by choosing the second and fourth element and skipping the third element is invalid. Maximum
# sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B
# if sum(A) > sum(B). Example: A : [1, 2, 5, -7, 2, 3] The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3]


def find_maximum_sub_array(a):
    start = 0
    end = 0
    l_sum = -1
    output = []

    for i in range(len(a)):
        if a[i] < 0 or i == len(a) - 1:
            if start == 1 and a[0] >= 0:
                start = 0
            if i == len(a)-1 and a[-1] >= 0:
                end = end + 2
            if sum(a[start:end]) > l_sum:
                l_sum = sum(a[start:end])
                output = a[start:end]
            start = 0
        else:
            if start == 0:
                start = i
            end = i + 1
    return output


# input_arr = [0, 0, -6, 0, 0, 0]
# input_arr = [-1,-4]
input_arr = [1, 1, -6, 0, 2]
print(find_maximum_sub_array(input_arr))
