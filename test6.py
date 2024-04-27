phone= input("phone")
num1={"1":"one","2":"two","3":"three","4":"four",

}
output=""
for ch in phone:
    output+=num1.get(ch,"!")+" "

print(output)









