from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty, NumericProperty, StringProperty, DictProperty
from kivy.lang import Builder

Builder.load_string('''
#-------------------------------
#  SpinnerKnob class
#  
#
#-------------------------------
<SpinnerKnob>
    color: [144/255, 228/255, 1, 1]
 
#-------------------------------
''')


class SpinnerKnob(Spinner):
    addresses = ListProperty([])

    def set_knob(self, adr, value):
        self.text = self.values[value]


if __name__ == '__main__':
    kv_test = '''
BoxLayout:
    orientation: 'vertical'
    SpinnerKnob:
        text: 'Whole'
        values:['0-100', 'Whole', 'Dotted Half', 'Triplet Whole', 'Half', 'Dotted Qtr', 'Triplet of Half', 'Qtr', 'Dotted 8th', 'Triplet of Qtr', '8th', 'Dotted 16th','Triplet of 8th', '16th', 'Dotted 32th', 'Triplet of 16th', '32th']   
        addresses:[0x22]
        on_text: print(self.values.index(self.text)) 
    SpinnerKnob:
        text: 'Three'
        values:['One', 'Two', 'Three', 'Four']
        on_text: print(self.values.index(self.text)) 
    SpinnerKnob:
        text: 'a'
        values: ['a','b','c']
        on_text: print(self.values.index(self.text))  
              
    '''


    class SpinnerKnobApp(App):

        def build(self):
            return Builder.load_string(kv_test)


    SpinnerKnobApp().run()
