num=["12345","12354"]
f=0
for i in range(len(num)-1):
    for j in range (len(num[i])):
        if(num[i][j]==num[i+1][j] and num[i][0]==num[i+1][0]):
            f+=1

print(f)


    