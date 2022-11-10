#Elean Rivas
#Teoría de la computación


#Funciones lamda
alpha = lambda x: x + 1
beta = lambda x: 2*x
zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))

succesor = (lambda n: lambda f: lambda x: f(n(f)(x)))
#aqui pueden cambiar los parametros unicamente se puede con zero, one, two
addition = (lambda m: lambda n: lambda f: lambda x: n(f)(m(f)(x)))
product = (lambda m: lambda n:lambda f: lambda x: n(m(f))(x))   
potency = (lambda m: lambda n:lambda f: lambda x: n(m(f))**(x))