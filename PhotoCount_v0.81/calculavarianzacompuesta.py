#En teoria esta es la segunda varianza con los mismos datos
#Programa que calcula la varianza compuesta

import pickle, sys


#f = open('c:\\Users\\user\\object','rb')
#s = pickle.load(f)
#for directorio in s:
#	sys.path.append(directorio)

import numpy as np

import CountEmVariance 




def varc(ag,ap,a):
	
	#print (ag,ap,a)
	#qoi= [0,0,0,0,0,0] no hace falta
	#qei= [0,0,0,0,0,0]
	#print (qoi[1])
	#print (a)

	tau = ap/ag
	#print (tau,ag,ap,a)
	
	#Igual que en la varianza simple
	j,n=a.shape #es lo mismo que las 2 lineas de arriba pero de manera mas eficiente
	#shape coge en una tupla la dimension del array
	
	
	#para coger qoi y qei, es decir la suma de los numeros 
	qoi=a[[i for i in range(j) if i%2 ==0]]
	qoi=np.sum(qoi,axis=0)
	
	qei=a[[i for i in range(j) if not i%2 ==0]]
	qei=np.sum(qei,axis=0)
	
	#print('qoi'.format(qoi))
	#print('qei'.format(qei))
	
	#(Qoi-Qei)^2
	
	array_qei= np.array(qei) #Para quitar las comas
	array_qoi= np.array(qoi)
	array_qop= array_qoi - array_qei
	array_qop= array_qop**2
	#print (array_qop)
	qs=np.sum(array_qop)
	#print (qs)           
	
	array_Qi=array_qoi + array_qei
	Qi=np.sum(array_Qi)
	
	#print (array_Qi)
	#print (Qi)
	
	#C0 C1 y C2 , con index
	
	C0= array_Qi **2
	C0=np.sum(C0)
	#print (C0)
	
	#C1
	
	aux1C1= np.insert(array_Qi,0,0)
	aux2C1= np.insert(array_Qi,len(array_Qi),0)
	#print (aux1C1)
	#print (aux2C1)
	C1= aux1C1 * aux2C1
	C1=np.sum(C1)
	#print (C1)
	
	#C2
	aux1C2= np.insert(array_Qi,0,0)
	aux1C2= np.insert(aux1C2,0,0)
	aux2C2= np.insert(array_Qi,len(array_Qi),0)
	aux2C2= np.insert(aux2C2,len(aux2C2),0)
	#print (aux1C2)
	#print (aux2C2)
	C2= aux1C2 * aux2C2
	C2=np.sum(C2)
	#print (C2)
	
	#vn
	vn=(((1-tau)**2)/(3-2*tau))* qs
	
	#varianza
	#print (tau,C0,C1,C2,vn)
	varc= (1-tau)**2/(tau**4 * (2-tau))/6 * (3*(C0 - vn) -4*C1 + C2) + vn/tau**4
	return (varc)



def tras(matriz,ag,ap):
	    ag=ag*ag
	    ap=ap*ap
	    matt= np.transpose(matriz) #hace la traspuesta
	    vc1= varc(ag,ap,matriz) #calcula la varianza de la matriz normal
	    #print (vc1)
	    #print (matt)
	    #print (matriz)
	    vc2=varc(ag,ap,matt) #calcula la varianza de la matriz traspuesta
	    #print (vc2)
	    vc= (vc1+vc2)/2 #hace la media de las 2
	    return (vc)


def trasnueva(matriz,ag,ap):
	    ag=ag*ag
	    ap=ap*ap
	    matt= np.transpose(matriz) #hace la traspuesta
	    vc1= CountEmVariance.varc(ag,ap,matriz) #calcula la varianza de la matriz normal
	    #print (vc1)
	    #print (matt)
	    #print (matriz)
	    vc2=CountEmVariance.varc(ag,ap,matt) #calcula la varianza de la matriz traspuesta
	    #print (vc2)
	    vc= (vc1+vc2)/2 #hace la media de las 2
	    return (vc)