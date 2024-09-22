#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Fri Mar 27 21:12:50 2020

@author: MBI
Ejercicio 8.2 Crea un archivo de texto que haga que el programa siguiente falle y despues arregla el fallo.
"""
#%%
# Main()
archivo=open('C:/Users/MBI/Documents/Spider_Scripts/Ejercicios_del_Curso_Python _para_Informaticos/Ejercicios_7/mbox-short.txt')
for linea in archivo:
    palabra=linea.split()
    if len(palabra)==0 :continue
    if palabra[0] !='From': continue
    print(palabra[2])
#%%
"Solucion : El programa falla  si la linea no esta vacia y empieza  con from pero en la supuesta posicion 2  esta vacia"
# Main()
archivo=open('C:/Users/MBI/Documents/Spider_Scripts/Ejercicios_del_Curso_Python _para_Informaticos/Ejercicios_7/datos.txt')
for linea in archivo:
    palabra=linea.split()
    if len(palabra)!=0 and palabra[0] =='From' and  len(palabra)>2: 
        print(palabra[2])
#%%
"Ejercicio 8.3 Reescribe el codigo anterior usando solo una sentencia if con el operador and"
# Main()
archivo=open('C:/Users/MBI/Documents/Spider_Scripts/Ejercicios_del_Curso_Python _para_Informaticos/Ejercicios_7/datos.txt')
for linea in archivo:
    palabra=linea.split()
    if len(palabra)!=0 and palabra[0] =='From' and  len(palabra)>2: 
        print(palabra[2])
    else: continue
#%%
"""Ejercicio 8.4 Escribe un programa que habra el archivo  romeo.txt  y lo lea linea a linea . Para cada linea
, dividela en una lista de palabras usando la  funcion split .
Para cada palabra , mira a ver si esa palabra ya existe en la lista. Si no es asi añadela."""
from collections import Counter
# Main()
archivo_romeo= 'C:/Users/MBI/Documents/Spider_Scripts/Ejercicios_del_Curso_Python _para_Informaticos/Ejercicios_7/romeo.txt'
palabra=[]
try:
    with open(archivo_romeo,'r') as fname:
        for linea in fname:
            palabra.append(linea.split())
    
        fname.close()
except :
    print('No se pudo abrir el archivo')

new_lista=[]
for i in palabra:
    for x in i:
        new_lista.append(x)
        
texto=Counter(new_lista)
lista_ordenada=texto.keys()
lista_ordenada=list(lista_ordenada)
lista_ordenada.sort()
print(lista_ordenada)


# In[ ]:



"""Ejercicio 8.5 Escribe  un programa que lea a traves de los datos de un buzon de correo,
y cunado encuentre una  linea que empiece por From , la divida en palabras y muestre el remitente y cuantas lineas con 
From hay y sin From"""

# Main()
buzon='mbox-short.txt'
conteo_From=0
conteo_NoFrom=0
lista=[]
try:
    with open(buzon,'r') as fname:
        for linea in fname:
            if len(linea)!=0 and linea.startswith('From'):
                conteo_From=conteo_From+1
                linea_tem=linea.split()
                lista.append(linea_tem[1])
            else:
                    conteo_NoFrom=conteo_NoFrom+1
        fname.close()
except :
    print('No se encontro el archivo')

for x in lista:
    print(x)

print('Hay {} lineas en el archivo  con From comoprimera  palabra y {} sin from para un total {}'.format(conteo_From,conteo_NoFrom,(conteo_From+conteo_NoFrom)))


# In[ ]:


"""Ejercicio 8.6 Reescribe el programa que pide al usuario una lista de numeros e imprime el maximo y el minimo de los numeros introducidos al final
cuando el usuario introdusca fin"""
# Main()

verdadero=True
lista_numeros=[]
while verdadero:
      numero=(input('Ponga numero: '))
      if numero == 'fin':
          verdadero=False
      else:
            try:
                lista_numeros.append(int(numero))
            except :
                print('Ponga solo numeros')
                continue


print('El minimo {} , El maximo {} '.format(min(lista_numeros),max(lista_numeros)))  

