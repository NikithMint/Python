for item in ["nikith","mint","hello"]:
    print(item)

for item in range(5,10,2):
    print(item)

prices=[10,20,30]
sum=0
for i in prices:
    sum=i+sum
print(sum)    
 
 
for x in range(4):
    for y in range(3):
        print(f'({x},{y})') 

numbers=[5,2,5,2,2]
for i in numbers:
    print("x"*i )


numbers=[6,3,15,10,3,2]
max = numbers[0]
for number in numbers:
    if number > max:
        max=number
print(max)          
        
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]        
for i in matrix:
    for j in i:
       print(j) 



numbers.insert(10)
print(numbers)


