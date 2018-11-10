from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ListProperty
from kivy.lang import Builder

Builder.load_string('''
#-------------------------------
#  ToggleKnob class
#  
#
#-------------------------------
<ToggleKnob>


#-------------------------------
''')


class ToggleKnob(ToggleButton):
    addresses = ListProperty([])

    def set_knob(self, adr, value):
        self.state = 'normal' if not value else 'down'


if __name__ == '__main__':
    kv_test = '''
BoxLayout:
    orientation: 'vertical'
    ToggleKnob:
        text: 'Push me'
        on_state: print('switch 1 value is:', self.state)

    ToggleKnob:
        text: "really, I mean it!"
        on_state: print('switch 2 value is:', self.state)

    ToggleKnob:
        text: "I dare you"
        on_state: print('switch 3 value is:', self.state)

    '''


    class ToggleKnobApp(App):

        def build(self):
            return Builder.load_string(kv_test)


    ToggleKnobApp().run()
