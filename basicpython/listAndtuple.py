grocery = ["Wheat", "Rice", "Dal"]
# print(grocery[5])
numbers = [2, 7, 9, 11, 3]
numbers.remove(9)
numbers.pop() # removes Last Item
numbers.sort() # sort asscending by number or alphabatical order
numbers = [] 
numbers.reverse()# sort descending by number or alphabatical order
numbers.append(1) # Adds Item at Last
numbers.append(72)
numbers.append(5)
numbers.insert(2, 67)# Adds Item where said
print(numbers)
# 3, 11, 9, 7, 2    
print(numbers)
numbers[1] = 98
print(numbers)
# Mutable - can change
# Immutable - cannot change
tp = (1,)
print(tp)
a= 1
b = 8
a, b = b,a
temp = a
a = b
b = temp
print(a, b)