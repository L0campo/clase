import os
os.system ("clear")

peso=float(input("ingrese su peso "))
altura=float(input("ingrese su altura "))

indice_masa_corparal=peso/(altura**2)

match indice_masa_corparal:
    case _ if indice_masa_corparal<18.5:
        print(f"su imd es falta de peso {indice_masa_corparal:.2f}")
    case _ if indice_masa_corparal>=18.5 and indice_masa_corparal<=24.9:
        print(f"su imd es normal {indice_masa_corparal:.2f}")
    case _ if indice_masa_corparal>24.9 and indice_masa_corparal<=29.9:
        print(f"su imd es de sobrepeso {indice_masa_corparal:.2f}")
    case _:
        print(F"su imd es de gordo {indice_masa_corparal:2f}")
    

    



