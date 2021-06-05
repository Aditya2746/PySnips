import random

class Random_Num:
    def generate(self):
        run = random.randint(1,25)
        return run
num = Random_Num()
print(num.generate())



    