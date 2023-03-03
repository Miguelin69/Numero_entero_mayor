# Desarrollo numero mayor

n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
n3 = int(input("Digite el  tercer numero: "))

if n1 > n2 and n1 > n3:
    print("El numero mayor es: ",n1)
elif n2 > n1 and n2 > n3:
    print("El numero mayor es: ",n2)
elif n3 > n2 and n3 > n1:
    print("El numero mayor: ",n3)
else: 
    print("NO SE PUDO ESTABLESER EL MAYOR")