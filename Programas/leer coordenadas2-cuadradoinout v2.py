#https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/
# importando el modulo de regex de python
import re
import pickle, sys
f = open('c:\\Users\\user\\object','rb')
s = pickle.load(f)
for directorio in s:
	sys.path.append(directorio)
from numpy import array



import numpy as np

coordenadas =[]
# compilando la regex
patron = re.compile(r'\s+')

# Abre archivo en modo lectura

archivo = open('c:\\Users\\User\\Desktop\\TFG\Datos\\datos (1)\\annPoints_Iribar.dat','r')
"""cad1 = obj.read(9)
cad2 = obj.read()
print (cad1)

print("---------------")

print (cad2)"""


# inicia bucle infinito para leer línea a línea
listatotal = list()

for linea in archivo.readlines():
    coordenadas=list ()
    num1 = patron.split(linea)
    #print(num1[0])  # Muestra la línea leída
    coordenadas.append(float (num1[0]))
    coordenadas.append(float (num1[1]))
    listatotal.append(coordenadas)
    
coordenadas= array(listatotal)    
    
archivo.close()  # Cierra archivo
#print (coordenadas)
#print (coordenadas[:,0])


#tienes que mirar el x mas pequeño y el y mas pequeño para empezar a contar tus cuadrados
minx=np.amin(coordenadas [:,0]) #axis?
miny=np.amin(coordenadas [:,1])
maxx= np.amax(coordenadas [:,0])
maxy= np.amax(coordenadas [:,1])
#print (maxx)
#print (maxy)
#print (minx)
#print (miny)

#Transformar coordenadas para que empeicen en 0
coordenadas= coordenadas - np.array([minx,miny]) 
#coordenadas[:,0]=coordenadas[:,0]-minx
#coordenadas[:,1]= coordenadas[:,1]-miny
print (coordenadas)

#print (maxy)
#print (miny)
maxx=maxx-minx
maxy=maxy-miny

minx=0
miny=0


ag=250
ap=50

#Tirar cuadrados hasta que esten todos los puntos contados

puntos= len (coordenadas)
#print (puntos)

#print (coordenadas[:,0])
#Como guardar los puntos en la matriz
contp=1#contador prueba
#necesito auxiliar para volver al minx y miny
minxaux=minx
minyaux=miny

#print (maxy)
filas =int (maxy//ag)+1 #
columnas =int (maxx//ag)+1

#Creo la matriz final
matrix=np.zeros((filas, columnas))
print (matrix)

#while minxaux<maxx: # minyaux<maxy:
for y in range(columnas):
        for x in range (filas):
                print ("X")

                print (minxaux)
                print ("Y")
                print (minyaux)
                

                for i in coordenadas:
                        if i[0]>= minxaux and i[0]<minxaux+ag and i[1]>=minyaux and i[1]<minyaux+ag:
                                #print (contp)
                                print (i)
                                contp= contp+1
                                matrix[x][y]=matrix[x][y] +1
                minyaux=minyaux+ag
                        
        
        
        minyaux=miny
        minxaux=minxaux+ag
        

print (matrix)

#llamar a var compuesta4
#from varcompuestav3 import varc
#import varcompuestav3 as vcomp
#print (varc(ag, ap, matrix))
