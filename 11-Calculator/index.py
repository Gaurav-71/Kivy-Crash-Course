from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
import kivy
kivy.require('2.0.0')  # replace with your current kivy version !

Window.size = (500, 700)

Builder.load_file('Design.kv')


class MyLayout(Widget):
    pass


class Calculator(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Calculator().run()
