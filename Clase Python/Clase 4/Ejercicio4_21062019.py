from statistics import *

def changeNumbers(x):
    if x=="A":
        return 1
    if x=="C":
        return 2
    if x=="G":
        return 3
    if x=="T":
        return 4
    
f=open("./myGenes.csv")

#Cambiar las letras A,T,G y C en numeros y sacar moda
lines=(f.read()).split(sep="\n")
f.close()
#map es como un for, va por cada valor llamando la funcion que se le ponga
data=list(map(changeNumbers,lines))
val=mode(data)

#Ejercicio: importar un documento del internet y en una lista con genes
#de cuatro letras dividir todo por letra para saber la letra mas frecuentada
import urllib.request
import json
url="http://10.25.245.136:8080"
#req=urllib.request.Request(url,method="GET")
#response=urllib.request.urlopen(req)
#response_bytes=response.read()
#content= response_bytes.decode("utf8")
#print(content)



datos3=[]
c=0

content=open("./prueba1.txt")
#al principio todas las letras salen en un string con comas
#el string se divide en diferentes strings separados por comas
datos=(content.read().split(sep=","))
print(datos)

for i in range (0,len(datos)):
    for y in range (0,len(datos[i])):
        datos3 += datos[i][y]
        c+=1
        
        
print(datos3)
print (mode(datos3))

