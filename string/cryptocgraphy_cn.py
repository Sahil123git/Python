str=input("enter the string")
key=int(input("enter the key"))

j=len(str)
for i in str:
    print(chr(ord(i)+key))