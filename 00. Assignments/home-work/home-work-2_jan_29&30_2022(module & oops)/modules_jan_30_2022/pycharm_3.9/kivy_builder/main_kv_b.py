import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("style.kv")

class MyGrid (Widget):
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    edu = ObjectProperty(None)

    def press(self):
        name = self.name.text
        age = self.age.text
        edu = self.edu.text
        disp_str = "Name: " + str(name) + ", Age: " + str(age) + ", Education: " + str(edu)
        # add widgets
        print(disp_str)
        self.clear()

    def clear(self):
        self.name.text = ""
        self.age.text = ""
        self.edu.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()