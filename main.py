from kivy.uix.textinput import TextInput
from kivymd.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

Builder.load_file('bg.kv')


class TaskLayout(BoxLayout):
    pass

class RootLayout(BoxLayout):
    pass

class AddButton(Button):
    pass
class TaskListApp(MDApp):
    def build(self):
        # создаем главный вертикальный контейнер
        # Builder.load_file('bg.kv')

        root = RootLayout(orientation='vertical')


        task_container = ScrollView()
        root.add_widget(task_container)

        self.task_list = GridLayout(cols=1, size_hint_y = None, spacing=10)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        task_container.add_widget(self.task_list)

        # создаем горизонтальный контейнер, который будет хранить поле ввода и кнопку добавления
        input_container = BoxLayout(orientation='horizontal', height='60', size_hint=(1, None), padding=(10, 10), spacing=10)

        # создаем поле ввода и кнопку добавления
        input_field = TextInput()
        add_button = AddButton(text='+', on_press=lambda x: self.add_task(input_field.text), size_hint=(None, 1), padding=(10, 10))

        # добавляем поле ввода и кнопку добавления в контейнер
        input_container.add_widget(input_field)
        input_container.add_widget(add_button)

        # добавляем в главный контейнер список задач
        root.add_widget(input_container)



        return root

    def add_task(self, task_text):
        task = GridLayout(cols=2, size_hint_y=None, padding=10)

        task_buble = TaskLayout(orientation='horizontal', size_hint=(1, None))

        task_name = Label(text=task_text, size_hint=(1.5, 1))
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
        self.task_list.add_widget(task)


if __name__ == '__main__':
    TaskListApp().run()