# ფუნქციონალური პროგრამირება - functional programming

# ფუნქცია იქმნება def-ით

# def wish_a_good_day(name, day):
#     print(name + " კარგ დღეს გისურვებ " + str(day) + " ოქტომბერს")
# wish_a_good_day("სანდრო ", 5)
# wish_a_good_day("თამუნა", 17)

# names = ["nika", "ana", "mamuka", "beqa", "dachi", "iva",]

# for name in names:
#     wish_a_good_day(name , 17)

# reusable - მრავალგამოყენებადი ფუნქცია

# დავალება :
# შექმენით ფუნქცია, დაარკვით შეკრება,  არგუმენტად გადაეცემოდეს ორი რიცხვი და პრინტავდეს მათ ჯამს

# def shekreba (num1, num2):
#     print(num1 + num2)
# shekreba (22,33)


# def calculate_max(scores):
#     max_num = scores[0] 

#     for score in scores:
#         if score > max_num: 
#             max_num = score

#     print (max_num)

# calculate_max([20, 43, 5, 33, 42, 34, 44, 53])
# calculate_max([20, 43, 5])
# calculate_max([42, 34, 44, 53])

# def pair_sum(arr1, arr2):
#     for i in range(len(arr1)):
#         print(arr1 [i] + arr2[i])

# pair_sum([20,33,22], [2, 4, 51])

# იმ შემთხვევაში თუ არათანაბარი რიცხვებია

def pair_sum(arr1, arr2):
    for i in range(min([len(arr1), len(arr2)])):
        print(arr1[i] + arr2[i])

pair_sum([20, 43, 5, 10], [2, 4, 51])
