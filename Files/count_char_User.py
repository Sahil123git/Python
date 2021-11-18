fname=input("enter the file name with extension")
file=(open(fname,'r'))#by default read mode
file_read=file.read()#this will read whole file content in characters
print(file_read)
count=0
char= input("enter the character you want to search")

for let in file_read:
    # print(let," ")
    if let==char:
        count+=1
        
print(count)