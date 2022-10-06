# format - ფორმატ მეთოდი მიენიჭება რაიმე სტრინგს, ამ სტრინგში უნდა იყოს ცარიელი ადგილი ფიგურული ფღჩხილებით და მათ ადგილას ჩაჯდება ის პარამეტრები რომელიც გადაეცემა ფორმატ მეთოდს
# if - გამოიყენება რაღაც ლოგიკური პირობების შესამოწმებლად, if-ის მარჯვნივ იწერება ლოგიკური პირობა და მერე ორ წერტილი, ამ ლოგიკური პირობის მიღმა დგას ორნაირი ალტერნატივა ან True & False, თუ if-ის მარჯვნივ მდგომი პირობა არი True მაშინ შესრულდება მის ქვემოთ Tab-ით გამოყოფილ სიცრცეში არსებული ბლოკი თუარადა გადავა else-ში, else გულისხმობს ზემოთ ჩაწერილის გარდა ყველაფერს
# input - მეთოდით ჩვენ შეგვიძლია ტერმინალიდან შევიტანოთ რაღაც მნიშვნელობები რომელიც გაუტოლდება ცვლადის მნიშნვნელობებს
# type - გვიბრუნებს რა ტიპი არის მასში გადაცემული პარამეტრი
# ზრდის პროცესს ქვია ინკრემენტაცია (incrematation)
# Statement - if-ის ქვევით tab-ით გამოყოფილი სივრცე

# დავალება:
# მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
# აქედან მხოლოდ კენტები შეკრიბოს და დაბეჭდოს ჯამი

num1 = int(input("Enter Num1 : "))
num2 = int(input("Enter Num2 : "))
num3 = int(input("Enter Num3 : "))

# for each number if number kentia, 0  + number

sum = 0

if num1 % 2 == 1:
    sum += num1

if num2 % 2 == 1:
    sum += num2

if num3 % 2 == 1:
    sum += num3

# += დაემატება და გაუტოლდება ძველ ვერსიას

print ("The Sum Of Odd Numbers Is {}".format (sum))


a = 10
# a *= 3 # გამრაველბა
# a /= 5 # გაყოფა

print (a//3)

# // ჩამომჭრელი, ათწილადს ჩამოჭრის წერტილის მარჯვნივ რაცაა


# iteration - იტერაცია - განმეორება
my_name = "sandro"

# ამ შემთხვევაში char არის საიტერაციო ცვლადი (ცვლადს რომელიც მუდამ იცვლის მნიშნველობას ციკლის განმავლობაში)
# ცვლადი იწყება s-დან და მთავრდება o-ზე ხდება თითოეულის თავიდან გამოტანა სანამ საბოლოო ცვლადზე არ მივა
for char in my_name:
    print(char)

# i - საიტერაციო ცვლადი  და თითოეულ იტერაციაზე იძენს იმ მნიშვნელობას რა დიაპაზონიც არის აქ
# აქ იგულისხმება 0-დან 10-მდე
for i in range(10):
    print (i)

for i in range(10):
    print (str(i) + "s")

# თითოეულ დატრიალებაზე იძენს იმ მნიშვნელობას რომელზეც დგას




# მომხმარებელს შემოატანინე ორი სახელი და ის დამიპრინტე
# რომლის სახელშიც მეტი ხმოვანი იქნებაა

name1 = input("Enter Your Name1 : ")
name2 = input("Enter Your Name2 : ")

# vowels - ხმოვნები

amount_of_vowels_in_name1 = 0 # ცვლადი იწყება ნულით, მნიშვნელობა ექნება 0
amount_of_vowels_in_name2 = 0

for char in name1:
    if char in "aeiou": # char - ნაწილი, "aeiuo" მთლიანი
        amount_of_vowels_in_name1 += 1

for char in name2:
    if char in "aeiou":
        amount_of_vowels_in_name2 += 1

if amount_of_vowels_in_name1 > amount_of_vowels_in_name2:
    print ("The Amount Of Vowels In Name 1 Is More And It Contains {} vowels".format(amount_of_vowels_in_name1))

elif amount_of_vowels_in_name1 < amount_of_vowels_in_name2:
    print ("The Amount Of Vowels In Name 2 Is More And It Contains {} vowels".format(amount_of_vowels_in_name2))
else:
    print("They Have Equal Amount Of Vowels")


# else if --> elif

name1 = "sandro"
name2 = "giorgi"

if name1 == "giorgi":
    print ("giorgis ver shevadareb")
elif name2 == "giorgi":
        print("giorgis ver shevadareb")

else:   # თუ if შესრულდება გაჩერდება და არ გადაიტანს else
    if len(name1) > len(name2):
        print("pirveli upor grdzelia")

    elif len(name2) > len(name1):
        print ("meore upro grdzelia")

    else:
        print("tolia mati sigrdze")


# შემოიტანეთ რაღაც წინადადება და დაითვალეთ რამდემი "ა" გხვდება

text = input("Enter Your Text : ")
amount_of_a = 0

for char in text:
    if char == "a":
        amount_of_a += 1

# როცა print-ის შიგნით გვინდა ბრჭყალით გამოვყოთ რაიმე სიტყვა ან ასო ამ შემთხევაში ან კონკრეტულ სიტყვას დავწერტ ორი ბრჭყალით(" ") ან მხოლოდ ერთით (' )
print ('There is {} "a" in my text'.format (amount_of_a))