#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Tue Mar 24 21:20:01 2020

@author: MBI

Ejercicio 5.10 Escriba un programa que lea repetidamente numeros hasta que el usuario introduzca fin
Una vez se haya introducido fin, muestra  por pantalla el total, la cantidad de numeros y la media de esos numeros.
Si el usuario introduce cualquier otra cosa que no sea un numero, detecta su fallo y muestra un mensaje de error y pasa 
al siguiente numero.
"""

# Main()
def operaciones(to,can,me):
    me=to/can
    print('Total = {} Cantidad = {} Media = {}'.format(to,can,me))
    
    
fin=True
total=0
cantidad=0
media=0
while fin :
    numero= input('Introdusca numero: ')
    if str.lower(numero)== 'fin':
        fin=False
    else:
        try:
            numero_int=int(numero)
            cantidad= cantidad+1
            total += numero_int
        except:
            print('Dato erroneo')
            
operaciones(total,cantidad,media)        


# In[1]:



"""
Ejercicio 5.2 Escribe otro programa que pida una lista de numeros como la anterior y al final muestre  por pantalla
el maximo y el minimo de los numeros, en vez de la media

"""
# Main()
import timeit
def maximominimo(lista,minimo,maximo):
    minimo=lista[0]
    for m in lista:
        if minimo > m :
            minimo=m
        else:
            minimo=minimo
    for n in lista:
        if maximo < n:
            maximo=n
        else:
            maximo=maximo
    print('Maximo = {} Minimo = {}'.format(maximo,minimo))
    
fin= True
maximo=0
lista=[]
minimo=0
while fin:
     numero= input('Introdusca numero: ')
     if str.lower(numero)== 'fin':
        fin=False
     else:
         try:
             numero_int=int(numero)
             lista.append(numero_int)
         except :
             print('Dato erroneo')

maximominimo(lista,minimo,maximo)
print(timeit.timeit())


# In[2]:


"""Variante mas facil"""
# Main()
import timeit
 
fin=True
lista=[]
while fin:
     numero = input('Introdusca numero: ')
     if str.lower(numero)== 'fin':
        fin=False
     else:
         try:
             numero_int=int(numero)
             lista.append(numero_int)
         except :
             print('Dato erroneo')

print('Maximo = {} Minimo = {}'.format(max(lista),min(lista)))
print(timeit.timeit())


# In[ ]:




