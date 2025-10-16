#9. Pide un número y muestra su tabla de multiplicar")
numero = int(input(f"Ingrese el número para conocer sus múltiplos:"))
print(f"Tabla de multiplicar de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")         
                              
                              
                                                
                              
#20. Simula una calculadora (suma, resta, multiplicación, división).")
                             
                                                        
num1 =int(input("ingrese su numero 1 "))
num2=int(input("ingrese su numero 2  "))
operacion = input("ingrese su operacion(+ - * /):")
resultado= 0

if operacion == "+":
    resultado=num1+num2
elif operacion== "-":
    resultado=num1-num2 
elif operacion== "+":
    resultado=num1*num2 
elif operacion== "/":
    resultado=num1/num2 
else:
    print("ingrese una operacion valida")

print(f"el resultado de {num1} {operacion} {num2} = {resultado} ")
