from kivy.app import App

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
        task = GridLayout(cols=2, size_hint_y=None, padding=10)

        task_buble = TaskLayout(orientation='horizontal', size_hint=(1, None))

        task_name = Label(text=task_text, size_hint=(1.5, 1), color='black', font_name='Inter-ExtraLight', font_size=15)
        task_buble.add_widget(task_name)

        task_rare = TaskLayout(orientation='vertical', width=50, size_hint=(None, None))

        task_stars = TaskLayout(orientation='horizontal', width=50, size_hint=(None, 1))
        for i in range(5):
            task_stars.add_widget(Label(text="*", font_size=20, color='yellow'))
        task_rare.add_widget(task_stars)

        task_time = Label(text='19:30', color='black', font_name='Inter-ExtraLight', font_size=18)
        task_rare.add_widget(task_time)

        task_buble.add_widget(task_rare)

        task.add_widget(task_buble)


if __name__ == '__main__':
    AwesomeApp().run()