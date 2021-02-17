from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
import kivy
kivy.require('2.0.0')  # replace with your current kivy version !

Builder.load_file('css.kv')


class MyGridLayout(Widget):
    color = "#FF0000"


class Design(App):

    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    Design().run()
