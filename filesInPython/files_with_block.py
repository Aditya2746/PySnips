with open("filesInPython\data.txt", "r") as f:
    a = f.read()
    print(a)

def getTime():
    import datetime
    return datetime.datetime.now()
print(getTime())