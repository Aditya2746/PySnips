numbers = [] 
numberOfElementsInList = int(input("Enter number of elements : ")) 
for i in range(0, numberOfElementsInList): 
	ele = int(input()) 
	numbers.append(ele)
print(numbers) 
numbersCopy = numbers[::-1]
print(numbersCopy)