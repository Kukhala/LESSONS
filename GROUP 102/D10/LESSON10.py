# # surname = "kukhaleishvili"

# # print(surname[1:-1])

# my_str = "nika 11 kesheleva"

# print(my_str[5]+"5")


def reverse_arr(any_arr):

    new_arr = []

    i = len(any_arr)

    while i > 0:
        new_arr.append(any_arr[i-1])
        i -= 1

    print(new_arr)




students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva",]
reverse_arr(students)
