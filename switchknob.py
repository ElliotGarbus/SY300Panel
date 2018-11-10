from kivy.app import App
from kivy.uix.switch import Switch
from kivy.properties import ListProperty
from kivy.lang import Builder

Builder.load_string('''
#-------------------------------
#  SwitchKnob class
#  
#
#-------------------------------
<SwitchKnob>


#-------------------------------
''')


class SwitchKnob(Switch):
    addresses = ListProperty([])

    def set_knob(self, adr, value):
        self.active = value


if __name__ == '__main__':
    kv_test = '''
BoxLayout:
    orientation: 'vertical'
    SwitchKnob:
        on_active: print('switch 1 value is:', self.active)
        
    SwitchKnob:
        on_active: print('switch 2 value is:', self.active)
      
    SwitchKnob:
        on_active: print('switch 3 value is:', self.active)

    '''


    class SwitchKnobApp(App):

        def build(self):
            return Builder.load_string(kv_test)


    SwitchKnobApp().run()
