from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ColorProperty
from kivy.lang import Builder
from kivymd.uix.gridlayout import GridLayout

# from kivy.core.window import

Builder.load_file('bg.kv')


class TaskLayout(BoxLayout):
    pass


class HelloWorldApp(App):
    def build(self):
        task = GridLayout(cols=2, size_hint_y = None)

        task_buble = TaskLayout(orientation='horizontal', size_hint=(1, None))

        task_name = Label(text='llll', size_hint=(1.5, 1))
        task_buble.add_widget(task_name)

        task_rare = TaskLayout(orientation='vertical', size_hint=(.5, 1))

        task_stars = TaskLayout(orientation='horizontal')
        for i in range(5):
            task_stars.add_widget(Label(text="*", font_size=20, color='yellow'))
        task_rare.add_widget(task_stars)

        task_time = Label(text='19:30')
        task_rare.add_widget(task_time)

        task_buble.add_widget(task_rare)

        task.add_widget(task_buble)
        return task


if __name__ == '__main__':
    HelloWorldApp().run()
