#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Ejercicio 7.1  Escribe un programa que lea un fichero e imprima en pantalla su 
contenido linea a linea, todo en mayusculas.
"""
# Main()
nombre=input('Nombre de archivo  a abrir: ')
try:
    with open(nombre,'r') as fname:
        for linea in fname:
            print(linea.upper().rstrip())
        fname.close()
except :
    print('Error  en la apertura')


# In[ ]:


"""
Ejercicio 7.2 Escribe un programa que pida el nombre de un fichero y despues lea ese fichero, buscando lineas que tengan la forma 
X-DSPAM-Confidence: 0.8475.
Cuando se encuentre una linea separa esa linea para extraer el numero flotante que figure en ella, cuenta esas lineas y calcula el valor medio
de la probabilidad de spam
"""
# Main()

archivo=input('Introdusca nombre de archivo:')
contador=0
total=0
try:
   with open(archivo,'r') as fname:
        for linea in fname:
            if linea.startswith('X-DSPAM-Confidence:'):
                new_linea=linea.rstrip()
                inicio=new_linea.find(' ')
                final=new_linea.find('\n')
                valor = float(linea[inicio+1:final])
                total += valor
                contador = contador + 1

            else:
                continue
        fname.close()
except :
    print('Error de archivo')
valor_medio=total/contador
print('Valor meido de probabilidad de spam : {}'.format(valor_medio))


# In[1]:


"""Ejercicio 7.3 Modifica el programa anterior para cunado el usuario  
  ponga el nombre exactona na boo boo imprima por pantalla un mensaje 
  divertido."""
# Main()
archivo=input('Introdusca nombre de archivo:')
mensaje=''
try:
   with open(archivo,'r') as fname:
        if archivo == 'na na boo boo.txt':
            for linea in fname:
                if linea.find('-') != -1:
                    pos= linea.find('-')
                    mensaje=linea[pos+1:]
                    print(mensaje+'Felicidades Na Na Boo Boo'+' '+'Resive tu nuevo IPhon 11')
                else:
                    continue
        else:
            for linea in fname:
                print(linea.rstrip())
                
        fname.close()
except :
    print('Error de archivo')


# In[ ]:




