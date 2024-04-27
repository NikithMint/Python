# n=int(input())
# li=[]
# for i in range(n):
#     a=list(map(int,input().split(" ")))
#     li.append(a)
#     if len(li)==n:
#         break
# for m in li:
#     for k in range(1):
#         if m[0]==m[1]:
#             print("Yes")
#         elif m[0]+1==m[1]-1:
#             print("yes")
#         elif m[0]-1==m[1]+1:
#             print("yes")
#         else:
#             print("No")

# cook your dish here
li=["a","e","i","o","u"]
lii=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
ki=[]
s="apple"
for letter in s:
    ki.append(letter)
    
for i in range(21):
    for j in range(len(ki)):
        if ki[j]==lii[i]:
            print("YES")
        else:
            print("NO")
                

     
        
    