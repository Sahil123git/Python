with open("to_read_file.py",'rb')as file1:
    with open("Remove_comment_2.py",'wb')as file2:
        while True:
            b=file1.readline()
            if(chr(b[0])=='#'):
                pass
            elif (len(b)>2):
                print(len(b)," ",chr(b[0]))
                file2.write(b)
            else:
                break

