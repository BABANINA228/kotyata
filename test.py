from kivymd.app import MDApp

class Myapp(MDApp):
    def build(self):
        return
    def get_data(self):
        print("The data of text field is :: ",self.root.ids.data.text)

Myapp().run()