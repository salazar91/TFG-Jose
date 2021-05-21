import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty 
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from sqlalchemy.sql.expression import except_
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class Widgets(GridLayout):
    def btn(self):
        show_popup(self)

class P(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        return Widgets()


def show_popup(x):
    
    show = P()
    #print (int((x.ids["txtinput"].text))) #Si metes algo que no es un entero va a ir a la edxcepcion
    
    popupWindow = Popup(title="Lado Pequeno",  content=show, size_hint=(None,None), size=(400,400), auto_dismiss=True)
    show.ids["cerrar"].bind(on_release=popupWindow.dismiss)
    try:
        temp=int(x.ids["txtinput"].text)
        show.ids["mensaje"].text="Actualizado a:"+str(temp)
        #Comprobacion de si ap > ag
        #popupWindow.text=x.ids["txtinput"].text
        
        #text=f'{int((x.ids["txtinput"].text))}',
    except ValueError:
        show.ids["mensaje"].text="Error"
        show.ids["cerrar"].text="Reintentar"
        
        #popupWindow = Popup(title="Ha habido un error", content=show, size_hint=(None,None), size=(400,400))
    #if  show.ids["cerrar"].text="Reintentar" que vuelva al pop up, sino que guarde la variable - con un while al principio mejor
    popupWindow.open()
    

if __name__ == "__main__":
    MyApp().run()
    
"""    

popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400))
"""