#Programa para a partir del fichero de resultado de las simulaciones, sacar la grafica
#Programa parecido al kdtreespillow a la hora de leer el fichero

import re
import pickle, sys


import numpy as np
import matplotlib.pyplot as plt

# Abre archivo en modo lectura
archivo = open('simulaciones.txt','r') #Modificar para crear ruta local
patron = re.compile(r'\s+')

# inicia bucle infinito para leer línea a línea y anadirlo a una lista
listatotal = list()


	
for linea in archivo.readlines():
	
	simulaciones=list ()
	num1 = patron.split(linea)
	#print (num1)
	if num1[0] == ("Simulacion"): #Las lineas que no sean simulaciones y que sean o presentacion o la media que no las incluya
	#print(num1[0])  # Muestra la línea leída
		simulaciones.append(float (num1[2]))
		simulaciones.append(float (num1[3]))
		listatotal.append(simulaciones)
	
archivo.close()  # Cierra archivo

print (listatotal)

#Ya tengo en la listatotal todos los datos. Ahora hay que hacer la grafica



# example data
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# example variable error bar values
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)


fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, sharex=True,
                                    figsize=(12, 6))

ax0.set_title('all errorbars')
ax0.errorbar(x, y1, yerr=y1err)
ax0.errorbar(x, y2, yerr=y2err)

ax1.set_title('only every 6th errorbar')
ax1.errorbar(x, y1, yerr=y1err, errorevery=6)
ax1.errorbar(x, y2, yerr=y2err, errorevery=6)

ax2.set_title('second series shifted by 3')
ax2.errorbar(x, y1, yerr=y1err, errorevery=(0, 6))
ax2.errorbar(x, y2, yerr=y2err, errorevery=(3, 6))

fig.suptitle('Errorbar subsampling')
plt.show()