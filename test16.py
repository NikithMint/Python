def myGenerator():
   print('First item')
   yield 10
   print('Second item')
   yield 20
   print('Last item')
   yield 30

# # gen = myGenerator
# # print(next(gen))

# #--------------------------------------------------------
# def fibonacci(max):
#     a,b=0,1
#     while a < max:
#         yield a
#         a,b=b,a+b
# fib=fibonacci(5)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# #-------------------------------------------------

# obj=["Even" if i%2==0 else "odd" for i in range(10)]
# print(obj)

# #-------------------------------------------------

# number_list=[x for x in range(20) if x%2==0]
# print(number_list)

# #-------------------------------------------------



# li=[]
# name=input("enter a string : ")

# li.extend(name)
# print(name[1])
# count=0
# for i in name:

#     if "a" == i or "e" == i or "i" == i or "o" == i or "u" == i:
#         print("String contains vowels")
#     else:
#         count= count + 1
# print(count)        
        
  





