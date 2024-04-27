def square(number):
    return number*number

print(square(0))

try:
    age=int(input('Age:'))
    income=20000
    risk=income/age
    print(risk)
except ZeroDivisionError:
     print('Age cannot be zero')    
except ValueError:
    print("invalid value")

print("Sky is blue")













