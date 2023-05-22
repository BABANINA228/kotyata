from kivy.uix.scatter import Scatter
from kivy.app import App
from kivy.graphics.svg import Svg
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


Builder.load_string("""
<SvgWidget>:
    do_rotation: False
<FloatLayout>:
    canvas.before:
        Color:
            rgb: (1, 1, 1)
        Rectangle:
            pos: self.pos
            size: self.size
""")

class SvgWidget(Scatter):
    def __init__(self, filename):
        super(SvgWidget, self).__init__()
        with self.canvas:
            svg = Svg(filename)
        self.size = svg.width, svg.height


class SvgApp(App):
    def build(self):
        self.root = FloatLayout()

        filename = "plus.svg"
        svg = SvgWidget(filename)
        self.root.add_widget(svg)
        svg.scale = 2


if __name__ == '__main__':
    SvgApp().run()