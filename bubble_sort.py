def bubblesort(lis):
    flag=1
    while(flag<len(lis)-1):
        for i in range(0,len(lis)-flag):
            if(lis[i]>lis[i+1]):
                temp=lis[i]
                lis[i]=lis[i+1]
                lis[i+1]=temp
        flag+=1
    return(lis)
test=[21,4,1,3,9,20,25,6,21,14]
print(bubblesort(test))
