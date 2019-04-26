'''
Created on 15 mar. 2019

@author: User
'''
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.button import Button


from kivy.uix.textinput import TextInput
textinput = TextInput(text='Hello world')

class SampleApp(App):
    def build(self):
        return textinput

SampleApp().run()