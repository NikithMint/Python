def timeconversion(x):
    if x<=0:
        print("please enter a positive number")
    elif x<=12:
        print(x)
    elif x==13:
        print("1")
    elif x==14:
        print("2")
    elif x==15:
        print("3")
    elif x==16:
        print("4")
    elif x==17:
        print("5")
    elif x==18:
        print("6")
    elif x==19:
        print("7")
    elif x==20:
        print("8")
    elif x==21:
        print("9")
    elif x==22:
        print("10")
    elif x==23:
        print("11")
    elif x==24:
        print("12")
                                                        

x=int(input("enter a number"))    

if x>=0 and x<=24:
    timeconversion(x)
else:
    print("enter numbers between 1 to 24")    