#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Sat Mar 21 20:57:15 2020

@author: MBI

Ejercicio 3.1 Reescribir el programa de clalculo  del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40
"""
# Main()
pedido = input('Introdusca su horas y tarifa separados por un espacio: ')
horas=0
tarifa=0
po=pedido.find(' ')
horas = pedido[:po]
tarifa = pedido[po+1:]
salario=0
if float(horas) > 40:
    horas_ex= float(horas)-40
    salario= 40*float(tarifa)+horas_ex*(1.5*float(tarifa))
else:
    salario=float(horas)*float(tarifa)

print('Horas = {} Tarifa = {} Salario = {}'.format(horas,tarifa,salario))


# In[ ]:


"""
Ejercicio 3.2 Rescribir el programa anterior usando  try  y except
"""
# Main()
print('Introdusca horas y tarifas a continuacion: ')
try:
    horas=float(input())
    tarifa=float(input())
    
    if float(horas) > 40:
        horas_ex= float(horas)-40
        salario= 40*float(tarifa)+horas_ex*(1.5*float(tarifa))
    else:
        salario=float(horas)*float(tarifa)

    print('Horas = {} Tarifa = {} Salario = {}'.format(horas,tarifa,salario))
except :
        print('Ponga solo numeros')
        


# In[ ]:


"""
Ejercicio 3.3 Escribe un programa que solicite una puntuacion entre 0.0 y 1.0 . Si la puntuacion
esta fuera de ese rango, muestra un mensaje de error.Si la puntuacion esta entre 0.0 y 1.0 muestra la calificacion
usando la tabla siguiente
"""  
# Main()

for i in range(0,4):
    try:
        puntuacion= float(input('Introdusca un a puntuacio entre 0.0 y 1.0: '))
        if puntuacion >= 0.0 and puntuacion <=1: 
            if puntuacion >= 0.9 :
                print('Sobresaliente')
            elif puntuacion >= 0.8 :
                print('Notable')
            elif puntuacion >= 0.7 :
                print('Bien')
            elif puntuacion >= 0.6 :
                print('Suficiente')
            elif puntuacion < 0.6 :
                print('Insuficiente')
        else:
           print('Valor fuera de rango')
    except :
            print('Puntuacion incorrecta')

