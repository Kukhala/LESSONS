# დავალება:
# ინფუთით შევიტანოთ სახელი და გვარი
# ტერმინალში გამოვიყვანოთ რომელი ინდექსზე არის ხმოვნები

# sandro kukhaleishvili

full_name = input ("Enter Your Name: ")

i = 0
while i < len(full_name):
    if full_name[i] in "aeiou":
        print (str(i) + " - " + full_name [i])
    i += 1



