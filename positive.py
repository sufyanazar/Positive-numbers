list1=[]
n=int(input("Enter length of list :"))
print("Enter elements \n")
for i in range(0,n):
    x=int(input())
    list1.append(x)
list2=[]
for j in list1:
    if(j>0):
        list2.append(j)
print(list2)
