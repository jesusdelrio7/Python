#Ejercicio 5

segments= [0,1,2,3,4,5,6,7]

segments[0]=([2,1,3,1,1,0,2,1])
segments[1]=([1,1,2,2,1,1,0,1])
segments[2]=([0,1,1,1,0,1,0,1])
segments[3]=([2,0,1,0,1,2,0,1])
segments[4]=([1,0,2,1,3,1,0,2])
segments[5]=([0,1,2,1,2,3,2,1])
segments[6]=([0,0,0,0,1,1,2,3])
segments[7]=([1,1,2,1,0,2,2,1])


z=0
c=0
twoswithzeros=0
threeswithtwos=0



for i in range (0,len(segments)):
        #se recomienda hacer, thissegment=segment[i]
        for y in range (0,len(segments[i])):

            #cuantos 2 tienen al menos 1 alrededor (arriba, abajo, izquierda y derecha) 
            if segments[i][y] == 2:
                    countMe=False
                    #los 2 de la primera fila 
                    if (i>0 and segments[i-1][y]==1):
                            countMe=True
                    #los 2 de la ultima fila
                    if (i<len(segments)-1 and segments[i+1][y]==1):
                            countMe=True
                    #los 2 de la primera columna   
                    if (y>0 and segments[i][y-1]==1):
                            countMe=True
                    #los 2 de la ultima columna         
                    if (y<len(segments[i])-1 and segments[i][y+1]):
                            countMe=True
                            
                    if countMe:
                            z+=1
            

            #para ver cuantos 2 tienen un zero a la izquierda
            if y>0 and segments[i][y]==2:
                if(segments[i][y-1]==0):
                    twoswithzeros+=1
                    
            #para ver cuantos 3 tienen a la derecha un 2
            if y<(len(segments)-2) and segments[i][y]==3:
                if(segments[i][y+1]==2):
                    threeswithtwos+=1

            #para ver cuandos 0 hay en las primeras y ultimas lineas
            if i==0 or y==0 or i==(len(segments)-1) or y==(len(segments[i])-1):
                if segments[i][y]==0:
                    c+=1


                            
                    
                


print(z)
print(twoswithzeros)
print(threeswithtwos)
print(c)





