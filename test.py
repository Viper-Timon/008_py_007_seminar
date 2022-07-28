
a=input('a = ')
for i in len(a):
    flag=0
    if a[i].isdigit()==False:
        flag=1
    
if flag==0:
    a2=float(a)
else:
    a2=complex(a)
    
