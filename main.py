#Operadores Lógicos and or not
edad=int(input("Ingrese su edad: "))

#if(edad>= 18 and edad<=20 or edad>=24 and edad<=30 or edad>=34 and edad<=45):
#   print("Credito como pasante")

if(edad == 17):
    print("Puede solicitar un crédito como pasante")

elif(edad<20 and edad>=18):
    print("Puede solicitar un crédito")  

elif(edad<=24 and edad>=20):
     print("Puede solicitar un crédito y bono")      


else:
    print("No puede solicitar un crédito.")