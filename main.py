from kivy.uix.image import Image
from kivymd.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivymd.uix.textfield import MDTextField



Builder.load_file('bg.kv')


class TaskLayout(BoxLayout):
    pass

class RoundedInput(MDTextField):
    pass
class RootLayout(BoxLayout):
    pass

class InvLayout(BoxLayout):
    pass

class AddButton(Button):
    pass

class TaskCont(GridLayout):
    pass

class HLine(Label):
    pass

class TaskListApp(MDApp):
    def build(self):
        # создаем главный вертикальный контейнер
        # Builder.load_file('bg.kv')

        root = RootLayout(orientation='vertical')
        h_line1 = HLine( height=1, size_hint=(1, None))
        h_line2 = HLine(height=1, size_hint=(1, None))

        task_container = ScrollView()


        self.task_list = GridLayout(cols=1, size_hint_y = None, spacing=10)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))


        # создаем горизонтальный контейнер, который будет хранить поле ввода и кнопку добавления
        input_container = RootLayout(orientation='horizontal', height='60', size_hint=(1, None), padding=(10, 10), spacing=10)

        # создаем поле ввода и кнопку добавления
        input_field = RoundedInput()
        add_button = AddButton(on_press=lambda x: self.add_task(input_field.text), size=(48, 33), size_hint=(None, None))

        # добавляем поле ввода и кнопку добавления в контейнер


        # добавляем в главный контейнер список задач

        bot_menu = InvLayout(orientation='horizontal', height='70', size_hint=(1, None), padding=(10, 10), spacing=10)


        tasks_button = Button()


        # Упаковываем
        root.add_widget(task_container)
        task_container.add_widget(self.task_list)
        input_container.add_widget(input_field)
        input_container.add_widget(add_button)
        root.add_widget(h_line1)
        root.add_widget(input_container)
        root.add_widget(h_line2)
        root.add_widget(bot_menu)

        return root

    def add_task(self, task_text):
        task = TaskCont(cols=2, size_hint_y=None, padding=10)

        task_buble = TaskLayout(orientation='horizontal', size_hint=(1, None))

        task_name = Label(text=task_text, size_hint=(1.5, 1), color='black', font_name='Inter-ExtraLight', font_size=15)
        task_buble.add_widget(task_name)

        task_rare = TaskLayout(orientation='vertical', width=90, size_hint=(None, None))

        task_stars = TaskLayout(orientation='horizontal', width=90, size_hint=(None, 1))
        for i in range(5):
            task_stars.add_widget(Image(source='Star_point.png', size=(30, 30)))
        task_rare.add_widget(task_stars)

        task_time = Label(text='19:30', color='black', font_name='Inter-ExtraLight', font_size=18)
        task_rare.add_widget(task_time)

        task_buble.add_widget(task_rare)

        task.add_widget(task_buble)
        self.task_list.add_widget(task)


if __name__ == '__main__':
    TaskListApp().run()