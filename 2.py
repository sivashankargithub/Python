old = "How$ are you ? Oh my God, you are bleeding! Let us go to the doctor quickly."
list1=['!','@','#','$','%','^','&','*','(',')','<','>','.',',','{','}','"','?']
new=''
len1=len(old)
len2=len(list1)
for j in range(0,73,1):    
    for i in range(0,len2,1):    
        if old[j]==list1[i]:
            old=old.replace(old[j],'')

print(old)
print(new)
