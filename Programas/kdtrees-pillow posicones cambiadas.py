#https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/
# importando el modulo de regex de python
import re
import pickle, sys
f = open('c:\\Users\\user\\object','rb')
s = pickle.load(f)
for directorio in s:
	sys.path.append(directorio)
from numpy import array


from PIL import Image
from random import randint
import numpy as np
from scipy import spatial

coordenadas =[]
# compilando la regex
patron = re.compile(r'\s+')

# Abre archivo en modo lectura

archivo = open('c:\\Users\\User\\Desktop\\TFG\Datos\\datos (1)\\roi1.dat','r')

rutafoto = 'c:\\Users\\User\\Desktop\\portero.jpg'
im = Image.open(rutafoto)



# inicia bucle infinito para leer línea a línea
listatotal = list()

for linea in archivo.readlines():
    coordenadas=list ()
    num1 = patron.split(linea)
    #print(num1[0])  # Muestra la línea leída
    coordenadas.append(float (num1[0]))
    coordenadas.append(float (num1[1]))
    listatotal.append(coordenadas)

coordenadas= np.array(listatotal)    
    
archivo.close()  # Cierra archivo

#im = Image.open("hopper.ppm")

tree= spatial.KDTree(coordenadas)

print (coordenadas)

#Ahora necesito el tamaño del cuadrado grande, y del pequeño, ponerme en el medio del pequeño y mirar cuantos cuadrados hay
#Despues sumarle el tamaño del cuadrado grande hasta que llegue al tope de la imagen por arriba y por la derecha (necesito pillow)
#Hacer pruebas

maxx= np.amax(coordenadas [:,0])
maxy= np.amax(coordenadas [:,1])
print (maxx)
print (maxy)


ag=125
ap=25 #No esta permitido que el cuadrado pequeño sea mayor o igual que el cuadrado grande

#print (maxy)
filas =int (maxy//ag)+1 #
columnas =int (maxx//ag)+1

#Creo la matriz final
matrix=np.zeros((filas, columnas))
#print (matrix)

array_matrices=[] #para guardar todas las matrices y poder hacer la media al final

#Coloco el cuadrado pequeño en todos los puntos del cuadrado grande
for i in range(ag-ap):
        for i2 in range(ag-ap): # de 0 a 99 
                #print (i, i2)
                #print (i)
                cpx =i2 #El -1 es para que no coincida con el comienazo del siguiente cuadrado grande
                cpy =i
                #print (cpx,cpy) #El punto mas abajo a la izquierda del cuadrado
                #cojo el medio
                #print (cpx,cpy)
                cpx= cpx + ap/2
                cpy= cpy + ap/2
                print (cpx,cpy)
                cpyaux=cpy #para volver a la posicion
                cont=0 #contador para guardar las imagenes
                #Voy recorriendo la matriz
                for y in range(columnas):
                        for x in range (filas):
                                
                                indices= tree.query_ball_point ([cpx,cpy], ap/2, np.inf)
                                puntos=0
                                for i3 in indices:
                                        ptemp= coordenadas[i3]
                                        if ptemp[1] != cpy-ap/2 and ptemp[0] != cpx-ap/2:
                                                puntos = puntos +1

                
                                matrix[x][y]=matrix[x][y] +puntos

                                cpy=cpy+ag
      
        
                        cpy=cpyaux
                        cpx=cpx+ag

                
        

                #print (matrix)
                array_matrices.append(matrix)
                matrix=np.zeros((filas, columnas)) #reinicio la matriz


matrizmedia= np.mean(array_matrices, axis=0)
#print(array_matrices)
print (matrizmedia) 

