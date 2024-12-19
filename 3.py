old = "How$ are you ? Oh my God, you are bleeding! Let us go to the doctor quickly."
list1=['!','@','#','$','%','^','&','*','(',')','<','>','.',',','{','}','"','?']

for i in range(0,len(list1),1):    
    if list1[i] in old:
        old=old.replace(list1[i],'') 
print(old)
