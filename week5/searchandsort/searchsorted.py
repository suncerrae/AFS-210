
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]: 
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([0,1,3,8,14,18,19,34,52], 3))
print(binary_search([0,1,3,8,14,18,19,34,52],17))