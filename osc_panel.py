from kivy.app import App
from kivy.lang import Builder
from xy import XY_knob
from circleknob import CircleKnob

kv = """
GridLayout:
    rows: 3
    cols: 4
    GridLayout:
        rows: 2
        cols: 6
        Spinner:
            text: 'SAW'
            values: ['SIN', 'SAW', 'TRI', 'SQR', 'PWM', 'DETUNE SAW', 'NOISE', 'INPUT']
            size_hint_y: .5
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
        
        XY_knob:
            xy_knob_xlab: 'PWM ENV ATTACK'
            xy_knob_ylab: 'PWM ENV DEPTH'
        XY_knob:
            xy_knob_xlab: 'PITCH ENV ATTACK'
            xy_knob_ylab: 'PITCH ENV DEPTH'
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
