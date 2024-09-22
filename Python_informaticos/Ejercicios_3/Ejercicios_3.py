#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Mon Mar 23 21:15:59 2020

@author: MBI

Ejercicio 4.6 Reescribir el programa de  calculo de salario, con tarifa y media para horas
extras y cra una funcion llamada calculo_salario que reciba 2 parametros (Hora y Tarifo)
"""

# Main()
def calculo_salario(horas,tarifa):
    horas=float(horas)
    tarifa=float(tarifa)
    if horas > 40:
        salario= 40*tarifa +(horas-40)*(1.5*tarifa)
        print('Horas = {} Tarifa = {} Salario = {}'.format(horas,tarifa,salario))
    else:
        salario= horas*tarifa
        print('Horas = {} Tarifa = {} Salario = {}'.format(horas,tarifa,salario))
try:
    pedido= input('Ponga las horas seguido un epaacio y la tarifa por hora: ')
    p=pedido.find(' ')
    hora=pedido[:p]
    tarifa=pedido[p+1:]
    calculo_salario(hora,tarifa)
except :
    print('Introdusca solo numeros')


# In[ ]:


# Main()
def calcula_calificacion(nota):
    if nota >= 0.0 and nota <= 1:
        if nota > 0.9:
            print('Sobresaliente')
        elif nota > 0.8 :
            print('Notable')
        elif nota > 0.7 :
            print('Bien')
        elif nota > 0.6 :
            print('Suficinete')
        elif nota <= 0.6 :
            print('Insuficiente')
try:
    calificacion= float(input('Ponga la nota :'))
    calcula_calificacion(calificacion)
except :
    print('Introdusca solo numeros')

