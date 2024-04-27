n = int(input())
s = set(map(int, input().split()))
a = int(input())
l1 = []
for i in range(a):
    b = list(map(str, input().split(" ")))

    l1.append(b)
print(l1)
for j in range(len(l1)):
    if l1[j]=="pop":
        l1[j].insert(1,0)

print(l1)