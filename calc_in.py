
def inlet():
    a2=0
    b2=0
### ввод a
    a = input('a = ')
    for i in a:
        flag=0
        if a.isdigit()==False:
            flag=1
        
    if flag==0:
        a2=float(a)
    else:
        a2=complex(a)
### ввод b        
    b = input('b = ')
    for i in b:
        flag=0
        if b.isdigit()==False:
            flag=1
        
    if flag==0:
        b2=float(b)
    else:
        b2=complex(b)
### ввод c
    c = str(input('действие '))
   
    return [a2, b2, c]