from audioop import reverse
from posixpath import split
from collections import Counter


str="nikith"
print(str[:5])
print(str[::1])
print(str[-1:])
print(str[:-1])
print(str[::-1])


a=(1,2,3,4,5,6)

print(type(a))
print(a)
x=list(a)
print(x)


mydict ={"name":"nikith","age":28,"city":"new York"}
print(mydict)
mydict["email"]="nikithtankashala@gmail.com"
print(mydict)
#----deleting keys in dictionary
del mydict["email"]
print(mydict)
try:
    print(mydict["name"])
except:
    print("Error")    
for key in mydict.keys():
    print(key)
# for value in mydict.value():


myset=set()

myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
print(myset)
print(type(myset))
odds={1,3,5,7,9}
evens={0,2,4,7,8}
primes={2,3,5,7}
u=odds.union(evens)
print(u)
#intersection
#union
#update
#intersection_update
#difference_update

        

        
a="aaaabbbbbbbbbihccc"
my_counter=Counter(a)
print(my_counter)
print(my_counter.most_common(1))


for k in range(4,17,3):
    
    if k%3!=0:
        print(k)


def _hi_(m):
    return m*2
print(_hi_(2))  

def _hii_(g):
    return _hi_()*2
print(_hii_)    








