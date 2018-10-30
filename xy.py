
import kivy
from kivy.app                import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang               import Builder
from kivy.properties         import ListProperty
from kivy.properties         import StringProperty
from kivy.properties         import NumericProperty


kivy.require('1.10.1')

'''
XYKnob
Created by Seth Abraham, October 22, 2018

A 'knob' for setting two values.  Values are on
the axises of an XY plane, and selected point indicates
the settings for X and Y.  Essentially two knobs set by
indicating a point on the XY plane.

'''

xykivystring = '''
#:kivy 1.10.1
#

# from relative layout
<XYKnob>
    size: mypad.size
    size_hint: (None,None)
    Label:
        id: mypad
        size: x_axis.width, x_axis.width
        size_hint: (None,None)
        canvas.after:
            Line:
                points: root.xy_knob_trackx
            Line:
                points: root.xy_knob_tracky
            Line:
                width: 4
                points: root.xy_knob_val
        canvas.before:
            Color:
                rgba: [ 0, 0, .8, 1 ]
            Rectangle:
                size: self.size
    Label:
        id: x_axis
        size_hint_y: None
        height: 10
        text: root.xy_knob_xlab + "=  " + str( root.xy_knob_xmin )
        font_size: int(.5 + 1.14 * self.width / (4 + max(root.ids.y_axis.text.find('='), self.text.find('=')) ) )
    Label:
        id: y_axis
        size_hint: (None,None)
        height: x_axis.height
        width: x_axis.width - x_axis.height
        text: root.xy_knob_ylab + "=" + str( root.xy_knob_ymin )
        font_size: root.ids.x_axis.font_size
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
        text: str( root.xy_knob_trkval )
        text_size: self.size
        size: self.texture_size
        size_hint: (None,None)
        pos: mypad.center
#-----------------------
'''

class XYKnob(RelativeLayout):
    xy_knob_trackx = ListProperty( [] )
    xy_knob_tracky = ListProperty( [] )
    xy_knob_trkval = StringProperty( '' )
    xy_knob_val    = ListProperty([ [0, 0], [0,0] ] )
    xy_knob_xlab   = StringProperty( 'X-axis' )
    xy_knob_xmin   = NumericProperty(   0 )
    xy_knob_xmax   = NumericProperty( 100 )
    xy_knob_ylab   = StringProperty( 'Y-axis' )
    xy_knob_ymin   = NumericProperty(   0 )
    xy_knob_ymax   = NumericProperty( 100 )
  

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            wigtch  = self.to_widget( *touch.pos )
            wigloc  = self.to_widget( *self.pos )

            xval = int( wigtch[0] / self.width  * (self.xy_knob_xmax - self.xy_knob_xmin)  ) + self.xy_knob_xmin
            yval = int( wigtch[1] / self.height * (self.xy_knob_ymax - self.xy_knob_ymin)  ) + self.xy_knob_ymin
            self.xy_knob_trkval = '(' + str(xval) + ',' + str(yval)  +')'
            self.ids.trackinglabel.pos = wigtch


            self.xy_knob_tracky.extend( [[wigtch[0], wigloc[1]], [wigtch[0], wigloc[1] + self.height ] ] )
            self.xy_knob_trackx.extend( [[wigloc[0], wigtch[1]], [wigloc[0]+self.width, wigtch[1]] ] )
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
            xval = int( wigtch[0] / self.width  * (self.xy_knob_xmax - self.xy_knob_xmin)  ) + self.xy_knob_xmin
            yval = int( wigtch[1] / self.height * (self.xy_knob_ymax - self.xy_knob_ymin)  ) + self.xy_knob_ymin
            self.xy_knob_trkval = '(' + str(xval) + ',' + str(yval)  +')'
            self.ids.trackinglabel.pos = wigtch

            # update tracking lines.  Do a copy so property notices update
            self.xy_knob_tracky[0][0] = wigtch[0]
            self.xy_knob_tracky[1][0] = wigtch[0]
            self.xy_knob_tracky[:]    = self.xy_knob_tracky[:]

            self.xy_knob_trackx[0][1] = wigtch[1]
            self.xy_knob_trackx[1][1] = wigtch[1]
            self.xy_knob_trackx[:]    = self.xy_knob_trackx[:]

            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            del(self.xy_knob_trackx[0:] )
            del(self.xy_knob_tracky[0:] )
            self.xy_knob_trkval = ''

            #cleanup note:
            #common code with move should be exploited (code written once)

            # need touch position to be mutable so we can clamp to frame
            wigtch  = list(self.to_widget( *touch.pos )) 
            wigloc  =      self.to_widget( *self.pos  )

            # clamp position so it stays in frame...
            for i in (0,1):
               wigtch[i] = sorted([wigloc[i], wigloc[i]+ self.size[i], wigtch[i]])[1]

            xval = int( wigtch[0] / self.width  * (self.xy_knob_xmax - self.xy_knob_xmin)  ) + self.xy_knob_xmin
            yval = int( wigtch[1] / self.height * (self.xy_knob_ymax - self.xy_knob_ymin)  ) + self.xy_knob_ymin
          
            # re-title the axis with the new value
            self.ids.x_axis.text = self.xy_knob_xlab + " val= " + str(xval)
            self.ids.y_axis.text = self.xy_knob_ylab + " val= " + str(yval)

            # Move the dot to the new position
            del(self.xy_knob_val[0:])
            self.xy_knob_val.extend( ( wigtch, wigtch ) )

            return True
        return super().on_touch_up(touch)


Builder.load_string(xykivystring )




if __name__ == '__main__':

    kv = '''
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
        
        XYKnob:
            id: primo
            size: 250,250
            size_hint: (None,None)
            xy_knob_xlab: 'Cut-off'
            xy_knob_ylab: "Res"
        XYKnob:
            id: two
            size: 250,250
            size_hint:(None,None)
            xy_knob_xlab: "Volume"
            xy_knob_ylab: "Bal"
            xy_knob_xmax: 11
            xy_knob_ymax: 1
            xy_knob_ymin: -1
        XYKnob:
            id: three
            size: 250,250
            size_hint:(None,None)
        XYKnob:
            id: four
            size: 250,250
            size_hint:(None,None)

'''

    class XYKnobApp(App):
        def build(self):
            b = Builder.load_string(kv)
            print( b.ids.mypad.pos )
            return b

    XYKnobApp().run()
