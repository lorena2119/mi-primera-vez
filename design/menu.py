from logic.formula import hi
def design():
    print("Bienvenido(a) al mejor sistema del mundo")
    print("     0. Atrás")
    print("     1. ¿Desea que nuestra máquina lo salude?")
    opc=int(input("Elija una de las opciones disponibles: "))
    if opc == 1:
        name=(input("Ingrese su nombre: "))
        resultado=hi(name)
        print(resultado)
    return opc    
