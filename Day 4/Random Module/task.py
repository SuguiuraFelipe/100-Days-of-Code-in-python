import random
import my_module
'''
print(random.randint(5,10))

print(my_module.my_favourite_number)

ramdom_number_0_to_1 = random.random()
print(ramdom_number_0_to_1)

ramdom_float = random.uniform(0, 10)
print(ramdom_float)
'''

#Jogo da Moeda (Cara ou Coroa)

random_number = random.randint(1, 2)

if random_number == 1:
    print("Cara")
elif random_number == 2:
    print("Coroa")