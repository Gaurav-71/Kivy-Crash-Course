from os import name
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
import kivy
kivy.require('2.0.0')  # replace with your current kivy version !


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        self.top_grid.add_widget(
            Label(text="Name : "))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(
            Label(text="Fav Pizza : "))
        self.pizza = TextInput(
            multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(
            Label(text="Fav Color : "))
        self.color = TextInput(
            multiline=False)
        self.top_grid.add_widget(self.color)

        self.add_widget(self.top_grid)

        self.submit = Button(text="Submit", size_hint_y=None, height=100)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        self.add_widget(
            Label(text=f'Hello {name}, your fav pizza is {pizza} & fav color is {color}'))


class MyApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
