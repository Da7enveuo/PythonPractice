import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class myfirstkivyapp(App):
    def build(self):
        return Grid()

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 8
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="Number: "))
        self.number = TextInput(multiline=False)
        self.add_widget(self.number)


if __name__ == '__main__':
    myfirstkivyapp().run()
