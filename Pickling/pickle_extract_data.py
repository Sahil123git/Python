import emp,pickle
f=open("emp.dat","rb")

print("emp detail")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("end of file is reached")
        break
