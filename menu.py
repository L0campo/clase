import os
os.system ("clear")

menuLogin=("""bienvenido al programa de ventas de productos
      1. registrese
      2. iniciar sesion
      3.  salir""")

menuinicio="""bienvenido al menú de inicio
1.compra
2.inventario
3.vender
4.utilidades
5.salir"""




isActive=True

while isActive:
    os.system("clear")
    print(menuLogin)
    opcion=int(input(" seleciones una opcion 1-3: "))
   
    match opcion:
        case 1: 
            os.system("clear")
            print("Registra tu usuario")
            user=input("ingresar nombre de usuario: ")
            password=input("ingrese una contraseña: ")
        case 2:
            os.system("clear")
            print("inicia seción")
            userLogin=input("ingrese su nombre de usuario: ")
            passwordLogin=input("ingrse su contraseña: ")
            if user==userLogin:
                print("user correcto")
                os.system("pause")
                os.system("clear")
            else:
                print("usario incorrecto")
            if password==passwordLogin:
                os.system("clear")
                print("inciaste secion correctamente")
                os.system("pause")
                os.system("clear")
                
                
                isActiveinicio=True
                while isActiveinicio:
                    os.system("clear")
                    print(menuinicio)
                    opcion=int(input("seleccione una opcion: "))
                    match opcion:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            pass
                        case 4:
                            pass
                        case 5:
                            isActiveinicio=False
                        case _:
                            print("opcion no válida")
                    

                
            else:
                print("contraseña incorrecta")
        case 3:
            print("Gracias por usar el programa")
            break
        case _:
            print("opcion no válida")
            
    
    
              
    

            
              
        
        
        
        
  






