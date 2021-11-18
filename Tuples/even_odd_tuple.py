ty1=(1,2,-1,8,3)

tye=()
tyo=()
for i in ty1:
    if(i%2==0):
        tye=tye+(i,)
    else:
        tyo=tyo+(i,)
        
print(tye,"Even no")
print(tyo,"odd no")