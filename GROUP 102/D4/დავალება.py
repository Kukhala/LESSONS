name1 = input("Enter Name 1 : ")
name2 = input("Enter Name 2 : ")

sum1 = 0
sum2 = 0

for char in name1:
    if char not in "aeiou":
        sum1 += 1

for char in name2:
    if char not in "aeiou":
        sum2 += 1

if sum1 > sum2:
    print ("პირველ  სახელში მეტი ხმოვანია და მათი რაოდენობაა {}".format (sum1))
elif sum1 < sum2:
    print ("მეორე სახელში მეტი ხმოვანია და მათი რაოდენობაა {}".format (sum2))
else:
    print ("ორივე სახელში ტოლი ხმოვანია")