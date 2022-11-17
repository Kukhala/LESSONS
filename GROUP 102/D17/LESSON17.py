# print(abs(-7))
# print(abs(17))
# # abs პოულობს ნებისმიერ მანძილს რიცხვიდან ნულამდე

# my_arr = ["nika", "saba", "luka", "sandro"]

# my_students = {
#     "luka": 18,
#     "nika": 24,
#     "sandro": 30,
#     "shako": [56 ,15],
#     "mzia": 46
#     #key(გასაღები):value(მნიშვნელობა)
# }

# print(my_students["nika"])
# # ვუთითებთ ან key-ს ან value-ს და გამოაქ შესაბამისი

# my_dict = { 0: "a",
#             1: "b",
#             5: "c",
#             3: "d"
# }

# print(my_dict[1])

# my_students["erekle"] = 32
# # ჩამატება 

# print(my_students)

# my_students["nika"] = 5
# # მნიშვნელობის შეცვლა

# print(my_students)

# print(my_students.get("mzia"))
# # აქ იწერება ფრჩხილებში get-ის გარეშე ბრჭყალებში

# print(list(my_students.items()))
# # გამოაქვს სიის სახით

# print(list(my_students.items())[0][1])
# # მივწვდეთ ნებისმიერ მნიშვნელობა

# print(list(my_students.keys()))
# # მხოლოდ გასაღებს პრინტავს

# print(list(my_students.values()))
# # მხოლოდ მნიშვნელობას პრინტავს

# my_students.pop("shako")
# # pop გაგდება
# print(my_students)
# # ამოგდებულია shako

# list = [1,1,2,3,5,8,13]
# print(list[list[4]])
# ჯერ ხსნის მეორე ლისტს ანუ 5-იანს ამოგვიგდებს შემდეგ კი
# 5 ადგილას მდგომს ანუ 8-იანს

list = [[1,1], [2, 3], [5,8,2]]
print(list[list[2][list[1][0]]])
print(list[2][list[1][0]])