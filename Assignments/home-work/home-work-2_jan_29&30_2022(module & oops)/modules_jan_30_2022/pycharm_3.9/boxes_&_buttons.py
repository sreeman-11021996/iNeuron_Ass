import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialize the input
    def __init__(self, **kwargs):
        # call gridlayout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set the columns
        self.cols = 1



        #1st row -> the inside grid
        self.inside = GridLayout()
        self.inside.cols = 2

        # add widgets
        self.inside.add_widget(Label(text="Name: ",font_size=32))
        # text input
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        # add widgets
        self.inside.add_widget(Label(text="Age: ", font_size=32))
        # text input object
        self.age = TextInput(multiline=False)
        self.inside.add_widget(self.age)

        # add widgets
        self.inside.add_widget(Label(text="Education: ", font_size=32))
        # text input object
        self.edu = TextInput(multiline=False)
        self.inside.add_widget(self.edu)

        # add the inside grid to add widget
        self.add_widget(self.inside)

        

        # 2nd row-> of the outside grid
        # add widgets - buttons object
        self.submit = Button(text="Submit",font_size=32)
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    # when press in called it passes an instance of the button being pressed and gridlayout here
    def press (self,instance):
        name = self.name.text
        age = self.age.text
        edu = self.edu.text
        disp_str = "Name: " + str(name) + ", Age: " + str(age) + ", Education: " + str(edu)
        # add widgets
        self.add_widget(Label(text=disp_str))
        self.clear()

    def clear (self):
        self.name.text = ""
        self.age.text = ""
        self.edu.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
