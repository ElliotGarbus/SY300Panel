from kivy.app import App
from kivy.lang import Builder

kv = """
#:import XYKnob xyknob
#:import CircleKnob circleknob
GridLayout:
    rows: 3
    cols: 4
    GridLayout:
        rows: 2
        cols: 6
        BoxLayout:
            orientation: 'vertical'
            Spinner:
                text: 'SAW'
                values: ['SIN', 'SAW', 'TRI', 'SQR', 'PWM', 'DETUNE SAW', 'NOISE', 'INPUT']
            BoxLayout:
                CheckBox:
                    pos_hint: {'right': .9} 
                Label:
                    text:'Sync'
                    pos_hint: {'left': .9}
            BoxLayout:
                CheckBox:
                    pos_hint: {'right': .9}
                Label:
                    text:'Ring'
                    pos_hint: {'left': .9}
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
        Label:
            text: 'PLACEHOLDER'
        
        XYKnob:
            xy_knob_title:' PWM ENV '   # we space pad the title so it is about the same length as other titles
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        XYKnob:
            xy_knob_title:'PITCH ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        CircleKnob:
            knob_title: 'Pitch Bend Depth'
        CircleKnob:
            knob_title: 'Pitch Bend CTL'
        
    Button:
        text: 'Two'
        size_hint_x: .1
    Button:
        text: 'Three'
        size_hint_x: .1
    Button:
        text: 'Four'
        size_hint_x: .1
    Button:
        text: 'Five'
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
