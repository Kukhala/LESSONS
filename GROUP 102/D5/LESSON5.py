for i in range (7): # i საიტერაციო ცვლადი, range - ჩაშენებული(7) ფუნქცია 0-დან 7მდე
    print ("sandro")

for i in range (7-3): # იგივე რაც ზემოთ
    print ("sandro")

for i in range (len("sandro")): # იგივე რაც ზემოთ, ხედავს არა სახელს არამედ 6-იანს ინტეჯერს რადგან ჯამი 6ია ასოების
    print ("sandro")

for i in range (3,6): # range(3,6) = -,1,2,3,4,5,6
    print ("sandro")

for i in range (3,6): 
    print (str(i), "sandro") # i-დან იღებს თითოეულ რიცხვს და უწერს sandro-ს

for i in range (5,10,2):
    print (str(i) + " sandro")

# range-ს გადაეცემა სამი პარამეტრი, ერთი ორი და სამი

i = 0 # საიტერაციო რიცხვი საჭიროა თავში
while i < 5:
    print ("sandro")
    i += 1 # საიტერაციო რიცხვის ინკრემეტაცია საჭიროა ბოლოში რათა დასრულდეს და არ გაგრძელდეს უსასრულოდ

while i < 5:
    print ("sandro")
    print (i)
    i += 1 
    
full_name = "sandro kukhaleishvili"

i = 0
while i < len(full_name):
    print (full_name[i])
    i += 1


# დავალება :

# a = "qwerty"
# b = "asdfgh"
# დაიპრინტოს
# qa
# ws
# ed
# rf
# tg
# yh

a = "qwerty"
b = "asdfgh"

i = 0
while i < len(a):
    print (a[i] + b[i])
    i += 1


# range - დიაპაზონი დან-მდე
if 10 > 5 and 3 > 1:
    print ("cool")

if 10 > 5 or 3 > 5:
    print ("cool")


# and ამოწმებინებს ორივეს "და" კავშირი
# and -კავშირში თუ ორივე არის სწორი True გამოდის თუ რომელიმე არის არასწორი False
# or - "ან" კავშირი თუ რომელიმე მაინც არის სწორი გამოქვს
# not - False-ს ატრიალებს True-თ ან პირიქით
# break - აჩერებს პროგრამას კონკრეტული შემთხვევის დროს
# continue - გადახტომა

i = 0
while i < 10:
    print (i)
    i += 1

    if i == 5:
        break


