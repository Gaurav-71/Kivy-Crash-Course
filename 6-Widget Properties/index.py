from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.app import App
import kivy
kivy.require('2.0.0')  # replace with your current kivy version !


class MyLayout(Widget):
    pass


class Design(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Design().run()
