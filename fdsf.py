from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField

# Создаем кроссплатформенное с помощью Builder
Builder.load_string("""
<MyTextInput>:
    orientation: 'horizontal'
    size_hint_y: None
    height: dp(48)
    MDTextField:
        id: text_input
        hint_text: "Введите текст"
    MDIconButton:
        icon: "icon1.png"
        on_release: root.icon1_click()
    MDIconButton:
        icon: "icon2.png"
        on_release: root.icon2_click()
""")

# Создаем пользовательский класс с нашими виджетами
class MyTextInput(MDBoxLayout):
    def icon1_click(self):
        # Когда нажата кнопка icon1.png
        print("Нажата кнопка icon1.png")

    def icon2_click(self):
        # Когда нажата кнопка icon2.png
        print("Нажата кнопка icon2.png")


# Создаем основной класс приложения для вывода пользовательского интерфейса
class MyApp(MDApp):
    def build(self):
        return MyTextInput()

# Запускаем приложение
if __name__ == '__main__':
    MyApp().run()