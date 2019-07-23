#Crear un archivo con un gen

import random

#definir funciones

def complement(value):
    if value =="A\n":
        return "A,T\n"
    if value =="T\n":
        return "T,A\n"
    if value =="C\n":
        return "C,G\n"
    if value =="G\n":
        return "G,C\n"
    
def filterAT(value):
    if(value=="A,T"):
        return "A,T"
    
variables =['A','T','G','C']
random_list=[]

#./ es que estan en el mismo directorio (misma carpeta)
f= open("./myGenes.csv","w")

for i in range(0,100):
    #de la casilla 0 a la casilla 3
    pollo=random.randint(0,3)
    random_list+=[variables[pollo]]
    #f.write(variables[pollo])
    #f.write("\n")
    #tambien puede ser:
    f.write(f'{variables[pollo]}\n')
    
f.close()

#Hacer un archivo con complementariedad del gen

f=open("./myGenes.csv")
lines=f.readlines()
print(lines)

complements_list=list(map(complement,lines))

f.close

f=open("./complementsGenes.csv","w")
f.write("".join(complements_list))
f.close()

f=open("./complementsGenes.csv","r")
#separar mientras lee el documento
lines=(f.read()).split(sep="\n")
f.close()

atList=list(filter(filterAT,lines))
print("AT is ", len(atList))

        

