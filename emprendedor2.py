#Ingreso de datos 

#Variable denominada "P" que corresponde al precio de la suscripción
P = int(input("Ingrese el precio de la suscripción, por favor ocupe sólo números: "))

#Variable denominada "Up" que contiene el número de Usuarios Premium
Up = int(input("Ingrese el número de Usuarios Premium, por favor ocupe sólo números: "))

#Variable denominada "Un" que contiene el número de Usuarios Normales
Um = int(input("Ingrese el número de Usuarios Normales, por favor ocupe sólo números: "))

#Variable denominada "Gt" que contiene el gasto total 

Gt= int(input("Ingrese el gasto total, por favor ocupe sólo números: "))
#recargo del 50% a los usuarios premium 

Ump = Up * 1.5*P

#Calculo de Usuarios normales 
Umn = Um * P 

print(f"Ganancia por Usuarios Premium:  {Ump}")
print(f"Ganancia por Usuarios Normales:{Umn} ")

#Calculo de Uilidades 

Utilidades = (Ump + Umn) - Gt

print(f"El resultado de las utilidades es: {Utilidades}")