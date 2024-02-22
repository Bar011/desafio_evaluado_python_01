#Ingreso de datos 

#Variable denominada "P" que corresponde al precio de la suscripción
P = int(input("Ingrese el precio de la suscripción, por favor ocupe sólo números: "))

#Variable denominada "U" que contiene el número de Usuarios
U = int(input("Ingrese el número de Usuarios totales, por favor ocupe sólo números: "))

#Variable denominada "Gt" que contiene el gasto total 

Gt= int(input("Ingrese el gasto total, por favor ocupe sólo números: "))

#Calculo de Uilidades 

Utilidades = P * U - Gt

print(f"El resultado de las utilidades es: {Utilidades}")