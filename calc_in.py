
def inlet():
    a2=0
    b2=0
### ввод a
    a = input('a = ')
    flag=0
    for i in a:
        if i.lower()=='j':
            flag+=1
        
    if flag<1:
        a2=float(a)
    else:
        a2=complex(a)
### ввод b        
    b = input('b = ')
    flag=0
    for i in b:
        if i.lower()=='j':
            flag+=1
        
    if flag<1:
        b2=float(b)
    else:
        b2=complex(b)
### ввод c
    c = str(input('действие '))
   
    return [a2, b2, c]