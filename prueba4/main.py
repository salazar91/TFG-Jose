from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle
#from random import randomint
from  pruebaguardarpillow5 import *
from  calculavarianzacompuesta import tras, trasnueva
from  kdtreespillow2prueba import *
import shutil # Libreria para borrar los recortes
        
import numpy as np #Para rellenamatriz
from itertools import product, combinations

import os

#from simulacion import numero_imagenes


ruta= "."
ruta= os.path.join(ruta,"Recortes")

matrix=[] #La matriz que hay que pintar
mataux=[]
print ("matrix")
numimagenactual =0 #El anterior contador de la imagen por la que ibamos no la pongo porque da fallos extranhos
columnas=0 
filas=0
numero_imagenes=0
ag=0
ap=0
rutafoto= "" #para pasarlo despues al fichero la pongo como global
listagenerador=[]



#class Boton(Button):


    

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    contador =0
    

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()
        #self.ids["var_text"].text= "20"

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,size_hint=(0.9, 0.9))
        self._popup.open()
    
    def load(self, path, filename):
        print(filename[0])
        extension = os.path.splitext(filename[0])[1] #Para coger la extension (Con el import os)
        print (extension)
        #*****************
        #Si la extension no es jpg, pasarlo a jpg (el nombre y la imagen)
        #if extension != ".jpg":
        #
        #
        #
        #
        #*****************    
            
            
        #Para reescribir el fichero de coordenadas
        f=open('coordenadas.txt','w')
        f.write ("COORDENADAS \n")
        f.write ("-------------- \n")
        f.close()
        
        #Para rescribir el fichero resultados
        f=open('resultados.txt','w')
        f.write ("RESULTADOS \n")
        f.write ("-------------- \n")
        f.close()
            
            
        self.ids["mario"].source=filename[0]
        self.ids["var_text"].text= "20"
        
        self.dismiss_popup()
        
        #Hacer aqui el pop up del area pequena
        global rutafoto
        rutafoto = (filename[0])
        
        datosfoto= devolverancho(rutafoto) #retorno los datos de la imagen
        ancho=(datosfoto[0])
        print (ancho)
        global ag
        ag = math.ceil(ancho/6) #se puede cambiar ese 6 por el numero de columnas 
        #ag = int(input("Area Grande: "))
        #ag=500
        print (ancho/6,ag)
        global ap
        ap = int(input("Lado Pequeño: ")) #No esta permitido que el cuadrado pequeño sea mayor o igual que el cuadrado grande
        #ap=25
        #self.ids["lienzo"].pinta=True
        while ap> ag:
            print("Area Pequena se sale de Area Grande")
            ap = int(input("Lado Pequeño: ")) 
            
        global filas
        global columnas
        global numero_imagenes
        numero_imagenes, filas, columnas=recortar_imagen(ag, ap, rutafoto)
        global matrix
        global mataux
        matrix=np.zeros((filas, columnas)) #Rellena a -1
        mataux=np.zeros((filas, columnas)) #matriz con los valores reales en las posiciones recorridas y con ceros en el resto para calcular su varianza y calcular con la que estamos calculando nosotros. La inicializamos de la misma forma que la otra
        print(matrix, "Prueba")
        print(mataux, "Prueba2")
        
        self.ids["Sig"].opacity=100
        self.ids["Sig"].disabled=False  
        
        self.ids["Cargar"].text="Reiniciar"
        self.ids["Cargar"].on_release= self.reset()
       
        
        #Por si acaso cargas directamente ya en el programa #Si esta el load oculto no haria falta
        self.ids["Vol"].opacity=0
        self.ids["Vol"].disabled=True
        
        self.ids["Finalizar"].opacity=0
        self.ids["Finalizar"].disabled=True   
        
             
    

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()
        
    def siguiente(self):
        self.ids["lienzo"].canvas.clear()
        self.matreal=[] #Simu?
        
        
        
        global numimagenactual                
        global columnas
        global filas
        global numero_imagenes
        global ag
        global ap
        global matrix
        global mataux
        global listagenerador
   
        
        listagenerador=self.generador(filas,columnas)
        listagenerador= list(listagenerador)
        print (listagenerador)
        print (listagenerador[0])
                    
        #Calcular varianza real
        #cojo cpx y cpy que los necesito en el programa, y estan en pruebaguardarpiloow
        cpx,cpy=devolveresquina ()
        #print("Hola")
        #print (cpx,cpy)
        #*** Simulaciones *** self.matreal=devolvermatreal(ag,ap,filas,columnas,cpx,cpy)  #Te devuelve la matriz con el fichero
        #print (self.matreal)
        
        #print (tras(self.matreal,ag,ap)) no hace falta porque lo que necesitamos es la matriz real con los 0 de por donde vamos en la otra matriz
        
        
        #coger primero del generador
        #coger esa posicion para ver cuantas personas ahi (imagen) , el recorte de esa imagen tambien
        #coger la matriz auxiliar y rellenar con el numero del generador y el dato de la matriz real
        #Calcular la varianza de ambas        
        #diferencia= Varianza real / varianza obtenida
        #while valor diferencia > constante(x)  y num imagenes < 50% imagenes totales
            #anadir uno al indice (del generador)
            #coger esa posicion para ver cuantas personas ahi (imagen) , el recorte de esa imagen tambien - no como lo hacemos ahora ya que hay que saltar y el numimagenactual da igual
            #coger la matriz auxiliar y rellenar con el numero del generador y el dato de la matriz real
            #Calcular la varianza de ambas        
            #diferencia= Varianza real / varianza obtenida
        
        
        #print(lista[0][0]) #Ultimo 0= fila, Ultimo 1= columna
        #print (numimagenactual)
        #print(lista[numimagenactual][0])        
            
        if numimagenactual < numero_imagenes: #Si quedan imagenes por recorrer
            
            self.ids["mario"].source=os.path.join(ruta,f"recorte{listagenerador[numimagenactual][0]}_{listagenerador[numimagenactual][1]}.jpg")
            #global ag
            #global ap
            print (numimagenactual , numero_imagenes)
            
            #print (mataux [0,3])
            #print ("Fernando")
        
            #print(listagenerador[numimagenactual])
            #self.ids["lienzo"]= MyPaintWidget() #Da igual que llegue al if siguiente porque cuando llegamos al mypaintwidget se vuelve a poner en false
            
            #***Simulaciones Aqui sera donde tienes que pasar a la matriz auxiliar el dato real que aparece en la matriz real
            #mataux[listagenerador[numimagenactual]]=self.matreal[listagenerador[numimagenactual]]
            #print (mataux)
            
            #mataux es la matrix con las posiciones restantes rellenas al azar (no confundir con las simulaciones)
            
            print (matrix,"Antes de")
            
            mataux=self.rellenarmatriz(matrix, (numero_imagenes-numimagenactual) ) #Anadir el valor de posiciones vacias (Seran las imagenes(self.numero_imagenes)- las que llevamos recorridas(numimagenactual))
            
            #matrix(listagenerador[numimagenactual])+=1
            
            
            
            self.varianzareal=tras(mataux,ag,ap)
            self.varianza=tras(matrix, ag,ap)
            
            #self.varianzanueva=trasnueva(matrix, ag,ap)
           
            #print ("-----PRUEBA VARIANZA------------")
            #print (self.varianza, self.varianzanueva)
            
            
            print (mataux,"Prueba")
            print (matrix, "Prueba2") 
            
            #print (mataux is matrix)
           
            
            print ("VARIANZA MIA:"+str(self.varianza))
            print ("VARIANZA REAL:"+str(self.varianzareal))
            
            if (numimagenactual / numero_imagenes > 0.5 and (self.varianza - self.varianzareal) < 0.1* self.varianzareal):
                print (f"Numero de imagenes recorridas: {numimagenactual} \n con diferencia del {(self.varianza - self.varianzareal):.2f} ") 
                f=open('prueba.txt','a')
                f.write (f"%.2f \t %.2f\n"%(numimagenactual/numero_imagenes,abs((self.varianza - self.varianzareal)/self.varianzareal))) #Para que te saque solo 2 decimales (expresiones) #abs para el valor absoluto
                f.close()
                
                self.ids["Finalizar"].opacity=100
                self.ids["Finalizar"].disabled=False
                
                             
                #exit()       
            
            if numimagenactual>0:
                self.estimacion=(ag**2/ap**2)*matrix.sum()* (numero_imagenes/numimagenactual)  #anadido el n de cuadrados
            else:
                self.estimacion =-1
                
            coeficiente_error=self.varianzareal/self.estimacion**2
            self.ids["var_text"].text= "Coeficiente: "+str(coeficiente_error)

                
            print (ag,ap,matrix.sum(), numero_imagenes,numimagenactual)
            self.ids["var_est"].text= "Estimacion: "+str(self.estimacion)
            numimagenactual +=1

            
                
                
            
        if numimagenactual == 1:
            #print ("Hola")
            self.ids["lienzo"].pinta=True
            self.ids["Vol"].opacity=100
            self.ids["Vol"].disabled=False  
            
        if numimagenactual == numero_imagenes:
            if self.ids["Sig"].text!="Finish":
                self.ids["Sig"].text="Finish"
                print ("calcular varianza")
                self.varianza=tras(matrix,ag,ap)
                self.estimacion=(ag/ap)*matrix.sum()* (numero_imagenes/numimagenactual)
                self.ids["var_text"].text= str(self.varianza)
                self.ids["var_est"].text= str(self.estimacion)
                print (self.varianza)
                #Aqui calculas la varianza pero tendras que hacer algo mas, no ? que desaparezca el boton siguiente, ...
                #Meter los resultados en el ficghero con t,T cpx,cpy
                f=open('resultados.txt','a')
                f.write ("T: %d \n"%(ag))
                f.write ("t: %d \n"%(ap)) 
                f.write ("cpx: %d \n"%(cpx))
                f.write ("cpy: %d \n"%(cpy))
                f.write ("varianza: %.2f \n"%(self.varianza))
                f.write ("estimacion: %.2f \n"%(self.estimacion))
                f.close()
        
            else:
                shutil.rmtree(ruta) #Elimina los recortes antes de salir del programa
                exit()
                
                
    def volver(self):
        global rutafoto
        global numimagenactual
        global ap
        global matrix
        global listagenerador
        
        print ("Hola")
        
        #porque no se puede copger la lista
        
        #lo he intentado con listas y con arrays
        
       # print (listagenerador[numimagenactual])[0]      
        
        #matrix[listagenerador(numimagenactual)]=0
        
        fila=int(listagenerador[numimagenactual-1][0]) #Me quedo con la parte entera
        col= listagenerador[numimagenactual-1][1]
        
        #print (fila)
        #print (col)
        
        matrix[fila][col]=0
        
        numimagenactual -=1
        self.ids["lienzo"].canvas.clear()
        
        if numimagenactual != 0: #Si quedan imagenes por recorrer
            fila=int(listagenerador[numimagenactual-1][0]) #Me quedo con la parte entera
            col= listagenerador[numimagenactual-1][1]
            matrix[fila][col]=0 #Porqwue hay que recorrer tambien la anterior
            self.ids["mario"].source=os.path.join(ruta,f"recorte{fila}_{col}.jpg")
       
        else: #Para pasar de la primera imagen a la imagen completa y pedir otro ap
            self.ids["mario"].source=rutafoto
            self.ids["lienzo"].pinta=False
            ap = int(input("Lado Pequeno: "))
            while ap> ag:
                print("Area Pequena se sale de Area Grande")
                ap = int(input("Lado Pequeño: ")) 
            self.ids["Vol"].opacity=0
            self.ids["Vol"].disabled=True  
           
        #poner a 0 la posicion de la matriz en la que estamos
        #poner a 0 la posicion anterior a la que estamos (hay que volverla a contar)
        #valor num imagen actual hay que restarle 1
        #volver a la imagen anterior    
        
        #si el numero imagen actual es 1, volver a la imagen completa y pedir de nuevo el ap
    
    
    def reset(self):
        print("Reinicio")
        
    
    
    
    
    def generador(self,filas, columnas):
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
        return lista     
    
    def rellenarmatriz(self, matriz, vacios):
        #Funcion a la que se le pasa la matriz que llevamos recorrida, y te tiene que devolver la matriz extrapolada, transformando las posiciones no recorridas en valores posibles (Rango del minimo al maximo de las anteriores posiciones)
        print ("Extrapolar")
        print (matriz,vacios)
        
        matextra=np.matrix.copy(matriz)
        
        #co ger el maximo y el minimo de la matriz sin contar los -1
        
        maximo=np.max(matriz)
        if maximo < 1: #Para que no sea 0
            maximo=1
        minimo=0
        
        global listagenerador
        global numero_imagenes 
        
        for i in range(numero_imagenes-vacios, numero_imagenes):
            #listagenerador[i]
            matextra [listagenerador[i]]=randint (minimo, maximo)
        
        print (matextra, "Matriz extrapolada") 
        print (matriz, "Matriz no extrapolada")    
        return matextra
            

    
                
                  
    def guardarresultados(self):
            global ap
            global ag
            
            cpx,cpy=devolveresquina ()
            
            f=open('resultados.txt','a')
            f.write ("T: %d \n"%(ag))
            f.write ("t: %d \n"%(ap)) 
            f.write ("cpx: %d \n"%(cpx))
            f.write ("cpy: %d \n"%(cpy))
            f.write ("varianza: %.2f \n"%(self.varianza))
            f.write ("estimacion: %.2f \n"%(self.estimacion))
            f.close()
            
            exit() 

            

    
class MyPaintWidget(Widget):
    conjunto = set()
    contador=0
    #fila=0
    #col=0
    
    def dimensionar (self, touchx, touchy, ex, ey, cpx, cpy, ag, ap, fila, columna):
        
        print ("Inicio")
        #print (touchx,touchy)
        
        #sacar la coordenadada en la imagen dimensionada (no en el programa)
        coordx=touchx - ex
        coordy=touchy - ey
        
        #Dimensionar la imagen (area p con dimensiones por defecto 600,00)
        #print(self.size)
        coordx=coordx*ap/self.size[0] #anchura del cuadrado en el que se presenta la imagen (x)
        coordy=coordy*ap/self.size[1] #altura del cuadrado en el que se presenta la imagen (y)
        
        #Poner la coordenada repsecto al ag
        coordx=coordx+cpx
        coordy=coordy+cpy
        
        #Sabiendo la fila y la columna poner la coordenada real en la imagen
        global filas
        filaaux=filas-1-fila #filaaux para coger la fila para calcular bien la coordenada empezando desde arriba
        coordx=coordx+ag*columna
        coordy=coordy+ag*filaaux
        
        
        print ("FINAL")
        #print (coordx,coordy)
        f=open('coordenadas.txt','a')
        f.write ("%.2f \t %.2f\n"%(coordx,coordy)) #Para que te saque solo 2 decimales (expresiones)
        f.close()
        
        pass
    
    
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            print("TOuch %.2f %.2f"%( touch.x,touch.y),self.contador)
            if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0] and touch.y > self.pos[1] and touch.y < self.pos[1] + self.size[1] and self.pinta:
                self.contador +=1
                self.conjunto.add((touch.x,touch.y))
                d = 10.
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                global listagenerador
                fila=int(listagenerador[numimagenactual-1][0]) #Me quedo con la parte entera
                col= listagenerador[numimagenactual-1][1]
                print("prueba")
                print(fila,col, numimagenactual)
                global matrix
                print(matrix)
                matrix[fila][col]+=1 #matrix[fila][col]+ 1
                cpx,cpy= devolveresquina ()
                print (self.pos[0], self.pos[1], cpx , cpy , ag , ap , fila,col)
                self.dimensionar(touch.x,touch.y, self.pos[0], self.pos[1], cpx, cpy, ag, ap, fila,col)
                
                #Color(0, 0, 0) #Para quitar el amarillo del mario
                #Rectangle()#(source="mario.png")
                #print(self.conjunto)
            #print(fila,col)
            print(matrix)
        
            #print(self.nec,self.nec2)
            
    

class Editor(App):
    pass
#    def build(self):
#        return MyPaintWidget()




Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    if os.path.exists(ruta):
        shutil.rmtree(ruta)
    Editor().run()
    shutil.rmtree(ruta)
    
    #print ('borrar recortes')
