import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text='Hello world!')

if __name__ == '__main__': #this if statement is used so that if the .py file itself is run, it runs as a program, but not if imported as library
    HelloApp().run()
