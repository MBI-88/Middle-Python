#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Tue Apr  7 20:55:17 2020

@author: MBI
Ejercicio 12.1 Cambiar el programa del socket socket1.py para  que pida al usuario la URL
, de modo que pueda leer cualquier pagina web. Usa try y except para contemplar la posibilidad
de que el usurio introdusca una URL mal formada o inexistente
"""
import socket
import re
# Main()
try:
    pagina= input('Ponga la Url y el puerto a buscar: ')
    puerto=0
    if re.search('^www.+\.com',pagina):
        p=re.findall('^www.+\.com.*:\s+(\d+)',pagina)
        h=re.findall('([a-z]\S+\.com)',pagina)
        for x in p:
            puerto=int(x)
        for y in h:
            host=y
            
    if len(host)>0 and puerto !=0:
        misock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        misock.connect((host,puerto))
        add=input('Ponga la direccion del archivo a buscar usando el protocolo:  ')
        misock.send('Get'+add+'\n\n')
        while True:
            datos=misock.recv(512)
            if len(datos) < 1:
                break
            print(datos)
        misock.close()
        
    else:
        print('Error de formato de pagina')

except :
    print('Error la pagina no existe')


# In[ ]:


"""Ejercicio  12.2 Cambia  el programa anterior para que cuente el numero de caracteres que  ha 
recibido y se detenga, con un texto en pantalla, despues de que se haya mostrado 3000 caracteres. El
programa debe recuperar el documento completo y contar el numero total de caracteres, mostrando ese total
al final del  documento """
import socket
import time as t
# Main()
try:
    pagina= input('Ponga la Url y el puerto a buscar: ')
    puerto=0
    tamaño=0
    if re.search('^www.+\.com',pagina):
        p=re.findall('^www.+\.com.*:\s+(\d+)',pagina)
        h=re.findall('([a-z]\S+\.com)',pagina)
        for x in p:
            puerto=int(x)
        for y in h:
            host=y
            
    if len(host)>0 and puerto !=0:
        misock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        misock.connect((host,puerto))
        add=input('Ponga la direccion del archivo a buscar usando el protocolo:  ')
        misock.send('Get'+add+'\n\n')
        while True:
            datos=misock.recv(512)
            tamaño +=len(datos)
            if len(datos) < 1:
                break
            if len(datos)==3000:
                print('Se ha cargado {} caracteres'.format(tamaño))
                t.sleep(0.25)
        print(datos,':',tamaño)
        misock.close()
        
    else:
        print('Error de formato de pagina')

except :
    print('Error la pagina no existe')


# In[ ]:


"""Ejercicio 12.3 Usa urlib para rehacer el ejercicio anterior de modo que reciba el
el documento de url, mestre hasta 3000 caracteres y cuente la cantidad total de caracteres en el documento."""
import urllib
import time as t
# Main()
try:
    pagina= input('Ponga la Url  a buscar: ')
    tamaño=0
    if re.search('^www.+\.com',pagina):
        h=re.findall('([a-zA-Z0-9]\S+)',pagina)
        for y in h:
            host=y
            print(host)

    if len(host)>0: 
        miurl=urllib.urlopen('http://'+host)
        for  linea in miurl:
            tamaño +=len(linea)
            if tamaño == 3000:
                print('Se ha cargado {} caracteres'.format(tamaño))
                t.sleep(0.25)
            else:continue
        print('Total de caracteres {}'.format(tamaño))
        miurl.close()
    else:
        print('Error de formato de pagina')
except :
    print('Error la pagina no existe')


# In[ ]:


"""Ejercicio 12.4 Cambia el programa urllinks.py para extraer y contar las etiquetas de parrafo (p)
del documento HTML recuperado y mostrar el total de parrafos como salida del programa."""
import urllib
from bs4  import BeautifulSoup
# Main()
try:
    url=input('Introdusca _')
    contador=0
    lista=[]
    html=urllib.urlopen(url).read()
    sopa=BeautifulSoup(html)
    etiqueta=sopa('p')
    for e in etiqueta:
        contador +=1
        lista.append(e.get('text',None))
    print('Total de parrafos {}'.format(contador))
except :
     print('Error la pagina no existe')

