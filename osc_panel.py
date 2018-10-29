from kivy.app import App
from kivy.lang import Builder

kv = """
#:import XYKnob xyknob
#:import CircleKnob circleknob
GridLayout: # Comment to force push
    rows: 3
    cols: 4
    padding: 5
    GridLayout:
        rows: 2
        cols: 5
        BoxLayout:
            orientation: 'vertical'
            Spinner:
                text: 'SAW'
                values: ['SIN', 'SAW', 'TRI', 'SQR', 'PWM', 'DETUNE SAW', 'NOISE', 'INPUT']
            Label:
                text:''
        CircleKnob:
            knob_title: 'PITCH'
        CircleKnob:
            knob_title: 'FINE'
        CircleKnob:
            knob_title: 'PULSE WIDTH'
        CircleKnob:
            knob_title: 'DETUNE'
        CircleKnob:
            knob_title: 'SHARPNESS'
        
        XYKnob:
            xy_knob_title:' PWM ENV '   # we space pad the title so it is about the same length as other titles
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        XYKnob:
            xy_knob_title:'PITCH ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        CircleKnob:
            knob_title: 'PBEND DEPTH'
        CircleKnob:
            knob_title: 'PBEND CTL'
        
    Button:
        text: 'Two'
        size_hint_x: .1
    Button:
        text: 'Three'
        size_hint_x: .1
    Button:
        text: 'Four'
        size_hint_x: .1
    GridLayout:
        rows: 2
        cols: 5
        canvas:
        BoxLayout:
            orientation: 'vertical'
            Spinner:
                text: 'SAW'
                values: ['SIN', 'SAW', 'TRI', 'SQR', 'PWM', 'DETUNE SAW', 'NOISE', 'INPUT']
            BoxLayout:
                orientation: 'vertical'
                BoxLayout:                            
                    Label:
                        text:'Sync'
                        text_size: self.size
                        halign: 'right'
                    CheckBox:               
                BoxLayout:
                    Label:
                        text:'Ring'
                        text_size: self.size
                        halign: 'right'
                    CheckBox:
                
        CircleKnob:
            knob_title: 'PITCH'
        CircleKnob:
            knob_title: 'FINE'
        CircleKnob:
            knob_title: 'PULSE WIDTH'
        CircleKnob:
            knob_title: 'DETUNE'
        CircleKnob:
            knob_title: 'SHARPNESS'
        
        CircleKnob:
            knob_title:' PWM ENV ' 
            
        CircleKnob:
            knob_title:'PITCH ENV'
        CircleKnob:
            knob_title: 'PBEND DEPTH'
        CircleKnob:
            knob_title: 'PBEND CTL'
        
    Button:
        text: 'Six'
        size_hint_x: .1
    Button:
        text: 'Seven'
        size_hint_x: .1
    Button:
        text: 'Eight'
        size_hint_x: .1
    Button:
        text: 'Nine'
    Button:
        text: 'Ten'
        size_hint_x: .1 
    Button:
        text: 'Elven'
        size_hint_x: .1
    Button:
        text: 'Twelve'
        size_hint_x: .1
        
        
"""


class PanelApp(App):

    def build(self):
        return Builder.load_string(kv)


PanelApp().run()
