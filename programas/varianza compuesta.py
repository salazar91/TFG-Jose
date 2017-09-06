#En teoria esta es la segunda varianza con los mismos datos

import pickle, sys

f = open('c:\\Users\\user\\object','rb')
s = pickle.load(f)
for directorio in s:
	sys.path.append(directorio)

import numpy as np

ag=250
ap= 50
n=64



a = np.array([(0,0,1,0,0,0), (5,3,0,0,0,0), (4,3,3,0,0,0), (0,2,0,4,0,0), (0,0,2,4,4,0), (0,0,3,3,3,0), (0,0,0,2,2,2)])
qoi= [0,0,0,0,0,0]
qei= [0,0,0,0,0,0]
#print (qoi[1])
#print (a)

tau = ap/ag
#print (tau)
n=6 #las columnas ( se podrian quitar las que no tuvieran datos y se quedarian en 6
j=7 #Numero de filas

for x in range (n):
    for y in range (j):
        #print (x)
        #Esto es una guarreria pero si el indice es par le meto donde los impares porque empieza en 0 y en el ejemplo del articulo empieza en 1
        if y %2 ==0:
            qoi[x]= qoi[x]+a[y][x]
        else:
            qei[x]= qei[x]+a[y][x]
        #print (a[x][0])
    

#print('qoi'.format(qoi))
#print('qei'.format(qei))

#(Qoi-Qei)^2
array_qei= np.array(qei)
array_qoi= np.array(qoi)
array_qop= array_qoi - array_qei
print (array_qop**2)
qs=np.sum(array_qop**2)
print (qs)           

qop= [0,0,0,0,0,0]
qops=0
Q= [0,0,0,0,0,0]
Qs=0

for i in range (len(qop)):
    #qop[i]= qoi[i] - qei[i]
    #qop[i]= qop[i] **2
    #qops= qops + qop[i]
    Q[i]= qoi[i] + qei[i]
    Qs = Qs + Q[i]


print (qop)
#print (Q)

#print (qops)
#print (Qs)




#varianza sencilla? , no entiendo los datos de un cuadrado, no deberia ser un numero normal, y no un array?
#vn1 = ((1-tau)**2 / (3-2*tau))* qops#no se como poner a vn en forma de funcion v(n), en realidad no habria que ponerlo en este caso pienso
#print (vn1)
