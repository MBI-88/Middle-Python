#!/usr/bin/env python
# coding: utf-8

# Modifica el programa www.py4inf.com/code/geojson.py para imprimir en pantalla el codigo de pais de dos caracteres de los recuperados.Añade comprobacion de errores, de modo que el programa no rastree los datos si el codigo del pais no esta presente.

# In[ ]:


# Programa geojson.py
import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
        
    if 'status' not in js or js['status'] != 'OK'  or 'postal_code' not in js['address_components']:
        print ('==== Failure To Retrieve ====')
        print (data)
        continue
    else:
        print(json.dumps(js, indent=4))
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        code_pay= js['results'][0]['address_components']['postal_code']
        print ('lat',lat,'lng',lng,'postal_code',code_pay)
        location = js['results'][0]['formatted_address']
        print (location)
#Nota: Debe probarse el programa en internet


# In[ ]:




