from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle
from  pruebaguardarpillow5 import *
from  calculavarianzacompuesta import *
import shutil # Libreria para borrar los recortes
		

import os


ruta= "."
ruta= os.path.join(ruta,"Recortes")

matrix=[]
print ("matrix")
numimagenactual =0 #El anterior contador de la imagen por la que ibamos no la pongo porque da fallos extranhos
columnas=0 
filas=0
ag=0
ap=0

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
			
			
		self.ids["mario"].source=filename[0]
		self.ids["var_text"].text= "20"
	    
		self.dismiss_popup()
		
		#Hacer aqui el pop up del area pequena
		
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
		ap = int(input("Area Pequeña: "))
		#ap=25
		#self.ids["lienzo"].pinta=True
		global filas
		global columnas
		self.numero_imagenes, filas, columnas=recortar_imagen(ag, ap, rutafoto)
		global matrix
		matrix=np.zeros((filas, columnas)) #
		print(matrix)
		
    

	def save(self, path, filename):
		with open(os.path.join(path, filename), 'w') as stream:
			stream.write(self.text_input.text)

		self.dismiss_popup()
		
	def siguiente(self):
		self.ids["lienzo"].canvas.clear()
		
		global numimagenactual				
		global columnas
							
		if numimagenactual < self.numero_imagenes:
			
			self.ids["mario"].source=os.path.join(ruta,f"recorte{numimagenactual//columnas}_{numimagenactual%columnas}.jpg")
			numimagenactual +=1
			global ag
			global ap
			print (numimagenactual , self.numero_imagenes)
			#self.ids["lienzo"]= MyPaintWidget() #Da igual que llegue al if siguiente porque cuando llegamos al mypaintwidget se vuelve a poner en false
			self.varianza=tras(matrix,ag,ap)
			self.ids["var_text"].text= str(self.varianza)
			
			self.estimacion=(ag/ap)*matrix.sum()* (self.numero_imagenes/numimagenactual)  #anadido el n de cuadrados
			print (ag,ap,matrix.sum(), self.numero_imagenes,numimagenactual)
			self.ids["var_est"].text= str(self.estimacion)
			
				
				
			
		if numimagenactual == 1:
			#print ("Hola")
			self.ids["lienzo"].pinta=True
			
		if numimagenactual == self.numero_imagenes:
			if self.ids["Sig"].text!="Finish":
				self.ids["Sig"].text="Finish"
				print ("calcular varianza")
				self.varianza=tras(matrix,ag,ap)
				self.estimacion=(ag/ap)*matrix.sum()* (self.numero_imagenes/numimagenactual)
				self.ids["var_text"].text= str(self.varianza)
				self.ids["var_est"].text= str(self.estimacion)
				print (self.varianza)
			#Aqui calculas la varianza pero tendras que hacer algo mas, no ? que desaparezca el boton siguiente, ...
		
			else:
				shutil.rmtree(ruta) #Elimina los recortes antes de salir del programa
				exit()
			

	
class MyPaintWidget(Widget):
	conjunto = set()
	contador=0
	#fila=0
	#col=0
	
	def dimensionar (self, touchx, touchy, ex, ey, cpx, cpy, ag, ap, fila, columna):
		
		print ("Inicio")
		print (touchx,touchy)
		
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
		print (coordx,coordy)
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
			    fila=int((numimagenactual-1)/columnas) #Me quedo con la parte entera
			    col= (numimagenactual-1)%columnas
			    print("prueba")
			    print(fila,col, numimagenactual)
			    global matrix
			    print(matrix)
			    matrix[fila][col]+=1 #matrix[fila][col]+ 1
			    cpx,cpy= devolveresquina ()
			    self.dimensionar(touch.x,touch.y, self.pos[0], self.pos[1], cpx, cpy, ag, ap, fila,col)
			    
				#Color(0, 0, 0) #Para quitar el amarillo del mario
				#Rectangle()#(source="mario.png")
				#print(self.conjunto)
			#print(fila,col)
			print(matrix)
		
			#print(self.nec,self.nec2)

class Editor(App):
	pass
#	def build(self):
#		return MyPaintWidget()




Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
	if os.path.exists(ruta):
		shutil.rmtree(ruta)
	Editor().run()
	shutil.rmtree(ruta)
	
    #print ('borrar recortes')
