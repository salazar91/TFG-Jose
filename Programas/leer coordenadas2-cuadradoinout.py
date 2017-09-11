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

archivo = open('c:\\Users\\User\\Desktop\\TFG\Datos\\datos (1)\\roi1.dat','r')
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
miny=np.amin(coordenadas [0,:])
maxx= np.amax(coordenadas [:,0])
maxy= np.amax(coordenadas [0,:])
#print (minx)
#print (miny)

#Transformar coordenadas para que empeicen en 0
coordenadas[:,0]=coordenadas[:,0]-minx
coordenadas[:,1]= coordenadas[:,1]-miny
print (coordenadas)

minx=0
miny=0
maxx=maxx-minx
maxy=maxy-miny

ag=125
ap=25

#Tirar cuadrados hasta que esten todos los puntos contados

puntos= len (coordenadas)
#print (puntos)

#print (coordenadas[:,0])
#Como guardar los puntos en la matriz
cont=1
#necesito auxiliar para volver al minx y miny
minxaux=minx
minyaux=miny

while minxaux<maxx:
        
        for i in coordenadas: #Mirar todos los puntos
                #print (cont)
                #print (i[0])
                #print (minx+ag)

                #print (i[1])
                #print (miny+ag)
                #cont = cont+1
        
        
                if i[0] < minxaux+ag and i[1] < minyaux+ag and i[0]>= minxaux and i[1] >= minyaux :
                        print (cont)

                        print (i)
                        puntos=puntos-1
                        cont=cont+1

                if minaux+ag==minaux+ag:
                        

        
                        
        

        
"""
while puntos:
        for i in coordenadas[] :
                print (i)
                if i[0,:]< minx+ag and i[:,0]< miny+ag:
                        print (i)

        print (puntos)
        puntos=puntos-1
"""
