 
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label 
from kivy.uix.image import Image
from kivy.lang import Builder

Window.clearcolor = (1,1,1,1)
Window.size = (400,600)
class Myapp(App):
    def build(self):
        self.title="Home Page"
        self.window= Screen()
        self.img1 = Image(source="img1.jpg" , size_hint=(0.5 , 0.5) , pos_hint= {"center_x":0.5 , "center_y":0.85})
        self.img2 = Image(source="img2.jpg" , size_hint=(0.2 , 0.2) , pos_hint= {"center_x":0.5 , "center_y":0.10})
        self.label1 = Label(text="New Vision" , pos_hint = {"center_x":0.5 , "center_y":0.96}, halign="center", valign="center" , color=(0,0,0.66,1))
        self.label2 = Label(text="Welcome to New Vision App\nthe app aim to help people who have color\ndeficiency to have a better vision of the objects color" , pos_hint = {"center_x":0.5 , "center_y":0.72}, halign="center", valign="center" , color=(0,0,0.66,1))
        self.label3 = Label(text="Please choose from the types below" , pos_hint = {"center_x":0.5 , "center_y":0.64}, halign="center", valign="center" , color=(144,160,189,1))
        self.label4 = Label(text="Graduation Project \nComputer Science" , pos_hint = {"center_x":0.5 , "center_y":0.20}, halign="center", valign="center" , color=(0,0,0.66,1))
        self.button1 = Button(text="Deuteranomaly" , size_hint=(0.4 , 0.0600) , pos_hint = {"center_x":0.5 , "center_y":0.56} , color=(1,1,1,1) , background_color=(0,0,0.99,1))
        self.button2 = Button(text="Protanopia" , size_hint=(0.4 , 0.0600) , pos_hint = {"center_x":0.5 , "center_y":0.46}, color=(1,1,1,1) , background_color=(0,0,0.99,1))
        self.button3 = Button(text="Tritanopia" , size_hint=(0.4 , 0.0600) , pos_hint = {"center_x":0.5 , "center_y":0.36}, color=(1,1,1,1) , background_color=(0,0,0.99,1))


        self.window.add_widget(self.img1)
        self.window.add_widget(self.img2)
        self.window.add_widget(self.label1)
        self.window.add_widget(self.label2)
        self.window.add_widget(self.label3)
        self.window.add_widget(self.label4)
        self.window.add_widget(self.button1)
        self.window.add_widget(self.button2)
        self.window.add_widget(self.button3)

        return self.window


if __name__ == '__main__':
    Myapp().run()
