
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.properties      import ListProperty
from kivy.properties      import StringProperty

from math import atan2, degrees, fabs
from random import random

kivy.require('1.10.1')

'''
XY_knob
Created by Seth Abraham, October 22, 2018

A 'knob' for setting two values.  Values are on
the axises of an XY plane, and selected point indicates
the settings for X and Y.  Essentially two knobs set by
indicating a point on the XY plane.

'''

kv = '''
#:kivy 1.10.1
#

<XY_knob>
    size: mypad.size
    size_hint: (None,None)
    Label:
        id: x_axis
        size_hint_y: None
        height: 25
        text: "I am the X axis"
    Label:
        id: y_axis
        size_hint: (None,None)
        height: x_axis.height
        width: x_axis.width - x_axis.height
        text: "I am the Y axis"
        canvas.before:
            PushMatrix
            Rotate
                angle: 90
            Translate
                y: -x_axis.height
                x: x_axis.height
        canvas.after:
            PopMatrix
    Label:
        id: trackinglabel
        text: str( root.XY_knob_trkval )
        text_size: self.size
        size: self.size
        size_hint: (None,None)
    Label:
        id: mypad
        size: x_axis.width, x_axis.width
        size_hint: (None,None)
        canvas.after:
            Line:
                points: root.XY_knob_trackx
            Line:
                points: root.XY_knob_tracky
            Line:
                width: 4
                points: root.XY_knob_val
        canvas.before:
            Color:
                rgba: [ 0, 0, .8, .7 ]
            Rectangle:
                size: self.size
#-----------------------
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: .1
        Button:
            text: "What an I doing here?"
        Button:
            text: "good question"
        Button:
            text: "different sort of knob"

    GridLayout:
        rows: 2
        cols: 2
        padding: 10
        spacing: 10
        
        XY_knob:
            id: primo
            size: 250,250
            size_hint:(None,None)
        XY_knob:
            id: two
            size: 250,250
            size_hint:(None,None)
        XY_knob:
            id: three
            size: 250,250
            size_hint:(None,None)
        XY_knob:
            id: four
            size: 250,250
            size_hint:(None,None)

'''


class XY_knob(RelativeLayout):
#class XY_knob(FloatLayout):
    XY_knob_trackx = ListProperty( [] )
    XY_knob_tracky = ListProperty( [] )
    XY_knob_trkval = StringProperty( '' )
    XY_knob_val    = ListProperty([ [50, 50], [50,50] ] )
  

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            # TODO: test that an explicit widget pos does not break things
            wigtch  = self.to_widget( *touch.pos )
            wigloc  = self.to_widget( *self.pos )

            xval = int( wigtch[0] / self.width  * 100.0 )
            yval = int( wigtch[1] / self.height * 100.0 )
            self.XY_knob_trkval = '(' + str(xval) + ',' + str(yval)  +')'
            self.ids.trackinglabel.pos = wigtch


            self.XY_knob_tracky.extend( [[wigtch[0], wigloc[1]], [wigtch[0], wigloc[1] + self.height ] ] )
            self.XY_knob_trackx.extend( [[wigloc[0] , wigtch[1]], [wigloc[0]+self.width, wigtch[1]] ] )
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:

            # need touch position to be mutable so we can clamp to frame
            wigtch  = list(self.to_widget( *touch.pos )) 
            wigloc  =      self.to_widget( *self.pos  )

            # clamp position so it stays in frame...
            for i in (0,1):
               wigtch[i] = sorted([wigloc[i], wigloc[i]+ self.size[i], wigtch[i]])[1]

            # update and move the tracking label
            xval = int( wigtch[0] / self.width  * 100.0 )
            yval = int( wigtch[1] / self.height * 100.0 )
            self.XY_knob_trkval = '(' + str(xval) + ',' + str(yval)  +')'
            self.ids.trackinglabel.pos = wigtch

            # update tracking lines.  Do a copy so property notices update
            self.XY_knob_tracky[0][0] = wigtch[0]
            self.XY_knob_tracky[1][0] = wigtch[0]
            self.XY_knob_tracky[:]    = self.XY_knob_tracky[:]

            self.XY_knob_trackx[0][1] = wigtch[1]
            self.XY_knob_trackx[1][1] = wigtch[1]
            self.XY_knob_trackx[:]    = self.XY_knob_trackx[:]

            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            del(self.XY_knob_trackx[0:] )
            del(self.XY_knob_tracky[0:] )
            self.XY_knob_trkval = ''

            #cleanup note:
            #common code with move should be exploited (code written once)

            # need touch position to be mutable so we can clamp to frame
            wigtch  = list(self.to_widget( *touch.pos )) 
            wigloc  =      self.to_widget( *self.pos  )

            # clamp position so it stays in frame...
            for i in (0,1):
               wigtch[i] = sorted([wigloc[i], wigloc[i]+ self.size[i], wigtch[i]])[1]

            xval = int( wigtch[0] / self.width  * 100.0 )
            yval = int( wigtch[1] / self.height * 100.0 )
          
            # re-title the axis with the new value
            self.ids.x_axis.text = 'label type, val= ' + str(xval)
            self.ids.y_axis.text = 'label type, val= ' + str(yval)

            # Move the dot to the new position
            del(self.XY_knob_val[0:])
            self.XY_knob_val.extend( ( wigtch, wigtch ) )

            return True
        return super().on_touch_up(touch)




class XY_knobApp(App):
    def build(self):

        return Builder.load_string(kv)


if __name__ == '__main__':
    XY_knobApp().run()
