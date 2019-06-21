#Ejercicios 2
myFile=open("./datosTamañoyPeso.txt")
#ir guardando valores en dudes para diferentes parametros
dudes=[0,0,0]


#Dividir el documento por cada enter que detecte
lines =myFile.read()
data=lines.split(sep="\n")


#Quitar el espacio que registra en el .txt por que al final puse un enter
if( data[len(data)-1] == '' ):
    data = data[0:len(data)-1]
print(data)


#Crear una funcion para contar las personas entre una estatura determinada
def countDudes(x,minLimit,maxLimit,space):
    if(x[0]>minLimit and x[0]<maxLimit):
        #busca al contador en el preograma
        global dudes
        dudes[space]+=1

        
#rango de cero a lo que duren los datos
for i in range (0,len(data)):
    data[i]=data[i].split(sep=",")
    data[i]=data[i][0:2]
    height = float(data[i][0])
    weight = float(data[i][1])
    #se usa 3 por que nadie mide mas de 3 metros o menos de 3 centimetros
    if(height>=3):
        height/=100
    data[i][0]=height
    print(data[i])
    #llamar la funcion para un parametro diferente
    countDudes(data[i],1.59,1.62,0)
    countDudes(data[i],1.63,1.68,1)
    countDudes(data[i],1.69,1.89,2)
    
print(dudes)
myFile.close()

