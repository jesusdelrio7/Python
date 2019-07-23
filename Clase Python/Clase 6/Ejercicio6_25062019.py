#Ejercicio 6: quitar comas de datos numericos en archivos 

from statistics import *
import urllib.request
import json
import pandas as pd

#Se separan los datos por ;
def divideData (x):
    return x.split(sep=";")

#Se quita la coma para las columnas con los datos que son numericos
def setNumericData(x):
    if(len(x)>8):
        #por que entra la función con maps el corchete de columas se pone primero
        #content[filas][columnas], maps va de fila en fila por lo tanto lee content [columa]
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
    cols=(data[0].split(sep=";"))
    #Quitar el fila del los titulos
    print(data[0])
    data=data[1:]
    data=list(map(divideData,data))
    data=list(map(setNumericData,data))
    
                   
    df=pd.DataFrame(data[0:],columns=cols)
    

    '''
    myDataDescription=(df[" Total Discharges "].describe())
    print(myDataDescription)
    '''
    
    twoColumns1=(df.iloc[:,[0,10]])
    print(twoColumns1.groupby("ï»¿DRG Definition").sum())

    twoColumns2=(df.iloc[:,[5,11]])
    print(twoColumns2.groupby("Provider State").sum())

    twoColumns3=(df.iloc[:,[0,5]]).groupby([cols[5],cols[0]])


    #for item in twoColumns3=


    
    
        

    
    
    #diseases= df['0'].unique().tolist()
   
    
   

    #print(diseases)
   




