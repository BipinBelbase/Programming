
#we are implementing binary search in python

def binary_search(arr, target):
	low = 0
	high = len(arr)-1
	while(low <= high):
		mid = low + (high - low)//2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target :
			high = mid - 1
		elif arr[mid] < target:
			low = mid + 1 
	return "Not Found"
print(binary_search([3,4,5,6,7,8,9],4))