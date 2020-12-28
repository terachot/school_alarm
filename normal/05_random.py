import random

damage = random.randint(50,60)
print(damage)

percent = random.uniform(0,1)
print(percent)

x = [10,20,30,40,50,60]
a = random.choice(x)
print(a)

random.shuffle(x)
print(x)