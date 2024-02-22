#importación libreria math para facilitar manejo de operaciones matemáticas
import math 

#variables

r = int(input("Ingrese el Radio en Kilometros: "))
g = float(input("ingrese la constante G en (m/seg^2): "))


#Pasar de Km a metros

r = r*1000
#calculo de la velocidad de escape

Ve =math.sqrt( 2* g * r) 

#redondeo de decimales

resultado = round(Ve,2)

print((f"La velocidad de escape es {resultado} m/s"))