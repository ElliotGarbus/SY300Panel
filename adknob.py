from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        Button:
            text:'PL'        
        Button:
            text: 'Square Pad'
            size_hint_x: None
            width: self.size[1]
        Button:
            text: 'PR'
    Button:
        text: 'Label goes here'
        size_hint_y: None
        height: self.texture_size[1]

'''


class ADKnobApp(App):

    def build(self):
        return Builder.load_string(kv)

ADKnobApp().run()

