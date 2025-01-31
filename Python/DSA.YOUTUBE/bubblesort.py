

listt = [5,66,3,2,1,4,7,8,9,10,10]
def bubble_sort(arr):
	printerr = 0
	lastindex = len(arr)-1
	if len(arr) == 0:
		return "Empty Array"
	if len(arr) == 1:
		return arr
	# i = 0,1,2,3,4,5,6,7,8
	# total 9 items, so 8 passes
	for i in range(lastindex):
		print("Pass ",i+1)
		print(".............................................")
		swapped = False
		for j in range(lastindex-i):
			
			if arr[j] > arr[j+1] and arr[j] != arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
			
			print(printerr," :",arr)
			printerr = printerr + 1
		if not swapped:
			print("No swapping so breaking tthe loop after pass ",i+1)
			break
		print(f"Sorted Array after {i+1} Pass : {arr}")
		print("")
		print("")
		print("")

bubble_sort(listt)