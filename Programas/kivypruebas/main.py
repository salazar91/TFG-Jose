from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle
from  pruebaguardarpillow4 import *
import shutil # Libreria para borrar los recortes
		

import os

#class Boton(Button):

class SimplePopup(Popup):
    pass
	

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



            self.ids["mario"].source=filename[0]
            self.ids["var_text"].text= "20"

            self.dismiss_popup()
            pops= SimplePopup()
            pops.open()
            rutafoto = (filename[0])
            ag = int(input("Area Grande: "))
            #ag=500
            ap = int(input("Area Pequeña: "))
            #ap=25
            #self.ids["lienzo"].pinta=True
            self.numero_imagenes=recortar_imagen(ag, ap, rutafoto)
    

	def save(self, path, filename):
		with open(os.path.join(path, filename), 'w') as stream:
			stream.write(self.text_input.text)

		self.dismiss_popup()
		
	def siguiente(self):
            self.ids["lienzo"].canvas.clear()
            if self.contador < self.numero_imagenes:
                    self.ids["mario"].source=f"./{str(self.contador)}.jpg"
                    self.contador +=1
                    print (self.contador)
                    #self.ids["lienzo"]= MyPaintWidget() #Da igual que llegue al if siguiente porque cuando llegamos al mypaintwidget se vuelve a poner en false

            if self.contador == 1:
                    #print ("Hola")
                    self.ids["lienzo"].pinta=True
		

	

class MyPaintWidget(Widget):
	conjunto = set()
	contador=0
	def on_touch_down(self, touch):
		with self.canvas:
			Color(1, 1, 0)
			print("TOuch %.2f %.2f"%( touch.x,touch.y),self.contador)
			if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0] and touch.y > self.pos[1] and touch.y < self.pos[1] + self.size[1] and self.pinta:
			    self.contador +=1
			    self.conjunto.add((touch.x,touch.y))
			    d = 10.
			    Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			#Color(0, 0, 0) #Para quitar el amarillo del mario
			#Rectangle()#(source="mario.png")
			print(self.conjunto)

class Editor(App):
	pass
#	def build(self):
#		return MyPaintWidget()




Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
	if os.path.exists("Recortes"):
		shutil.rmtree("Recortes")
	Editor().run()
	shutil.rmtree("Recortes")
	
    #print ('borrar recortes')
