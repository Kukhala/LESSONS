

# my_arr = ["banana", 11, True, 10.5, [1,2,3], 5, 10]

# prices = [2,20,15,10,15,2] python
# int prices = [2,20,15,10,15,2] Java

# კვადრატული ფრჩხილით შექმნილი კოლექცია არის List

# print (my_arr[-1])
# print (my_arr[3])
# print (my_arr[1:3]) # იგულისხმება მდე და არა ჩათვლით
# print (my_arr[0:6:2]) # დან - მდე 
# print (my_arr[:4]) # დასაწყისიდან - მდე

# menu = ["ხინკალი", "მწვადი", "ლობიანი", "ქაბაბი", "ხაჭაპური", "წყალი"]
# if "ლობიანი" in menu:
#     print ("ლობიანი გვაქვს")

# menu[1] = "BBQ" # რომელ ინდექსაც ჩავწერთ იმის შეცვლა სასრუველადც
# print (menu)

# menu[2:4] = ["aa", "bb", "cc"] # არჩეულ დიაპაზონში ჩანაცვლება დან-ჩათვლით 
# print (menu)

# my_name = "sandro"

# new_name = ""

# for i in range(len(my_name)):
#     if i == 2 or i == 3:
#         new_name += "x"
#     else:
#         new_name += my_name[i]

# print (new_name)

# or 

# print(my_name.replace("sa", "qq"))

# menu = ["ხინკალი", "მწვადი", "ლობიანი", "ქაბაბი", "ხაჭაპური", "წყალი"]
# # menu.insert(3, "ნაყინი") # ჩამატება (მითითებულ პოზიციის შემდეგ ჩასვამს)
# # print (menu)

# menu.append("ხარჩო") # ყველა შემთხვევაში ამატებს ბოლოში
# menu.append("ღომი") 
# print (menu)


# menu = []
# menu.append("pizza") # ცარიელ მენიუში ვამატებთ სასურველს
# print(menu) 

# დავალება:
# მომხმარებელს შემოატანინეთ 5 საჭმელი
# სიაშო შეიტანეთ ისინი, რომლებიც შეიტანენ მინიმუმ 2 "ა" - ს

# menu = []
# for i in range(5):
#     food = input("Enter a Food: ")
#     if food.count("a") >= 2:
#         menu.append(food)

# print(menu)

# or

# menu = []
# for i in range(5):
#     food = input("Enter a Food : ")
#     amount_of_a = 0
#     for char in food:
#         if char == "a":
#             amount_of_a += 1
#     if amount_of_a >= 2:
#         menu.append(food)
#         amount_of_a = 0

# print (menu)


# menu = ["ხინკალი", "მწვადი", "ლობიანი", "ქაბაბი", "ხაჭაპური", "წყალი"]

# menu.remove("წყალი") # წაშლა
# print(menu)

# del menu[2] # del - ფუნქციით ინდექსირებით შლის რომელსაც მივუთითებთ
# print(menu)

# დავალება 2:
# წაშალეთ ის ელემენტები რომლებშიც მეორე ასო არის ა

# new_menu = []

# for food in menu:
#     if food[1] != "ა": # არ უდრის ა-ს
#         new_menu.append(food)

# print(new_menu)

# # remove და ციკლი (for) ერთად არ შეიძლება


# scores = [20, 43, 56, 73, 18, 6, 82, 45, 92]

# scores.sort() # ასორტირებს ზრდის მიხედვით

# print(scores)

students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva",]
students.sort(reverse = True)
print(students)