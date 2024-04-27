l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=['0','1','2','3','4','5','6','7','8','9']
l3=['@','#','%','&','?']
l4=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l5=[]
a=int(input())
for i in range(a):
    b=list(input())
    l5.append(b)
print(l5)
for j in range(len(l5)):
    if len(l5[j])>=10:
        count=0
        count1=0
        count2=0
        count3=0
        for v in l5[j]:
            for k in l1:
                if v==k:
                    count=count+1
            for m in l2:
                if v==m:
                    count1=count1+1
            for n in l3:
                if v==n:
                    count2=count2+1
            for o in l4:
                if v==o:
                    count3=count3+1  
        print(count)
        print(count1)
        print(count2)
        print(count3)         
        if count>=1 and count1>=1 and count2>=1 and count3>=1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")     

                                     
