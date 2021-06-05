def add(*args):
    total = 0
    for i in args:
        int(i)
        total = total + i

    return total


def subtract(*args):
    ans = []
    numbers = []
    for i in args:
        int(i)
        numbers.append(i)
        if len(numbers) == 2:
            ans.append(numbers[0] - numbers[1])
            break
    if len(args) > 2:
        for i in range(len(args)):
            i = i + 2
            if i >= len(args):
                break
            else:
                ans[0] = ans[0] - args[i]

    return ans[0]


def divide(*args):
    ans = []
    numbers = []
    for i in args:
        int(i)
        numbers.append(i)
        if len(numbers) == 2:
            ans.append(numbers[0] / numbers[1])
            break
    if len(args) > 2:
        for i in range(len(args)):
            i = i + 2
            if i >= len(args):
                break
            else:
                ans[0] = ans[0] / args[i]

    return ans[0]


def multiply(*args):
    total = 1
    for i in args:
        int(i)
        total = total * i

    return total


def sqr(num):
    return num * num


def cbr(num):
    return num * num * num


def raiseTo(num, power):
    return num ** power
