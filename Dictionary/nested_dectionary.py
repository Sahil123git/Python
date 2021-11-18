score={"Vk":{10,40,2,12,40,60,70,14,80,40},
"Rs":{10,40,2,12,40,60,70,14,80,40},
1:"sd"}
 
for key in score:
     print(key,end="")
print()
for value in  score.values():
    print(value,end="")
print()
for key,value in score.items():
    print(key," ",value)
    # for i in value:
    #     print(i)


