
def compute(a,b,c):
    res = 0
    ttl={0:'Результат сложения', 1: 'Результат вычитания',\
         2:'Результат умножения', 3:'Результат деления', 4:\
             'Введите другое действие'}
    if c == '+': 
        res=a+b 
        t=ttl[0]
    elif c=='-': 
        res=a-b
        t=ttl[1]
    elif c=='*': 
        res=a*b
        t=ttl[2]
    elif c=='/': 
        res=a/b
        t=ttl[3]
    else:
        res=0
        t=ttl[4]
    
    return [res, t]

