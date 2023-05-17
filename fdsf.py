from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyLabel(Label):
    pass

class MyButton(Button):
    pass

class MyApp(App):
    def build(self):
        label = MyLabel(text='Hello World!', font_size=48)
        button = MyButton(text='Click me!', size_hint=(.5, .5), pos_hint={'x':.25, 'y':.25})
        label.add_widget(button)
        return label

if __name__ == '__main__':
    MyApp().run()