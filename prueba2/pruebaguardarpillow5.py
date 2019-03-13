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
import glob,os

rutafoto = 'c:\\Users\\User\\Desktop\\TFG\\Datos\\Fig1A_original.jpg'
ag=500
ap=25

def recortar_imagen(ag, ap, rutafoto): #¿Cuando cargas la imagen te coge la ruta?
	os.mkdir("Recortes") #Creo el directorio para meter las fotos
	im = Image.open(rutafoto)


    #Cojo el tamaño de la imagen
	form, tam, mod = (im.format, im.size, im.mode)
	print (tam)
	maxx , maxy = tam
    #print (x)

    #tamaux= np.array(tam)

    #Creo la foto que sera el collage
	new_im=Image.new("RGB", (tam[0]+500,tam[1]+500) ) #Creo la imagen
	ims = [] #Meto los recortes en este array



	filas =int (maxy//ag)+1 #
	columnas =int (maxx//ag)+1

	print (filas, columnas)
	#Coloco el cuadrado peque�o en un determinado punto del cuadrado grande
	cpx =randint(0, ag -1 - ap) #El -1 es para que no coincida con el comienazo del siguiente cuadrado grande
	cpy =randint(0, ag -1 - ap)
	cpyaux=cpy
	
	cont=0
	
	#cont=0
	
	for y in range(columnas):
		for x in range (filas):
			i=str(cont)
			a=str(x)
			b=str(y)
			cont= cont +1
			box = (cpx, cpy, cpx+ap, cpy+ap)
			region = im.crop(box)
			region.save('Recortes\\recorte'+a+'_'+b+'.jpg')
			#print (cont)
			cpy=cpy+ag
		cpy=cpyaux
		cpx=cpx+ag
	numero_imagenes= cont

	for infile in glob.glob("Recortes\\*.jpg"):
		print (infile)
		im = Image.open(infile)
		im.thumbnail(tam)
		ims.append(im)
	#print (ims)
	i = 0
	x = 0
	y = 0
	for col in range(columnas):
		for row in range(filas):
			print(i, x, y)
			new_im.paste(ims[i], (x, y))
			i += 1
			y += ag +15
		x += ag + 15
		y = 0

	new_im.save ("collage.jpg")
	print (numero_imagenes)
	return numero_imagenes, filas , columnas
                
	#im.show()

	#region = im.crop(box)
	#region.show()
	#region.save('recorte.jpg')
recortar_imagen(ag, ap, rutafoto)