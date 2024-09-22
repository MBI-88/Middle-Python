#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Created on Thu Mar 26 14:54:48 2020

@author: MBI

Ejecicio 6.5 Toma el codigo en Python siguiente, que almacena una cadena  y encuentra la cadena 
despues del operador punto y luego utiliza float para convertirla en un numero de punto flotante.
"""

# Main()

cad='X-DSPAM-Confidence: 0.8475'
pos=cad.find('.')
new_cad=cad[pos+1:]
numero_float=float(new_cad)
print('Cadena extraida y formateada :  %g'  % numero_float)


# In[ ]:




