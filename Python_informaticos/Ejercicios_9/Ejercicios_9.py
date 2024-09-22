#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Wed Apr  1 23:29:32 2020

@author: MBI
Ejercicio 10.1 Partiendo del ejercicio  9.3  crea una lista de tuplas (cotador,email)
a partir  del diccionario. Luego  ordenala lista  en orden inverso y muestra la persona
que tiene mas envios
"""
# Main()
mbox=input('Introdusca el nombre del archivo a abrir: ')
mbox_dic={}
try:
    with  open(mbox,'r') as fname:
        for linea in fname:
            lineas=linea.split()
            if len(lineas)==0 or lineas[0]!='From' or len(lineas)<1:
                continue
            else:
                mbox_dic[lineas[1]]=mbox_dic.get(lineas[1],0)+1
        fname.close()             
except :
       print('Error de archivo')

lista_tuplas=[]

for contador,email  in mbox_dic.items():
    lista_tuplas.append((email,contador))

lista_tuplas.sort(reverse=True)
contador,email =lista_tuplas[0]
print('El mayor  es {}  con {} envios'.format(email,contador))


# In[ ]:


#%%
"""Ejercicio 10.2 Crea un programa que cuente la distribucion de las horas del dia para
cada uno de los mensajes"""
# Main()
mbox=input('Introdusca el nombre del archivo a abrir: ')
mbox_dic={}
try:
    with  open(mbox,'r') as fname:
        for linea in fname:
            lineas=linea.split()
            if len(lineas)==0 or lineas[0]!='From' or len(lineas)<5:
                continue
            else:
                linea_5=lineas[5]
                hora=linea_5[:2]
                mbox_dic[hora]=mbox_dic.get(hora,0)+1
                
        fname.close()             
except :
       print('Error de archivo')
lista_tuplas=[]
for x,y in mbox_dic.items():
    lista_tuplas.append((x,y))

lista_tuplas.sort()
for  horas,mensajes in lista_tuplas:
    print('Horas {} , Mensajes {}'.format(horas,mensajes))


# In[ ]:


"""Ejercicio 10.3 Escribe un programa que solo lea de un archivo letras de la a-z y no tenga en cuneta
ningun signo de puntuacion"""
# Main()
archivo=input('Nombre de archivo:')
lista_palabras=[]
try:
    with open(archivo,'r') as fname:
        for linea in fname:
            lineas=linea.split()
            if len(lineas)==0:
                continue
            else:
                for x in lineas:
                    lista_palabras.append(x)
        fname.close()
except :
      print('Error de archivo')

diccionario_letras={}
for x in lista_palabras:
    for y in x.lower():
       if   y.isalpha():
            diccionario_letras[y]=diccionario_letras.get(y,0)+1
       else:
            continue
alfabeto=[]
for i in diccionario_letras.keys():
    alfabeto.append(i)
    
alfabeto.sort(reverse=True)    
print(alfabeto)

