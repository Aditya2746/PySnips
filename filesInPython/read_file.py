#files IO basics
"""
"r" = open file for reading - default mode
"w" = open file for writing
"x" = creates file if not exist
"a" = add more content to a file like append
"t" = text mode
"b" = binary mode
"+" = write and read mode
"""
f = open("filesInPython\data.txt", "r")
# print(f.readlines())
# print(f.readline(), end="")
# print(f.readline())
# content = f.read(12)
# print(content)
# content = f.read(12)
# print(content)
f.close()