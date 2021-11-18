file=open("with_line.py","rb")#r for txt file and rb for binary files
print(file," File properties")
for line in file:
    print(line)
    