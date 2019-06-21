#Tarea: Juntar 2 archivos con numeros aleatorios. Un archivo con num 1-8 y
#otro con num 1-20.Despues ordenarlo por valor y quitarle numeros repetidos
myFile=open("./Tarea2.csv")
myFile1=open("./Tarea2.2.csv")

lines=myFile.read()
lines1=myFile1.read()
data1=lines.split(sep="\n")
data2=lines1.split(sep="\n")

#unir archivos
data3=data1+data2

c=0

#ordenar por valores

#este for permite que ningun valor no se lea
for i in range (1,len(data3)):
    #este for ayuda a que el valor avanze a travez de la lista
    for x in range (0,len(data3)-i):
            if int(data3[x+1])<int(data3[x]):
                #se guarda en una variable el valor para ser remplazado
                c=data3[x]
                (data3[x])=(data3[x+1])
                (data3[x+1])=c

#quitar numeros repetidos

#este for revisa todos los datos                
for i in range (2,len(data3)):

    #este for va impidiendo que se repitan datos remplazando el valor de las dos
    #proximas casillas (si se repiten)
    for x in range (0,len(data3)-i):
        if int(data3[x+1])==int(data3[x]):
            (data3[x+1])=(data3[x+2])

#quitar los ultimos numeros del algoritmo de arriba (quitar numeros repetidos)            
data4=data3

#debido a que se juntaron los datos repetidos al final, este algoritmo detecta
#los valores que se repiten para quitarlos de la lista
for i in range (-len(data4),-1):
        if int(data3[i+1])==int(data3[i]):
            data3 = data3[0:len(data3)-1]
            
        

print(data3)


    
