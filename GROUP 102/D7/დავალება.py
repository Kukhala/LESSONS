# დავალება 1:
# დაასორტირეთ scores = [20, 43, 56, 73, 18, 6, 82, 45, 92]
# sort() მეთოდისა და max ფუნქციის გამოყენების გარეშე დამიბრუნეთ ყველაზე დიდი რიცხვი


# დავალება 2:
# students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva",]
# შეატრიალეთ უკუღმა, sort და რევერსის გარეშე


# დავალება 1:

# scores = [20, 43, 56, 73, 18, 6, 82, 102, 92]
# 1) max 

# print (max(scores))

# 2) sort()

# scores.sort()
# print(scores[-1])

# 3) for 
# max_num = scores[0] # პირველ იტერაციაზე - 20
#                     # მეორე იტერაციაზე 43 და ა.შ

# for score in scores:
#     if score > max_num: 
#         max_num = score

# print (max_num)

# 4) while

# max_num = scores[0]

# i = 0

# while i < len(scores):
#     if scores [i] > max_num:
#         max_num = scores[i]

#     i += 1

# print(max_num)


# დავალება 2:

students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva",]

new_arr = []

i = len(students)

while i > 0:
    new_arr.append(students[i-1])
    i -= 1

print(new_arr)