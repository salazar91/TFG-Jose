#Programa para formar la matriz

#https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/
# importando el modulo de regex de python
import re
import pickle, sys
#f = open('c:\\Users\\user\\object','rb')
#s = pickle.load(f)
#for directorio in s:
#	sys.path.append(directorio)
from numpy import array


from PIL import Image
from random import randint
import numpy as np
from scipy import spatial

def devolvermatreal(ag,ap,filas,columnas,cpx,cpy):
	coordenadas =[]
	# compilando la regex
	patron = re.compile(r'\s+')
	
	# Abre archivo en modo lectura
	archivo = open('c:\\Users\\Jose Antonio\\eclipse-workspace\\prueba3\\annPoints_Iribar.dat','r') #Modificar para crear ruta local

	#rutafoto = 'c:\\Users\\User\\Desktop\\portero.jpg' #Modificar para poner la ruta local (ya la tenemos?)
	#im = Image.open(rutafoto)
	
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
	
	#print (coordenadas)
	
	#Creo la matriz final
	matrix=np.zeros((filas, columnas))
	#print (matrix)
	
	#Coloco el cuadrado pequeño en un determinado punto del cuadrado grande
	#Tenemos cpx y cpy
	
	#cojo el medio
	cpx= cpx + ap/2
	cpy= cpy + ap/2
	print (cpx,cpy)
	
	cpyaux=cpy #para volver a la posicion
	cont=0 #contador para guardar las imagenes
	#Voy recorriendo la matriz
	for y in range(columnas):
		for x in range (filas):
			#print ("X")
			i=str(cont) #Para la cadena de la imagen
			cont= cont +1
			
			#print (minxaux)
			#print ("Y")
			#print (minyaux)
			indices= tree.query_ball_point ([cpx,cpy], ap/2, np.inf)
			puntos=0
			for i in indices:
				ptemp= coordenadas[i]
				print (ptemp)
				if ptemp[1] != cpy-ap/2 and ptemp[0] != cpx-ap/2:
					puntos = puntos +1
			
			matrix[x][y]=matrix[x][y] +puntos
			cpy=cpy+ag
		cpy=cpyaux
		cpx=cpx+ag
	return (matrix)

	




