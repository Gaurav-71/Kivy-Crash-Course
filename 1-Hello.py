from kivy.uix.label import Label
from kivy.app import App
import kivy
kivy.require('2.0.0')  # replace with your current kivy version !


class MyApp(App):

    def build(self):
        return Label(text='Hello world', font_size=100)


if __name__ == '__main__':
    MyApp().run()
