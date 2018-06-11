import os
os.environ['KIVY_TEXT'] = 'pil'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle


class MyPaintWidget(Widget):
	conjunto = set()
	def on_touch_down(self, touch):
		with self.canvas:
			Color(1, 1, 0)
			print("TOuch %.2f %.2f"%( touch.x,touch.y))
			self.conjunto.add((touch.x,touch.y))
			d = 10.
			Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			Rectangle(source="mario.png")
		    

class MyPaintApp(App):

    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()
