from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Introduce Area Pequena'
    TextInput:
        id: areapequena
        text: ''
        multiline: False
        on_text_validate: pop.dismiss()
''')
#textinput = TextInput(text='Hello world')


class SimplePopup(Popup):
    pass

class SimpleButton(Button):
    text = "Area Pequena"
    def fire_popup(self):
        pops=SimplePopup()
        pops.open()
        print(pops.ids["areapequena"].text)

class SampleApp(App):
    def build(self):
        return SimpleButton()

SampleApp().run()