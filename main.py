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

class CloseAddTaskMenu(Button):
    pass

class TaskListApp(MDApp):
    def build(self):
        # создаем главный
        self.root = RootLayout(orientation='vertical')
        self.add_tasks_root()
        self.add_bot_menu()
        return self.root

    def add_tasks_root(self):
        tasks_root = RootLayout(orientation='vertical')

        h_line1 = HLine(height=1, size_hint=(1, None))

        task_container = ScrollView()

        self.task_list = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))

        # создаем горизонтальный контейнер, который будет хранить поле ввода и кнопку добавления
        input_container = RootLayout(orientation='horizontal', height='60', size_hint=(1, None), padding=(10, 10),
                                     spacing=10)

        # создаем поле ввода и кнопку добавления
        global input_field
        input_field = RoundedInput()
        input_field.add_widget(Button(text=''))
        add_button = AddButton(on_press=lambda x: self.add_task(input_field.text), size=(48, 33),
                               size_hint=(None, None))

        # добавляем поле ввода и кнопку добавления в контейнер

        # Упаковываем страницу задач
        tasks_root.add_widget(task_container)
        task_container.add_widget(self.task_list)
        input_container.add_widget(input_field)
        input_container.add_widget(add_button)
        tasks_root.add_widget(h_line1)
        tasks_root.add_widget(input_container)

        self.root.add_widget(tasks_root)

    def add_bot_menu(self):
        h_line2 = HLine(height=1, size_hint=(1, None))
        self.root.add_widget(h_line2)
        bot_menu = InvLayout(orientation='horizontal', height='75', size_hint=(1, None), spacing=10)
        tasks_button = Image(source='tasks.png', height='75', size_hint=(1, None))
        calendar_button = Image(source='calendar.png', height='75', size_hint=(1, None))
        notes_button = Image(source='Notes.png', height='75', size_hint=(1, None))
        bot_menu.add_widget(tasks_button)
        bot_menu.add_widget(calendar_button)
        bot_menu.add_widget(notes_button)

        self.root.add_widget(bot_menu)

    def open_add_task_menu(self):
        close = CloseAddTaskMenu()
        self.root.add_widget(close)

    def add_task(self, task_text):
        task = TaskCont(cols=1, rows=2, size_hint_y=None, padding=10, pos=(0, 50))
        task_buble = TaskLayout(orientation='vertical', size_hint=(1, None))

        task_rare = GridLayout(cols=2, rows=1)
        task_stars = TaskLayout(orientation='horizontal', width=90, size_hint=(None, 1))
        for i in range(3):
            task_stars.add_widget(Image(source='Star_point.png', size=(30, 30)))
        task_time_container = TaskLayout(orientation='horizontal')
        task_time_label = Label(text='19:30', color='black', font_name='Inter-ExtraLight', font_size=18)
        task_time_icon = Image(source='clock.png')
        task_time = TaskLayout(size_hint_x=None, width=90)

        task_time.add_widget(task_time_icon)
        task_time.add_widget(task_time_label)

        task_time_container.add_widget(task_time)
        task_rare.add_widget(task_time_container)
        task_rare.add_widget(task_stars)
        task_buble.add_widget(task_rare)

        task_name_container = TaskLayout()
        task_name = Label(text=task_text, color='black', font_name='Inter-ExtraLight', font_size=15, halign='left',
                          size_hint=(1, 1))
        task_name_container.add_widget(task_name)
        task_buble.add_widget(task_name_container)
        task.add_widget(task_buble)
        self.task_list.add_widget(task)

        input_field.text = ''


if __name__ == '__main__':
    TaskListApp().run()
