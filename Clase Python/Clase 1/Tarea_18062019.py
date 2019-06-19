#Tarea 1: Sacar el promedio de la edad de una poblacion registrada en un archivo.c
import csv
with open('Tarea_18062019.csv') as archivo:
    lector=csv.reader(archivo)

    total=0
    contador=0

    x=input('Quiere promedio de edad o peso?: ')

    next (lector)

    if x=='edad':

#el for va de renglon por renglon
        for renglon in lector:
            #renglon [1] sgnifica que este en la columna 1,
            #como si fuera un arreglo y solo queremos la casilla 1
            total+= float(renglon[1])
            contador+=1

        prom=float(total/contador)
        print('El promedio de edad es',prom)

    if x=='peso':
        
        for renglon in lector:
            total+= float(renglon[2])
            contador+=1

        prom=float(total/contador)
        print('El promedio de peso es', prom)


        
        

        



       
        
        
        
    







    
    
    
    
    



      












      
    
