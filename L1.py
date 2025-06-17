import math
list_1=[1,2,3,4,5]
squar_list=[]
for i in list_1:
    squar_list.append(i**2)
for j in squar_list:
    if j%2==0:
        print(f"{j} which is square of ",math. sqrt(j)," is en even number")
    else:
        print(f"{j} which is square of ",math. sqrt(j)," is en odd number")
