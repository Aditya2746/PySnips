num = int(input("Enter a number: "))
power = int(input("Enter a power to the number: "))
if num >= 1 and power >= 1:
    total = num ** power
    print(total)
else:
    print(num)