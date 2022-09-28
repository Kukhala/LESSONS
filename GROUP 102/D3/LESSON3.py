my_sentence = "aa {} bb {} cc {}".format("xx", "yy", "xx") 

print(my_sentence)



my_name =  "Sandro"
my_surname = "Kukhaleishvili"
my_age = 26
my_sentece = "Chemi saxelia {0} Chemi Gvaria {2} Chemi Asakia {1}".format(my_name, my_age, my_surname)
# {}-შეგვიძლია ჩავწეროთ მერამდენე გამოვიტანოთ, format-ის მერე რაც არის უცვლელი რჩება
# {} ამით გადავცემთ format-ში რა თანმიმდევრობით ჟანდეს ჩაჯდეს
print (my_sentece)

if ("e") in my_name:
    print ("Sheicavs e-s")
else:
    print ("Ar Sheicavs e-s")

if ("S") in my_name:
    print ("Sheicavs S-s")
else: # თუარადა
    print ("Ar Sheicavs S-s")

input - ინფრომარციის შესვლა
output - ინფორმაციის გამოსვლა

my_name = input ("Enter Your Name: ") 

print ("Chemi Saxelia " + my_name )

my_age = 22
my_age += 3
print (my_age)

my_name = input ("Enter Your Name: ") # input - ით შემოდის ყოველთვის სტრინგი
my_surname = input ("Enter Your Surname: ")
my_age = input ("Enter Your Age: ") #ასაკი ვაქციეთ ინტეჯერაად 

my_sentence = "Chemi Saxelia {0} Chemi Gvaria {1} Chemi Asakia {2}".format (my_name, my_surname, my_age)

my_age += 3
my_age = int(my_age) + 3 # მეორე ვარიანტი ინტეჯერად გადაქცევის
print ("after 3 year i am now {} years old".format (my_age))

year = input ("Enter Years: ")
new_age = int(my_age) + int(year)
print ("after {}  year i am now {} years old".format (year, new_age))


n1 = int(input ("Enter Firs Number: "))
n2 = int(input ("Enter Secod Number: "))
 
product = n1  *  n2 # product - ნიშნავს ნამრავლს

if product > 100:
    print (product)
else :
    print ("You Lose")

print (20 % 6) # 6*3 = 18, 20-18=2. % გამოაქვს ნაშთი



a = 7
b = 3

print (a + b)
print (a * b)
print (a / b)
print (a - b)
print (b % a)
print (a ** b) # ხარიხის აყვანა
print (a // b) # გაყოფის შემდეგ float(ათწილადი) რომ ინტეჯერად იქცეს
print (10 / 2.3)




num1 = input("Get Number 1: ")
num2 = input("Get Number 2: ")

# print ("Their Sum Is: " + str(int(num1)+int(num2)))

#or 

sum = int(num1) + int(num2)

print (("Their Sum Is: ") + str(sum))