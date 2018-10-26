import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
kivy.require('1.10.1')
import xy

'''
Tiny input test app
Created by Seth Abraham, October 4, 2018

'''

Builder.load_string('''

#:kivy 1.10.1
#

# from float
<TTest>:
    XYKnob:
        id: knob
        size_hint: None,None
        size: 600,600

    Button:
        pos: ( 650, 0 )
        size_hint: None,None
        size: 150,150
        text: 'Click me'
        on_press: root.ids.knob.size = (root.ids.knob.width-50, root.ids.knob.height-50 )
    Button:
        pos: ( 650, 200 )
        size_hint: None,None
        size: 150,150
        text: 'Eat me'
        on_press: root.ids.knob.size = (root.ids.knob.width+50, root.ids.knob.height+50 )
''')


class TTest(FloatLayout):
    pass

class TTestApp(App):
    def build(self):
        r = TTest()
        #print(r.ids)
        #print("labels in app:  ",r.ids.keys())

        return r


if __name__ == '__main__':
    TTestApp().run()
