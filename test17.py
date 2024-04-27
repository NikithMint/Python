from unittest import result
import re

li=[]
name=input("enter a string : ")
for j in name:
    li.append(j)
print(li)
if "a" in li or "e" in li or "i" in li or "o" in li or "u" in li:
    print("String contains vowels")
else:
    print("string does not contains vowels")




# a=int(input("enter a number"))
# for i in range(4):
#    k= a*a*a
# print(k)    




inp_str="helloabchello"
result=re.match(r"[abc]",inp_str)
print(result)


imp_str="film Titanic was released in 1998"
result=re.search(r"[was]",imp_str)
print(result)


#-------multiplication Table-------
x=int(input("enter a number "))
k=0
for i in range(1,11):
    print("5 x ",i, "=" , x*i)


    
    






        
    
    

        



        

