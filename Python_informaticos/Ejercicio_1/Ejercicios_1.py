#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""


Ejercicio 2.3 . Escribir un programa para pedirle al ususrio
el numero de horasy la tarifa por hora para calcular el salario
bruto
"""

pedido= input('Introdusca las horas, seguidas de un , la tarifa:' )
hora=0
tarifa=0
coma=','
pos=pedido.find(coma)
hora=pedido[:pos]
tarifa=pedido[pos+1:]
salario_bruto=float(hora)*float(tarifa)
print('Horas = {} Tarifa= {} Salario = {}'.format(hora,tarifa,salario_bruto))


# In[2]:


"""Ejercicio 2.4  Asume que se ejecutamos las siguientes sentencias de asignacion
escribe el valor de la expresion y su tipo
"""
ancho= 17
alto= 12.0

print(ancho/2 ," " ,type(ancho/2))

print(ancho/2.0 ,'  ' , type(ancho/2.0))

print(alto/3 ,'  ' ,type(alto/3))

print(1+2*5 ,'  ' ,type(1+2*5))


# In[3]:


"""
Ejercicio 2.5 Escribe un programa que convierta una temperatura en grados Celsius a grados Fahrenheit

"""
temperatura = float(input('Introdusca una temperatura en grados Celsius:'))
tempeconvertida= (temperatura*1.8)+32
print('Celsius -> Fahreneheit= {}'.format(tempeconvertida))


# In[ ]:




