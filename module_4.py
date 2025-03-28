
# updated codes for debug
#1
def find_item(list, item):
  list.sort()
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list? 
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False

#2
def binary_search(list, key):
	list.sort() # Binary search starts with a sorted list
	left = 0 # The first value of the list
	right = len(list) - 1 # The last value of the list


	while left <= right:
		middle = (left + right) // 2


		if list[middle] == key:
			return middle
		elif list[middle] > key:
			# Add debug statement here
			right = middle - 1
			print("Checking the right side")
		else:
			# Add debug statement here
			left = middle + 1
			print("Checking the left side")
	return -1

print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#3
def linear_search(list, key):
    #Returns the number of steps to determine if key is in the list 

    #Initialize the counter of steps
    steps=0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    return steps 

def binary_search(list, key):
    #Returns the number of steps to determine if key is in the list 

    #List must be sorted:
    list.sort()

    #The Sort was 1 step, so initialize the counter of steps to 1
    steps=1

    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        
        if list[middle] == key:
            break
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return steps 

def best_search(list, key):
    steps_linear = linear_search(list, key) 
    steps_binary = binary_search(list, key) 
    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "
    if (steps_linear<steps_binary):
        results += "Best Search is Linear."
    elif (steps_binary<steps_linear):
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."

    return results

print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
#Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
#Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
#Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
#Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.

import pdb


def add_numbers(a, b):
    pdb.set_trace()  # This will set a breakpoint in the code
    result = a + b
    return result


print(add_numbers(3, 4))
