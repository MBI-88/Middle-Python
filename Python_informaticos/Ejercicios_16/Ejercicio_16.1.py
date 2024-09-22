#!/usr/bin/env python
# coding: utf-8

# Escribe un programa que recorra un directorio  y todos sus subdirectorios, buscando los archivos 
# que tengan un sufijo  determinado (como MP3) y liste las parejas de ficheros que tengan el mismo
# tamaño.

# In[9]:


import os 

def buscar_dir(direccion):
    diccionario={}
    directorios=0
    for dispahts,dirs,filesname in os.walk(direccion):
        for  nombre_file in filesname:
            if nombre_file.endswith('.mp3') and len(nombre_file)>0:
                ruta=os.path.join(dispahts,nombre_file)
                peso=os.path.getsize(ruta)
                if peso in diccionario.keys():
                    print('Peso= {} Archivo_nuevo= {} Archivo_diccionario= {}'.format(peso,ruta,diccionario[peso]))
                    
                else:
                    diccionario[peso]=ruta
                    directorios=len(dirs)
            else:
                continue
    return diccionario
# Main()
try:

    direccion=input('Direccion:__')
    if os.path.isdir(direccion):
        print(buscar_dir(direccion)) 
    else:
        print('Error en la direccion')
except:
    print('El sistema no puede  encontrar  el directorio')


# Modificar el programa anterior  para buscar ficheros que tengan contenidos duplicados usando un algoritmo de hashing o cheksum

# In[42]:


import os  
import hashlib as has

def buscar_dir(direccion):
    diccionario={}
    directorios=0
    for dispahts,dirs,filesname in os.walk(direccion):
        for  nombre_file in filesname:
                ruta=os.path.join(dispahts,nombre_file)
                try:
                    with open(ruta,'r') as fname:
                            datos=fname.read()
                            fname.close()
                            cheksum= has.md5(datos.encode()).hexdigest()
                            if cheksum in diccionario.keys():
                                 print(ruta,'  ',diccionario[cheksum])

                            else:
                                diccionario[cheksum]=ruta
                except:
                    print('No se pudo abrir el archivo')
                      
           
    return diccionario

# Main()
directorio=input('Directorio a buscar')
if os.path.isdir(directorio):
    buscar_dir(directorio)
else:
    print('La entrada no es un directorio')


# In[ ]:




