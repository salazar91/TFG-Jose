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
import os

os.mkdir("Recortes") #Creo el directorio para meter las fotos

rutafoto = 'c:\\Users\\User\\Desktop\\portero.jpg'
im = Image.open(rutafoto)

ag=125
ap=25

#Cojo el tamaño de la imagen
form, tam, mod = (im.format, im.size, im.mode)
print (tam)
maxx , maxy = tam
#print (x)

filas =int (maxy//ag)+1 #
columnas =int (maxx//ag)+1

print (filas, columnas)
cpx=0
cpy=0
cpyaux=cpy


cont=0
for y in range(columnas):
        for x in range (filas):
                i=str(cont)
                cont= cont +1
                box = (cpx, cpy, cpx+ag, cpy+ag)
                region = im.crop(box)
                region.save('Recortes\\hola'+i+'.jpg')
                #print (cont)
                cpy=cpy+ag
        cpy=cpyaux
        cpx=cpx+ag
                
#im.show()

#region = im.crop(box)
#region.show()
#region.save('hola.jpg')
