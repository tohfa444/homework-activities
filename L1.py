import math
list_1=[1,2,3,4,5]
squar_list=[]
for i in list_1:
    squar_list.append(i**2)
for j in squar_list:
    if j%2==0:
        print(math.sqrt(j)," which is the square root  of ",{j}," is en even number")
    else:
        print(math.sqrt(j)," which is the square root of ",{j}," is en odd number")

