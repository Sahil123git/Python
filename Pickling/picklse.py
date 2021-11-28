import emp,pickle
f=open("emp.dat","wb")
n=int(input("enter the number"))
for i in range(n):
    eid=int(input("enter"))
    name=input("enter teh name")
    sal=float(input("enter the sal"))
    e=emp.Emp_class(eid,name,sal)
    pickle.dump(e,f)#this will enter the data in emp.dat
    # print(type(e))
f.close()