
#Programa similar al main, pero con las simulaciones, con un archivo de coordenadas, una matreal que coge esas coordenadas y las transforma en matriz, y con su comparacion imagen a imagen, hasta que la varianza de la martriz que estamos recorriendo, y la real, tengan una siilitud importante.



#from random import randomint
#from  pruebaguardarpillow5 import *
from  calculavarianzacompuesta import tras
#from  kdtreespillow2prueba import *
from PIL import Image
import re
from random import randint
import numpy as np
from scipy import spatial
import scipy.io

import shutil # Libreria para borrar los recortes
        
from itertools import product, combinations

import os
import time
import pickle, sys, math
from sqlalchemy.sql.expression import except_
from logging import exception

from nueva_grafica import creargrafica


ruta= "."
ruta= os.path.join(ruta,"Recortes")

matrix=[] #La matriz que hay que pintar
mataux=[] #La matriz que vamos a usar para ir metiendo los distintos numeros de la matriz real, y compararlas
#print ("matrix")
columnas=0 
filas=0
numero_imagenes=0
ag=0
ap=0
rutafoto= "" #para pasarlo despues al fichero la pongo como global
listagenerador=[]

mediaimagenes=0
mediadiferencia=0

max_diferencia =0 #Para el %




#variables que no cambian con cada simulacion
#rutafoto = r'C:\Users\Jose Antonio\eclipse-workspace\prueba4\1.jpg'
#rutadatos = r'C:\Users\Jose Antonio\eclipse-workspace\prueba4\3_ann.mat'

lrutafotos=[r'./Datos/1.jpg',r'./Datos/3.jpg',r'./Datos/4.jpg',r'./Datos/19.jpg',r'./Datos/22.jpg']
lrutadatos=[r'./Datos/1_ann.mat',r'./Datos/3_ann.mat',r'./Datos/4_ann.mat',r'./Datos/19_ann.mat',r'./Datos/22_ann.mat']

ldifvarianza=[0.3, 0.1, 0.01, 0.001]

#rutafoto = r'./Datos/1.jpg'
#rutadatos = r'./Datos/1_ann.mat'


def devolverancho(rutafoto): #Uso este metodo para devolver el ancho
    im = Image.open(rutafoto)

    #Cojo el tamaño de la imagen
    form, tam, mod = (im.format, im.size, im.mode)
    #print (tam)
    maxx , maxy = tam
    #print (x)

    return maxx,maxy,tam , im

def esquinaaleatoria (ag,ap):
    #Coloco el cuadrado pequeno en un determinado punto del cuadrado grande
    global cpx, cpy
    cpx =randint(0, ag -1 - ap) #El -1 es para que no coincida con el comienazo del siguiente cuadrado grande
    cpy =randint(0, ag -1 - ap)
    return cpx,cpy



def devolvermatreal(ag,ap,filas,columnas,cpx,cpy):
    coordenadas =[]
    # compilando la regex
    patron = re.compile(r'\s+')
    
    # Abre archivo en modo lectura
    if '.mat' in rutadatos:
        coordenadas = scipy.io.loadmat(rutadatos)['annPoints']
        ficheroleermat=open("coordenadas_mat.txt","w")
        for coordenada in coordenadas:
            ficheroleermat.write(str(coordenada)+"\n")
        ficheroleermat.close()
    else:
        archivo = open(rutadatos,'r') #Modificar para crear ruta local

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
    #print (cpx,cpy)
    
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
                #print (ptemp)
                if ptemp[1] != cpy-ap/2 and ptemp[0] != cpx-ap/2:
                    puntos = puntos +1
            
            matrix[x][y]=matrix[x][y] +puntos
            cpy=cpy+ag
        cpy=cpyaux
        cpx=cpx+ag
    return (matrix)

    


def generador(filas, columnas):
        lista = [(0,0)]
        suma_columnas = columnas//2
        suma_filas = filas//2
        while suma_filas >0 or suma_columnas > 0:
            for i in range(0, filas, max(1,suma_filas)):
                for j in range(0, columnas, max(1,suma_columnas)):
                    if (i,j) not in lista:
                        lista.append((i,j))
            suma_filas //= 2
            suma_columnas //= 2
        #print ("uijhrilj")
        #print (lista)
        return lista    
    
      





def rellenar(numimagenactual, i, diferencia, nombrefichero):
        
        
        
        global columnas
        global filas
        global numero_imagenes
        global ag
        global ap
        global matrix
        global mataux
        global listagenerador
        
        global mediaimagenes
        global mediadiferencia
        
        global max_diferencia
        

        #print (listagenerador)
        #print (listagenerador[0])
                    
       
        
            
        if numimagenactual < numero_imagenes:
            
            #print (numimagenactual , numero_imagenes)
            
            mataux[listagenerador[numimagenactual]]=matrix[listagenerador[numimagenactual]]
            
            #print ("mataux")
            #print (mataux)
            
            #print ("matreal")
            #print (matrix)
            
            
            
            varianza=tras(mataux,ag,ap)
            varianzareal=tras(matrix, ag,ap)
            
            #print ("VARIANZA MIA:"+str(varianza))
            #print ("VARIANZA REAL:"+str(varianzareal))
            
            if (numimagenactual / numero_imagenes > 0.5 and (varianza - varianzareal) < diferencia* varianzareal):
                print (f"Numero de imagenes recorridas: {numimagenactual} \n con diferencia del {(varianza - varianzareal):.2f} ") 
                f=open(f'./Datos analisis/simulaciones{nombrefichero}_{diferencia}.txt','a')
                f.write (f"Simulacion {i+1} \t %.2f \t %.2f\n"%(numimagenactual/numero_imagenes,abs((varianza - varianzareal)/varianzareal))) #Para que te saque solo 2 decimales (expresiones) #abs para el valor absoluto
                f.close()
                
                mediaimagenes=mediaimagenes+numimagenactual
                mediadiferencia=mediadiferencia+(varianza - varianzareal)
                
                if (varianza - varianzareal) > max_diferencia:
                    max_diferencia=(varianza - varianzareal)
                raise Exception(f"Salirse (varianza)")        
            numimagenactual +=1


#print ("Prueba",numero_imagenes)


#Programa principal

numero_simulaciones =10000

for (rutafoto,rutadatos),diferencia in product(zip(lrutafotos,lrutadatos),ldifvarianza):
    
    nombrefichero=rutafoto.split("/")[-1] 
    #Creo el fichero para despues pasarselo al programa de las graficas
    f=open(f'./Datos analisis/simulaciones{nombrefichero}_{diferencia}.txt','w') 
    f.write ("SIMULACIONES \n")
    f.write ("-------------- \n")
    f.close()
    
    datosfoto= devolverancho(rutafoto) #retorno los datos de la imagen
    ancho=(datosfoto[0])
    #print (ancho)
    #global ag
    ag = math.ceil(ancho/6) #se puede cambiar ese 6 por el numero de columnas 
    print (ag, "Area Grande")
    print (ag/10, "AG / 10")
    #print (ancho/6,ag)
    #global ap
    #ap=50
    
    maxx, maxy, tam , im= devolverancho(rutafoto)
    filas =math.ceil (maxy/ag) 
    columnas =math.ceil (maxx/ag)
    numero_imagenes= filas*columnas
    
    
    
    
    #print (filas, "Filas")
    #print (columnas, "Columnas")
    #print (numero_imagenes, "Imagenes")
    
    
    #Programa para formar la matriz (kdtrees)
    


    for i in range (numero_simulaciones) :
        
        #Variables que cambian en cada simulacion (el ap y la esquina y por tanto la matriz entera)
        ap =randint(ag//10, ag//2) #Para que el area pequena no sea float
        
    
        #print (ap, "Area Pequena")
    
     
    
        matrix=np.zeros((filas, columnas)) # En este caso no es necesario inicializar a -1, porque no se va a rellenar 
        mataux=matrix.copy() #matriz con los valores reales en las posiciones recorridas y con ceros en el resto para calcular su varianza y calcular con la que estamos calculando nosotros
        
        
        cpx, cpy =esquinaaleatoria(ag, ap)
        #print (cpx, "cpx")
        #print (cpy, "cpy")
    
    
        matrix=devolvermatreal(ag, ap, filas, columnas, cpx, cpy)
        #print (matrix)
    
        listagenerador=generador(filas,columnas)
        listagenerador= list(listagenerador)
    
    
        try:
            for j in range (numero_imagenes): #Paso i para saber porque simulacion vamos y anadirlo al fichero de salida
                rellenar(j,i,diferencia, nombrefichero)
        except Exception as e:
            print (f"Simulacion {i+1} analizada")
            #print (e)    
    
    #Para hacer las medias, tengo la suma pero la he dividido. Lo hago ahora
    mediaimagenes=mediaimagenes/numero_simulaciones
    mediadiferencia=mediadiferencia/numero_simulaciones
    
    print (mediaimagenes,"media imagenes")
    
    print (mediadiferencia,"media diferencia")
    
    print (max_diferencia,"maxima diferencia")
    
   
    
    f=open(f'./Datos analisis/simulaciones{nombrefichero}_{diferencia}.txt','a')
    f.write (f"Maxima Diferencia: %.2f\n"%(max_diferencia)) #Para que te saque solo 2 decimales (expresiones)
    f.write (f"Media Imagenes: %.2f \t Media Diferencia: %.2f\n"%(mediaimagenes,mediadiferencia)) #Para que te saque solo 2 decimales (expresiones)
    f.close()

    creargrafica(nombrefichero, diferencia)



   
