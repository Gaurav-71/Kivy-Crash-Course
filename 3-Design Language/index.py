from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.app import App
import kivy
kivy.require('2.0.0')  # replace with your current kivy version !


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        # self.add_widget(
        # Label(text=f'Hello {name}, your fav pizza is {pizza} & fav color is {color}'))
        print(f'Hello {name}, your fav pizza is {pizza} & fav color is {color}')
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class Design(App):

    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    Design().run()
