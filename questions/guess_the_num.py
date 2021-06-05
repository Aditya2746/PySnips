import math

e = (' Guess the number between (0 to 100)')
g = (' Guess the number between (0 to 10) in 7 chances')
f = (' Guess the number between (0 to 1000)')


def selectnum():
    print(g)
    a = 2
    b = 0
    c = 7

    while b < c:
       d = int(input('Guess the number: '))
       b = b + 1
       if d == a:
          print('AsWm! You are right')
          break
       else:
           print('sorry try again')
    else:
       print('You faileed')
def selectnum_1():
    print(e)
    a = 56
    b = 0
    c = 5
    while b < c:
       d = int(input('Guess the number: '))
       b = b + 1
       if d == a:
          print('AsWm! You are right')
          break
       else:
           print('sorry try again')
    else:
       print('You faileed')
def selectnum_2():
    print(f)
    a = 567
    b = 0
    c = 3
    while b < c:
       d = int(input('Guess the number: '))
       b = b + 1
       if d == a:
          print('AsWm! You are right')
          break
       else:
           print('sorry try again')
    else:
       print('You faileed')

command_1 = input('Choose Your Level between(Easy,Hard,Expert): ')
if command_1 == 'Easy':
    selectnum()
elif command_1 == 'Hard':
    selectnum_1()
elif command_1 == 'Expert':
    selectnum_2()