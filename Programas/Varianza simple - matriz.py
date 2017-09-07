#En teoria esta es la varianza simple con los datos que te dan en el ejemplo de la figura 1B,
#Pero no da lo mismo.
#igual t y t' son el lado y ag y ap el area

import pickle, sys

f = open('c:\\Users\\user\\object','rb')
s = pickle.load(f)
for directorio in s:
	sys.path.append(directorio)

import numpy as np

ag=250
ap= 50



a = np.array([(0,0,1,0,0,0), (5,3,0,0,0,0), (4,3,3,0,0,0), (0,2,0,4,0,0), (0,0,2,4,4,0), (0,0,3,3,3,0), (0,0,0,2,2,2)])

print (a)


n=len (a)* len(a[0]) #len(a) te coge la longitud de las columnas, y len(a[0]) te coge la longitud de la primera fila como si fuera un array (Resultado = 7*6)
print (n)

x = np.mean(a)
v = np.var(a)

print(x, v)

#varianza sencilla? , no entiendo los datos de un cuadrado, no deberia ser un numero normal, y no un array?
vs = (ag/ap) **2 * n * v

print (vs)
