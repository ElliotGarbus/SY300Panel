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
#  Properties are: knob_title, knob_vals, knob_ndx 
#
# Notes:
# 1) might also want to add knob_turn_delay
#    see note about "delta" in python code
#
# 2) text size needs to scale with widget size
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
            knob_vals: [str(x) for x in range(0,201)]
        MyFirstKnob:
            knob_vals: [str(x) for x in range(-24,25)]
            knob_ndx: 3
            knob_title: 'Balance'
        MyFirstKnob:
            knob_vals: ['L'+str(-x) for x in range(-50, 0)] + ['CENTER'] + ['R'+ str(x) for x in range(1, 51)]
            knob_ndx: 1
            knob_title: 'Pan'
        MyFirstKnob:

   
'''
class MyFirstKnob(BoxLayout):
        
    knob_title = StringProperty()
    knob_vals  = ListProperty( [ str(i) for i in range(10) ] )
    knob_ndx   = NumericProperty( 1 )
    _mylast    = 0,0,0


    def on_touch_move(self, touch):

        timedelta = 0.02  # time delta required to move a knob
                          # might want to make this knob_turn_delay and let
                          # it vary per instance.  Large val lists need short
                          # times, but small val lists might do better with longer delay

        # Need better way to identify a knob than looking for knob_title in directory!
        # and i am probably looking at more widgets than I need to....

        for this in App.get_running_app().root.walk():
            if (  'knob_title' in dir(this)
                  and this.collide_point( touch.pos[0],touch.pos[1] )  
                  and ( time.time() - this._mylast[2] > timedelta ) ):

                 #   dy = touch.pos[1] - this._mylast[1] 
                 #   dx = touch.pos[0] - this._mylast[0] 
                 # if ( fabx(dy) > fabs(dx) ):
                 #    want the sign of y 
                 # else
                 #    want the sign of x

                if   this._mylast[1] > touch.pos[1] or this._mylast[0] > touch.pos[0] :
                   this.knob_ndx = max( this.knob_ndx - 1,  0 )
                elif this._mylast[1] < touch.pos[1] or this._mylast[0] < touch.pos[0] :
                   this.knob_ndx = min( this.knob_ndx + 1, len (this.knob_vals)-1 )
                this._mylast = touch.pos[0], touch.pos[1], time.time()

        return super().on_touch_move(touch)


class CircleApp(App):


    def build(self):
        return Builder.load_string(kv)






if __name__ == '__main__':
    CircleApp().run()
