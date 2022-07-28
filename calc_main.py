# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.

# В рамках этого обсуждения студентам надо нарисовать “архитектуру” (например, в виде блок-схемы)
# для работы данного приложения.


import calc_in as ci
import calc_operations as co
import calc_print as cp
import calc_log as cl

def button_start():
    a,b,c=ci.inlet()
    r=0
    
    r=co.compute(a,b,c)
    cp.output(r)
    d=[a,b,r[1],r[0]]
    cl.calc_logger(d)

button_start()
