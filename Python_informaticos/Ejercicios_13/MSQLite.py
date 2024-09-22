#!/usr/bin/env python
# coding: utf-8

# ### Ejemplo de uso de base de datos creando una agenda de telefonos

# In[ ]:


import sqlite3 as sq
import time as tt
import sys as sistema
import pandas as pd


def insertar_persona(nombre,apellido_1,apellido_2):
    sql_query="""INSERT OR IGNORE INTO PERSONA  VALUES (NULL,?,?,?)"""
    tupla_persona=(nombre,apellido_1,apellido_2)
    try:
        conexion=sq.connect(base)
        cur=conexion.cursor()
        cur.execute(sql_query,tupla_persona)
        cur.close()
        conexion.commit()
        conexion.close()
        print('Datos guardados con exito')
        tt.sleep(2)
    except:
        print('No se pudo acceder a la base de datos')
        tt.sleep(2)
        
def insertar_numeros_telefonos(nombre,movil,telefono_f,telefono_t):
    sql_query="SELECT ID  FROM PERSONA  WHERE NOMBRE=?"
    sql_query_1="INSERT OR IGNORE INTO NUMEROS_TELEFONOS VALUES (?,?,?,?)"
    try:
        conexion=sq.connect(base)
        cur=conexion.cursor()
        cur.execute(sql_query,(nombre,))
        idn=cur.fetchone()[0]
        cur.execute(sql_query_1,(idn,movil,telefono_f,telefono_t))
        cur.close()
        conexion.commit()
        conexion.close()
        print('Datos guardados con exito')
        tt.sleep(2)
    except:
        print('No se pudo acceder a la base de datos')
        tt.sleep(2)
    



def seach(nombre):
    sql_busca="SELECT * FROM NUMEROS_TELEFONOS JOIN PERSONA ON NUMEROS_TELEFONOS.ID=PERSONA.ID WHERE PERSONA.NOMBRE=?"
    tupla_busca=(nombre,)
    try:
        conexion=sq.connect(base)
        data_frame=pd.read_sql_query(sql_busca,params=tupla_busca,con=conexion)
        print(data_frame)   
        conexion.commit()
        conexion.close()
        tt.sleep(2)
    except:
        print('No se pudo conectar con la base  de datos.')
        tt.sleep(2)
        
        
def delete_dato(nombre):
    sql_borra="DELETE FROM PERSONA WHERE PERSONA.NOMBRE=?"
    tupla_borra=(nombre,)
    try:
        conexion=sq.connect(base)
        cur=conexion.cursor()
        cur.execute(sql_borra,tupla_borra)
        print('Borrado del contacto {} con exito'.format(nombre))
        cur.close()
        conexion.commit()
        conexion.close()
        tt.sleep(2)
    except:
        print('Error en la conexion con la base de datos')
        tt.sleep(2)
    

def ver_base():
    try:
        conexion=sq.connect('Mi_agenda.db')
        data_frame=pd.read_sql_query('SELECT * FROM  PERSONA JOIN NUMEROS_TELEFONOS WHERE PERSONA.ID=NUMEROS_TELEFONOS.ID',conexion)
        conexion.commit()
        conexion.close()
        print(data_frame)
        tt.sleep(2)
    except:
        print('Error  al conectar con la base de datos.')
        tt.sleep(4)
        return -1

def borrar_todo():
    try:
        conexion=sq.connect(base)
        cur=conexion.cursor()
        cur.execute('DROP TABLE IF EXISTS PERSONA')
        conexion.commit()
        cur.close()
        conexion.close()
        print('Base de datos borrada con exito')
        tt.sleep(2)
    except:
        print('Error en la conexion con la base  de datos')
        tt.sleep(2)
        
def update_persona():
    print('1-Nombre')
    print('2-Apellido_1')
    print('3-Apellido_2')
    print('4-Movil')
    print('5-Telefono_casa')
    print('6-Telefono_trabajo')
    print('7-Regresar')
    sql_id="SELECT ID FROM PERSONA WHERE PERSONA.NOMBRE=?"
    orden=True
    while  orden:
        try:
            valor=int(input('Seleccione:___'))
            if valor < 1 or valor > 7 :
                print('Valor fuera de rango')
                tt.sleep(1)
            else:
                if valor==1:
                    sql_query="UPDATE PERSONA SET NOMBRE=? WHERE PERSONA.ID=?"
                    #Actualizar nombre
                    nombre_old=input('Nombre actual:__').capitalize()
                    nombre_new=input('Nombre nuevo:__').capitalize()
                    if nombre_new.isalpha() and nombre_old.isalpha():
                        try:
                            conexion=sq.connect(base)
                            cur=conexion.cursor()
                            cur.execute(sql_id,(nombre_old,))
                            idn=cur.fetchone()[0]
                            cur.execute(sql_query,(nombre_new,idn))
                            cur.close()
                            conexion.commit()
                            conexion.close()
                            print('Actualizacion con exito')
                            tt.sleep(2)
                        except:
                            print('Error en la conexion con la base de datos')
                            tt.sleep(1)
                    else:
                        print('Tiene errores en las entradas')
                            
                elif valor==2:
                    # Actualizacion de apellido 1
                    sql_apellido_1="UPDATE PERSONA SET APELLIDO_1=? WHERE PERSONA.ID=?"
                    nombre_old=input('Nombre actual:__').capitalize()
                    apellido_new=input('Apellido_1 nuevo:__').capitalize()
                    if nombre_old.isalpha() and apellido_new.isalpha():
                        try:
                            conexion=sq.connect(base)
                            cur=conexion.cursor()
                            cur.execute(sql_id,(nombre_old,))
                            idn=cur.fetchone()[0]
                            cur.execute(sql_apellido_1,(apellido_new,idn))
                            cur.close()
                            conexion.commit()
                            conexion.close()
                            print('Actualizacion con exito')
                            tt.sleep(2)
                        except:
                            print('Error en la conexion con la base de datos')
                            tt.sleep(1)
                    
                    else: 
                        print('Tiene errores en las entradas')
                        
                elif valor==3:
                    # Actualizacion de apellido_2
                    sql_apellido_2="UPDATE PERSONA SET APELLIDO_2=? WHERE PERSONA.ID=?"
                    nombre_old=input('Nombre actual:__').capitalize()
                    apellido_new=input('Apellido_2 nuevo:__').capitalize()
                    if nombre_old.isalpha() and apellido_new.isalpha():
                        try:
                            conexion=sq.connect(base)
                            cur=conexion.cursor()
                            cur.execute(sql_id,(nombre_old,))
                            idn=cur.fetchone()[0]
                            cur.execute(sql_apellido_2,(apellido_new,idn))
                            cur.close()
                            conexion.commit()
                            conexion.close()
                            print('Actualizacion con exito')
                            tt.sleep(2)
                        except:
                            print('Error en la conexion con la base de datos')
                            tt.sleep(1)
                    
                    else: 
                        print('Tiene errores en las entradas')
                        
                elif valor==4:
                    # Actualizar movil
                    sql_movil="UPDATE NUMEROS_TELEFONOS SET MOVIL=? WHERE NUMEROS_TELEFONOS.ID=?"
                    nombre_old=input('Nombre actual:__').capitalize()
                    movil_new=input('Movil nuevo:__')
                    if  nombre_old.isalpha() and movil_new.isnumeric():
                        try:
                            conexion=sq.connect(base)
                            cur=conexion.cursor()
                            cur.execute(sql_id,(nombre_old,))
                            idn=cur.fetchone()[0]
                            cur.execute(sql_movil,(movil_new,idn))
                            cur.close()
                            conexion.commit()
                            conexion.close()
                            print('Actualizacion con exito')
                            tt.sleep(2)
                            
                        except:
                            print('Error en la conexion con la base de datos')
                            tt.sleep(1)
                        
                    else:
                        print('Tiene errores en las entradas')
                        tt.sleep(1)
                        
                elif valor==5:
                    # Actualiza telefono casa
                    sql_casa="UPDATE NUMEROS_TELEFONOS SET TELEFONO_FIJO=? WHERE NUMEROS_TELEFONOS.ID=?"
                    nombre_old=input('Nombre actual:__').capitalize()
                    movil_new=input('Telefono de casa  nuevo:__')
                    if  nombre_old.isalpha() and movil_new.isnumeric():
                        try:
                            conexion=sq.connect(base)
                            cur=conexion.cursor()
                            cur.execute(sql_id,(nombre_old,))
                            idn=cur.fetchone()[0]
                            cur.execute(sql_casa,(movil_new,idn))
                            cur.close()
                            conexion.commit()
                            conexion.close()
                            print('Actualizacion con exito')
                            tt.sleep(2)
                        except:
                            print('Error en la conexion con la base de datos')
                            tt.sleep(1)
                        
                    else:
                        print('Tiene errores en las entradas')
                        tt.sleep(1)
                        
                elif valor==6:
                    # Actualiza telefono trabajo
                    sql_trabajo="UPDATE NUMEROS_TELEFONOS SET TELEFONO_TRABAJO=? WHERE NUMEROS_TELEFONOS.ID=?"
                    nombre_old=input('Nombre actual:__').capitalize()
                    movil_new=input('Telefono de trabajo  nuevo:__')
                    if  nombre_old.isalpha() and movil_new.isnumeric():
                        try:
                            conexion=sq.connect(base)
                            cur=conexion.cursor()
                            cur.execute(sql_id,(nombre_old,))
                            idn=cur.fetchone()[0]
                            cur.execute(sql_trabajo,(movil_new,idn))
                            cur.close()
                            conexion.commit()
                            conexion.close()
                            print('Actualizacion con exito')
                            tt.sleep(2)
                            
                        except:
                            print('Error en la conexion con la base de datos')
                            tt.sleep(1)
                    else:
                        print('Tiene errores en las entradas')
                        tt.sleep(1) 
                        
                elif valor==7:
                    orden=False
                    print('Regresando al menu principal')
                    tt.sleep(1)
                    
        except:
            print('La entrada tiene caracteres no permitidos')
            tt.sleep(1)
    
    


# Main()

print('********Agenda telefonica/Mi_agenda********')
base="Mi_agenda.db"
sql_query_p="""CREATE TABLE IF NOT EXISTS PERSONA
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    NOMBRE VARCHAR(20) UNIQUE,
    APELLIDO_1 VARCHAR(15),
    APELLIDO_2 VARCHAR(15)
) """
sql_query_n="""CREATE TABLE IF NOT EXISTS NUMEROS_TELEFONOS 
(
     ID INTEGER UNIQUE, 
     MOVIL INTEGER,
     TELEFONO_FIJO INTEGER,
     TELEFONO_TRABAJO INTEGER
     
) """
try:
    database=sq.connect(base)
    cur=database.cursor()
    cur.execute(sql_query_p)
    
    cur.execute(sql_query_n)
    print('Base de datos creada con exito')
    cur.close()
    database.commit()
    database.close()
    tt.sleep(2)
except:
    print('Error al crear la base de datos')
    tt.sleep(2)
    sistema.exit()
    
programa=True
while programa:
    print('\n')
    print('1-Insertar datos')
    print('2-Actualizar datos')
    print('3-Buscar datos')
    print('4-Borrar datos')
    print('5-Ver base de datos')
    print('6-Borrar Mi_agenda.db')
    print('7-Sallir')
    print('\n')
    try:        
                valor=int(input('Seleccione___'))
                print('\n')
                if valor > 7 or valor < 1:
                    print('Valor fuera del rango')
                else:

                     # Insertar datos
                    if valor == 1 :                  
                            nombre=input('Nombre:__').capitalize()
                            apellido_1=input('Apellido_1:__').capitalize()
                            apellido_2=input('Apellido_2:__').capitalize()
                            if nombre.isalpha() and apellido_1.isalpha() and apellido_2.isalpha():
                                insertar_persona(nombre,apellido_1,apellido_2)
                                print('Nota: si no tiene numero para la opcion ponga 0 en la entrada')
                                movil=input('Numero de movil a agregar:__')
                                fijo=input('Numero de telefono fijo a agregar:__')
                                trabajo=input('Numero de telefono trabajo a agregar:__')
                                if movil.isnumeric() and fijo.isnumeric() and trabajo.isnumeric() :
                                    insertar_numeros_telefonos(nombre,movil,fijo,trabajo)
                                else:
                                    print('El numero contiene errores')
                                    tt.sleep(2)                            

                            else:
                                print('Los datos ingresados tienen caracteres no alphanumericos')
                                tt.sleep(2)

                    # Actualizar datos    
                    elif valor == 2:
                        update_persona()
                

                    # Buscar datos           
                    elif valor == 3:
                        nombre=input('Nombre de contacto a buscar:__').capitalize()
                        if nombre.isalpha():
                            seach(nombre)
                        else:
                            print('El nombre tiene caracteres no permitidos')
                            tt.sleep(2)
                            

                    # Borrar datos           
                    elif valor == 4 :
                        nombre_borrado=input('Nombre a borrar:__').capitalize()
                        if nombre_borrado.isalpha():
                            delete_dato(nombre=nombre_borrado)
                        else:
                            print('El nombre contiene caracteres no permitidos')
                            tt.sleep(2)

                    # Ver base de datos            
                    elif valor == 5 :
                        ver_base()
                    # Borrrar Mi_agenda
                    elif valor == 6:
                        borrar_todo()
                    # Salir del programa
                    elif valor == 7:
                        programa=False
                        print('Saliendo....')
                        tt.sleep(4)
                    
    except:
        print('Error en la seleccion')


# In[ ]:




