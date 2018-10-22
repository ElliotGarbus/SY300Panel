from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from math import atan2, degrees
from kivy.lang import Builder
from kivy.clock import time


kv = '''
#-------------------------------
# Knob class
#  Properties are: knob_title, knob_vals, knob_ndx , knob_turn_delay
#
# Notes:
# 1) text size needs to scale with widget size
# 2) pick between x and y (delta abs thinggy)
#-------------------------------
<MyFirstKnob>
    orientation: 'vertical'
    padding:10
    Label:
        font_size: 30
        text: root.knob_vals[ root.knob_ndx ]
    
        canvas:
            Color:
                rgba: .4, .4 , .4, .5 
            Line:         
                circle: self.center_x, self.center_y, self.height/2 *.9, -140, 140
                cap: 'square'
                width: dp(5)
        canvas.after:
            Color:
                rgba: 0, 0 , 1, .9 
            Line:         
                circle:
                    (
                    self.center_x, self.center_y,
                    self.height/2 *.9,
                    -140, -140 + root.knob_ndx * 280 / ( len(root.knob_vals) - 1 )
                    )
                cap: 'square'
                width: dp(5)
    Label:
        id: knob_title
        font_size: '20'
        text: root.knob_title
        size_hint_y: .1
#-------------------------------

        
              
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        Button:
            text: "What an I doing here?"
        Button:
            text: "good question"
        Button:
            text: "knob input is obsolete"
        TextInput
            text: '1'
            on_text: primo.knob_ndx = int( self.text )

    GridLayout:
        rows: 2
        cols: 2
        
        MyFirstKnob:
            id: primo
            knob_title: "Pulse Width"
            knob_vals:  [ str(x) for x in range(101)]
            knob_turn_delay: .008
        MyFirstKnob:
            knob_vals: [ 'L2', 'L1', 'C', 'R1', 'R2' ]
            knob_ndx: 3
            knob_title: 'Balance'
            knob_turn_delay: .10
        MyFirstKnob:
            knob_vals: ['L'+str(-x) for x in range(-50, 0)] + ['CENTER'] + ['R'+ str(x) for x in range(1, 51)]
            knob_ndx: 1
            knob_title: 'Pan'
            knob_turn_delay: .1
        MyFirstKnob:
            knob_turn_delay: .1

   
'''


class MyFirstKnob(BoxLayout):
        
    knob_title      = StringProperty()
    knob_vals       = ListProperty([ str(i) for i in range(101)])
    knob_ndx        = NumericProperty( 1 )

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            if touch.dy:
                index = self.knob_ndx
                self.knob_ndx = sorted((0, int(index + touch.dy), len(self.knob_vals)-1))[1] #sorted(min, val, max)[1]

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            # I receive my grabbed touch, I must ungrab it!
            touch.ungrab(self)

class CircleApp(App):


    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    CircleApp().run()
