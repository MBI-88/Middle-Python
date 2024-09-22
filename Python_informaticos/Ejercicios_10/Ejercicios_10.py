#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Sun Apr  5 16:01:03 2020

@author: MBI
Ejemplos del uso de expresiones regulares
"""
#%%
import re
# Main()
archivo=input('Ponga archivo a abrir:')

try:
    with open(archivo,'r') as fname:
        for linea in fname:
            linea.rsplit()
            x=re.findall('\w\S*@\S*[a-z]',linea) 
            if len(x)>0:
                print(x)
            else:continue
        fname.close()
except :
    print('Error al abrir el archivo....')       

#%%
import re
# Main()
arcivo=input('Ponga  archivo a abrir:')
lista_horas=[]
try:
    with open(archivo,'r') as fname:
        for linea in fname:
            linea.rsplit()
            x=re.findall('^From .* (\d\d):',linea)
            if len(x)>0:
                for  y in  x :
                    lista_horas.append(y)
            else:continue
        fname.close()
except :
    print('Error de archivo')
    
print(lista_horas)                


# In[ ]:


"""Ejercicio 11.1 Escribe un programa sencillo que simule la forma de operar 
del comando grep de Unix.Pide al usuario una expresion regular y cuenta el numero
de lineas que localiza a partir de ella """
import re
# Main()

expresion= input('Introdusca expresion regular: ')

archivo='C:/Users/MBI/Documents/Spider_Scripts/Ejercicios_del_Curso_Python _para_Informaticos/Ejercicios_10/'
lista_archivo=['mbox.txt','romeo-full.txt','words.txt']
diccionario={}
try:
    for linea in lista_archivo:
        with open(archivo+linea,'r') as fname:
            for palabra in fname:
                palabra.rsplit()
                if re.search('^'+expresion,palabra):
                    diccionario[linea]=diccionario.get(linea,0)+1
                else:continue
except :
    print('Error de archivo...')       
            
print(diccionario)


# In[ ]:


"""Ejercicio 11.2 Escribe un programa para buscar lineas que tengan esta forma
New Revision: 39772 y extrae el numero de cada una de esas lineas, calcula
la media y el total y muestra al final la media obtenida"""
import re
# Main()

archivo=input('Ponga fichero a abrir: ')
contador=0
suma=0
try:
    with open(archivo,'r') as fname:
        for linea in fname:
            linea.rstrip()
            x=re.findall('^New .* (\d+)\s',linea)
            if len(x)>0:
                contador +=1
                for y in x:
                    suma += int(y)
            else:continue
        fname.close()
except :
    print('Error de  archivo...')  
      
print(suma/contador)


# In[ ]:


"""Extrayendo ip del mbox.txt"""
import re
# Main()
archivo=input('Ponga fichero a abrir: ')
lista=[]
try:
    with open(archivo,'r') as fname:
        for linea in fname:
            linea.rstrip()
            x=re.findall('^Received: .*\[(\d.+)\]',linea)
            if len(x)>0:
                for y in x:
                    lista.append(y)
            else:continue
        fname.close()
except :
        print('Error de archivo...')
        
for listar in lista:
    print(listar+'\n')

