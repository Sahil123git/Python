def sep_vow(str1):
    str2=""
    for i in str1:
        if i in "aeiouAEIOU":
            pass
        else:
            str2+=i
            
    return str2

str=input("Enter the string\n")
print(sep_vow(str))

