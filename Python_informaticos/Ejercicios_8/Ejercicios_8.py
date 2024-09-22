#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Wed Apr  1 14:48:39 2020

@author: MBI
Ejercicio 9.1 Escribe un programa que lea las palabras  de word.txt y las almacene como
claves en un diccionario. No importa que valor tenga. Despues puedes usar el operador in
como un modo rapido de comprobar si una cadena esta en el diccionario.
"""
#%%
# Main()
word= 'C:/Users/MBI/Documents/Spider_Scripts/Ejercicios_del_Curso_Python _para_Informaticos/Ejercicios_8/words.txt'
diccionario={}
try:
    
    with open(word,'r') as fname:
        for linea in fname:
             new_line=linea.split()
             for x in new_line:
                diccionario[x] +=1
                
        fname.close()
except :
    print('Error de archivo')
       
valor=input('Ponga clave a buscar: ')

if  valor in diccionario:
    print('El valor esta en el diccionario')
else:
    print('El valor no esta en el diccionario')


# In[ ]:


"""Ejercicio 9.2 Escribe un programa que ordene  en categorias cada mensaje de correo segun el dia de  la semana
en que fue hecho  el envio."""
# Main()
mbox=input('Introdusca el nombre del archivo a abrir: ')
mbox_dic={}
try:
    with  open(mbox,'r') as fname:
        for linea in fname:
            lineas=linea.split()
            if len(lineas)==0 or lineas[0]!='From' or len(lineas)<2:
                continue
            else:
                mbox_dic[lineas[2]]=mbox_dic.get(lineas[2],0)+1
        fname.close()             
except :
       print('Error de archivo')
print(mbox_dic)


# In[ ]:


"""Ejercicio 9.3 Escribe un programa similar al anterior pero que diga de que direccion de correo electronico ha sido 
enviado"""
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
print(mbox_dic)


# In[ ]:


"""Ejercicio 9.4 Añade codigo al programa anterior para localizar quien tiene mas mensajes en el fichero"""
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

maximo= max(mbox_dic)
print('El maximo es : el destinatario {} tiene un total de {} mensajes'.format(maximo,mbox_dic[maximo]))


# In[ ]:



"""Ejercicio 9.5 Este programa debe guardar el nombre de dominio desde donde se envio el mensaje en vez de 
quien mando el mensaje"""
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
                    inicio=lineas[1].find('@')
                    dominino=lineas[1]
                    mbox_dic[dominino[inicio+1:]]=mbox_dic.get(dominino[inicio+1:],0)+1
            fname.close()             
except :
      print('Error de archivo')
    
print(mbox_dic)

