from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


# Designate Our .kv design file
Builder.load_file('bg.kv')
женя хуесос


class TaskLayout(BoxLayout):
    pass


class AwesomeApp(App):
    def build(self):
        root = BoxLayout()
        gg = TaskLayout()
        root.add_widget(gg)
        return root


if __name__ == '__main__':
    AwesomeApp().run()