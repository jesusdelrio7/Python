#Ejercicio 6: quitar comas de datos numericos en archivos 

from statistics import *
import urllib.request
import json

#Se separan los datos por ;
def divideData (x):
    return x.split(sep=";")

#Se quita la coma para las columnas con los datos que son numericos
def setNumericData(x):
    if(len(x)>8):
        a=float(x[8].replace(",",""))
        b=float(x[9].replace(",",""))
        c=float(x[10].replace(",",""))
        d=float(x[11].replace(",",""))
        return x[:8] + [a,b,c,d]
    else:
        return x

download=False

if(download==True):
    
    url="http://10.25.245.136:8080"
    req=urllib.request.Request(url,method="GET")
    response=urllib.request.urlopen(req)
    response_bytes=response.read()
    content= response_bytes.decode("cp1252")
    #Analogo a descargar el documento de internet
    f=open("tempData.txt","w")
    f.write(content)
    f.close()

else:

    f=open("tempData.txt")
    data=(f.read().split(sep="\n"))
    print (data[0])
    data=data[1:]#???
    data=list(map(divideData,data))
    data=list(map(setNumericData,data))
    
   

    print(data[0:20])




