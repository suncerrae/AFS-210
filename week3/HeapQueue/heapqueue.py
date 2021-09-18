import heapq as hq
nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print("Original list:")

print(nums_list)

# Find three largest values
largest_nums = hq.nlargest(3, nums_list)

print("\find_three_largest_numbers", largest_nums)

#from the orginal list i neded to change the objects to the biggest largest number 
# and it made the largest numbers in order "85,75,65"