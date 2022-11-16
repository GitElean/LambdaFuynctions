# Teoría de la computación
#Elean Rivas
# 19062

# Proyecto 2: Funciones lambda


def test(s):
    print (s, ' = ', eval(s))

operator = lambda x: x + 1
function = lambda n: n(operator)(0)

zero = lambda f: lambda x: x
one   = lambda f: lambda x: f(x)
two   = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))

alpha = lambda x: x+1
beta = lambda x: 2*x

menu = True
while(menu == True):
   while(menu == True):
    print("""
1) f(x)=x+1  					2) g(x)=2x
3) cero(f,x)=λf.λx.x            4) uno(f,x)=λf.λx.fx
5) dos(f,x)=λf.λx.ffx           6) tres(f,x)=λf.λx.fffx	
7) sucesor(𝑛,f,x)=λ𝑛.λf.λx(f(𝑛f(x)))
8) suma(a,b,f,x)				9) multiplicaicion(a,b,f,x)
10) Potencia(a,b,f,x)			0) Salir

							""")
    option = input("Seleccione una opcion ")
    if(option == "1"):

        #Ejercicio 1 


        alpha = lambda x: x+1

        print(" 𝑓(𝑥) = 𝑥+1 " )
        a = int(input("ingrese el valor de x: "))
        print("resultado  " + " " + str(alpha(a)))


        break

    elif(option == "2"):

        #Ejercicio 2

        beta = lambda x: 2*x

        print("𝑔(𝑥) = 2𝑥 ")
        a = int(input("ingrese el valor de x: "))
        print("resultado  " + " " + str(beta(a)))

        break

    elif(option == "3"):

        #Ejercicio 4


        zero = lambda f: lambda x: x
        print("𝑐𝑒𝑟𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑥")
        test("function(zero)")
        break

    elif(option == "4"):

        #Ejercicio 5
        print("𝑢𝑛𝑜(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑥")
        one   = lambda f: lambda x: f(x)
        test("function(one)")

        break

        
    elif(option == "5"):

        #Ejercicio 6


        print("𝑑𝑜𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑥")
        two   = lambda f: lambda x: f(f(x))
        test("function(two)")

        break

    elif(option == "6"):

        #Ejercicio 7 


        print("𝑡𝑟𝑒𝑠(𝑓,𝑥)=𝜆𝑓.𝜆𝑥.𝑓𝑓𝑓𝑥")
        three = lambda f: lambda x: f(f(f(x)))
        test("function(three)")
        break

    elif(option == "7"):

        #Ejercicio 8


        zero = lambda f: lambda x: x
        one   = lambda f: lambda x: f(x)
        two   = lambda f: lambda x: f(f(x))
        three = lambda f: lambda x: f(f(f(x)))

        suc = (lambda n: lambda f: lambda x: f(n(f)(x)))
        print("𝑠𝑢𝑐𝑒𝑠𝑜𝑟(𝑛,𝑓,𝑥)=𝜆𝑛.𝜆𝑓.𝜆𝑥(𝑓(𝑛𝑓(𝑥)))")
        
        print("Sucesor de 0")
        test("function(suc(zero))")

        print("Sucesor de 1")
        test("function(suc(one))")

        print("Sucesor de 2")
        test("function(suc(two))")

        print("Sucesor de 3")
        test("function(suc(three))")
        break

    elif(option == "8"):

        #Ejercicio 9


        print("𝑠𝑢𝑚𝑎(𝑎,𝑏,𝑓,𝑥)")
        
        
        addition = (lambda m: lambda n: lambda f: lambda x: n(f)(m(f)(x)))
        #aqui pueden ca,biar los parametros unicamente se puede con zero, one, two y three
        test("function(addition(three)(two))")

        break

    elif(option == "9"):

        #Ejercicio 10


        print("𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑐𝑎𝑐𝑖io𝑛(𝑎,𝑏,𝑓,𝑥)")
        product = (lambda m: lambda n: 
        lambda f: lambda x: n(m(f))(x))
         #aqui pueden ca,biar los parametros unicamente se puede con zero, one, two y three
        test("function(product(three)(one))")

        break

    elif(option == "10"):
        print("potencia(𝑎,𝑏,𝑓,𝑥)")
        potency = (lambda f: lambda x: (f)(x))
        test("function(potency(three)(two))")

        break

    elif(option == "0"):
        menu = False
        print("Bye")