def funcion_1(a, b, c):
    a=b-c*a
    b=c
    c=a
    b=c
    print("4. Valor de la variable (b):"+  str(b))

def funcion_2(x, y, z):
    a=x
    b=y
    c=y

    a=b**z + c
    b=c
    print("3. Valor de la variable (a):"+  str(a))
    return a

def funcion_3(m, n, l):
    a=m
    b=n
    c=l
    a=b-c
    b=c
    return a

def funcion_4(a, x, m):
    b=x
    c=m
    c= b+c
    b=c
    return b

def principal():
    a=1
    b=2
    c=3
    m=4
    n=5
    l=6
    x=7
    y=8
    z=9
    funcion_1(x, y, z)
    funcion_2(a, b, c)
    print("1. Valor de la variable (a):"+  str(a))
    b=funcion_3(a, b, c)
    print("2. Valor de la variable (b):"+  str(b))
    c=funcion_4(m, n, l)
    print("5. Valor de la variable (c):"+  str(c))

if __name__=='__main__':
    principal()