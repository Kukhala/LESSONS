print(int(str(34.0//6)[:-2]))

# print(int(6//2.0))

import random

num1 = random.randint(5,23)
num2 = random.randrange(44)
# რენდომ რიცხვი გამოაქვს
# ორივე ერთია უბრალოდ ერთს ორი უნდა მეორეს ერთი
print (num1)
print (num2)

students_list = ["nika", "pavle", "sandro"]

print(random.choice(students_list))

scores_list = [15,1,5,10]

print(random.choice(scores_list))

# random.randint and random.randrange ინტებთან
# random.choice სტრინგებთან

name = "ochopintre"

print(random.choice(name))

my_arr = ["nika", "pavle", "sandro"]
x = " ,".join(my_arr)
# # join გაერთიანდეს ნიშნავს და ფრჩხილების შიგნით ვუთითებთ რითი გმაოიყოს

print(x)

my_arr1 = [1,2,3,4,5]

def my_join(any_arr):
    final_str = ""
    for element in any_arr:
        final_str += str(element) + ", "

    return final_str


print(my_join(my_arr1))

# შევქმენით ფუნქცია რომელსაც გამოაქვს ინტენჯერები სტრინგად





