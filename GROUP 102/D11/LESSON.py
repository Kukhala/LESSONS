def find_index_of_chars(any_str, any_char):
    arr_of_indexes = []

    i = 0 

    while i < len(any_str):
        if any_str[i] == any_char:
            arr_of_indexes.append(i)

        i += 1
    
    print(any_char, " gvxvdeba", arr_of_indexes, " adgilebze")


print(find_index_of_chars("sandro kukhaleishvili", "a"))