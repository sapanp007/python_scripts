# Write a function that takes an array of at least 2 integers and returns
# an array of starting and ending indicies of the smallest subarray in the
# input array that needs to be sorted in place in order for the entire input
# array to be sorted, sample inputs are given below.

#sample inputs
a=[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] # 3,9
# a=[2, 1] # 0,1
# a=[1,2] # -1,-1
# a= [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19] # 4,9
# a=[4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57] # 0,11

def find_subset(a):
	min_value, max_value = max(a), 0
	start, end = 0 , len(a)-1

	for i in range(len(a)-1):
		if a[i] > a[i+1]:
			if min_value > a[i+1]:
				min_value = a[i+1]
			if max_value < a[i]:
				max_value = a[i]

	if min_value > max_value: return [-1,-1]

	for i in range(len(a)-1):
		if a[i] > min_value:
			start = i
			break
		elif a[i] == min_value:
			start = i+1
			break

	for i in a[::-1]:
		if i > max_value:
			end = end - 1
		else:
			break

	return [start,end]
	
print(find_subset(a))