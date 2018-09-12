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
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
        #self.ids["var_text"].text= "20"

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        print(filename[0])
        self.ids["mario"].source=filename[0]
        self.ids["var_text"].text= "20"
		
        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()
		
    def siguiente(self):
	    self.ids["mario"].source="portero.jpg"
	#   contador +=1

	

class MyPaintWidget(Widget):
	conjunto = set()
	contador=0
	def on_touch_down(self, touch):
		with self.canvas:
			Color(1, 1, 0)
			print("TOuch %.2f %.2f"%( touch.x,touch.y),self.contador)
			self.contador +=1
			self.conjunto.add((touch.x,touch.y))
			d = 10.
			Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			Rectangle(source="mario.png")
			print(self.conjunto)

class Editor(App):
	pass
#	def build(self):
#		return MyPaintWidget()




Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    #rutafoto = 'c:\\Users\\User\\Desktop\\TFG\\Datos\\Fig1A_original.jpg'
    #ag=500
    #ap=25
    recortar_imagen(ag, ap, rutafoto)
    Editor().run()
    #print ('borrar recortes')
    shutil.rmtree("Recortes")
