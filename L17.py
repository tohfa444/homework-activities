dict={"english":90,"math":95,"bangla":64,"biology":80,"history":54,"Chemistry":90,"physics":90,"higher_math":90}
k=90
res=0
for key in dict:
    if dict[key]==k:
        res+=1
print("The frecuency of k is",res)