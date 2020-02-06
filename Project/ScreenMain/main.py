#To display and to get user name and password from the user, to get access

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.properties import OptionProperty

class layout(BoxLayout):
    pass

class Screen(App):
    def build(self):
        return layout()

if __name__ == "__main__":
    Screen().run()
