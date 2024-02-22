#Ingreso de datos 
import math
#Variable denominada "P" que corresponde al precio de la suscripción
P = float(input("Ingrese el precio de la suscripción, ocupe sólo números: "))

#Variable denominada "U" que contiene el número de Usuarios
U = float(input("Ingrese el número de Usuarios totales, ocupe sólo números: "))

#Variable denominada "Gt" que contiene el gasto total 

Gt= float(input("Ingrese el gasto total en números: "))

#Variable denominada "Ua" Que corresponde a las utilidades del Año anterior

Ua= float(input("Ingrese las Utilidades del año anterior, sólo números: "))

#Calculo de Uilidades 

Utilidades = P * U - Gt

#Razon entre las Utilidades actuales y las del año anterior

Razon =str(round((Utilidades*100/Ua),2)) + '%'

print(f"La razón entre las utilidades actuales y las del año anterior es : {Razon}")