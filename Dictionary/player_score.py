score={"Vk":[10,40,2,12,40,60,70,14,80,40],
"Rs":[10,40,20,12,40,60,70,14,80,40],
"Ms":[10,40,2,72,40,60,70,14,80,40],
"Ar":[10,40,2,12,48,60,70,14,80,40],
"Cg":[10,40,2,12,40,80,70,14,80,40]}
 
ans={}
man_of_match=''
maxi=0
sum
for item,value in score.items():
    sum=0
    for i in value:
        sum+=i;
    # print(sum)
    ans[item]=sum #putting sum of all the values in ans dictionary
    
    if(maxi<sum):#changing maxi and storing sum
        maxi=sum
        man_of_match=item
        # print(maxi)
        
print(ans)
print("Man of the series is ",man_of_match,"with total score =",maxi)