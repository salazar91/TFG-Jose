#En teoria esta es la segunda varianza con los mismos datos

import pickle, sys

f = open('c:\\Users\\user\\object','rb')
s = pickle.load(f)
for directorio in s:
	sys.path.append(directorio)

import numpy as np

#Me falta pasarlo a funcion pero me tenia que ir, el resultado es correcto


def varc(ag,ap,a):

        #ag=250
        #ap= 50
        #n=64



        #a = np.array([(0,0,1,0,0,0), (5,3,0,0,0,0), (4,3,3,0,0,0), (0,2,0,4,0,0), (0,0,2,4,4,0), (0,0,3,3,3,0), (0,0,0,2,2,2)])
        qoi= [0,0,0,0,0,0]
        qei= [0,0,0,0,0,0]
        #print (qoi[1])
        #print (a)

        tau = ap/ag
        #print (tau)

        #Igual que en la varianza simple
        n=len(a[0]) #las columnas ( se podrian quitar las que no tuvieran datos y se quedarian en 6
        j=len(a) #Numero de filas


        #para coger qoi y qei, es decir la suma de los numeros 
        qoi=a[[i for i in range(j) if i%2 ==0]]
        qoi=np.sum(qoi,axis=0)

        qei=a[[i for i in range(j) if not i%2 ==0]]
        qei=np.sum(qei,axis=0)
        print (qei)

        #print('qoi'.format(qoi))
        #print('qei'.format(qei))

        #(Qoi-Qei)^2

        array_qei= np.array(qei) #Para quitar las comas
        array_qoi= np.array(qoi)
        array_qop= array_qoi - array_qei
        array_qop= array_qop**2
        print (array_qop)
        qs=np.sum(array_qop)
        print (qs)           



        array_Qi=array_qoi + array_qei
        Qi=np.sum(array_Qi)

        print (array_Qi)
        print (Qi)

        #C0 C1 y C2 , con index

        C0= array_Qi **2
        C0=np.sum(C0)
        print (C0)

        #C1

        aux1C1= np.insert(array_Qi,0,0)
        aux2C1= np.insert(array_Qi,len(array_Qi),0)
        #print (aux1C1)
        #print (aux2C1)
        C1= aux1C1 * aux2C1
        C1=np.sum(C1)
        print (C1)

        #C2
        aux1C2= np.insert(array_Qi,0,0)
        aux1C2= np.insert(aux1C2,0,0)
        aux2C2= np.insert(array_Qi,len(array_Qi),0)
        aux2C2= np.insert(aux2C2,len(aux2C2),0)
        print (aux1C2)
        print (aux2C2)
        C2= aux1C2 * aux2C2
        C2=np.sum(C2)
        print (C2)

        #vn

        vn=(((1-tau)**2)/(3-2*tau))* qs
        print (vn)

        #varianza
        #Seguro que sobra algun parentesis
        varc= (((1-tau)**2)/(tau**4 * (2-tau))/6) * (3*(C0 - vn) -4*C1 + C2) + (vn/tau**4)
        #print (varc)
        return (varc)


#Esto meterlo en otra funcion (lo de la el resultado de la matriz, la traspuesta y la media) ?
ar = np.array([(0,0,1,0,0,0), (5,3,0,0,0,0), (4,3,3,0,0,0), (0,2,0,4,0,0), (0,0,2,4,4,0), (0,0,3,3,3,0), (0,0,0,2,2,2)])
art= np.transpose(ar)
vc1= varc(250,50,ar)
print (vc1)
print (art)
vc2=varc(250,50,art)
print (vc2)
vc= (vc1+vc2)/2
print (vc)
