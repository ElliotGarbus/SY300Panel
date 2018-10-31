
import kivy
from kivy.app                import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang               import Builder
from kivy.properties         import ListProperty
from kivy.properties         import StringProperty
from kivy.properties         import BooleanProperty
from kivy.properties         import NumericProperty
from kivy.uix.boxlayout      import BoxLayout
from kivy.uix.floatlayout    import FloatLayout


kivy.require('1.10.1')

'''
XYKnob
Created by Seth Abraham, October 22, 2018
Total rewrite October 26, 2018

A 'knob' for setting two values.  Values are on
the axises of an XY plane, and selected point indicates
the settings for X and Y.  Essentially two knobs set by
indicating a point on the XY plane.

'''

xykivystring = '''
#:kivy 1.10.1
#

# from BoxLayout
<XYKnob>
    orientation: 'vertical'
    id: vbox
    BoxLayout:
        orientation: 'horizontal'
        id: hbox
        Label:
            text: ''
            width: 0.5 * ( vbox.width - mypad.width )
            size_hint_x: None
        RelativeLayout:
            #Label:
            #    id: mybackground 
            Label:
                id: mypad
                width: self.height
                size_hint_x: None
                font_size: 15
                text: str(root.xy_knob_xval) + ',' + str(root.xy_knob_yval)
                canvas.after:
                    Line:
                        points: root.xy_knob_trackx
                    Line:
                        points: root.xy_knob_tracky
                    Line:
                        width: 2
                        points: [ root._val2pos(root.xy_knob_xval, root.xy_knob_yval), root._val2pos(root.xy_knob_xval, root.xy_knob_yval) ]
                    Color:
                        rgba: [ 1, 0, 0, .5 ]
                    Line:
                        width: 1
                        points: [ 0,.5*mypad.height, mypad.width, .5*mypad.width ] if root.xy_knob_crosshair else []
                    Line:
                        points: [ .5*mypad.width, 0, .5*mypad.width, mypad.width ] if root.xy_knob_crosshair else []
                canvas.before:
                    Color:
                        rgba: [ 0, 0, .8, 1 ]
                    Rectangle:
                        pos: self.pos
                        size: self.size
                #end mypad
            Label:
                id: x_axis
                pos: ( mypad.center_x - .5*self.width, 0 )
                text: root.xy_knob_xlab
                size: self.texture_size
                size_hint: (None,None)
                font_size: int(.5 + 1.14 * mypad.width / max(len(root.ids.y_axis.text), len(self.text)) )
            Label:
                id: y_axis
                #pos_hint: { 'center_y':.5, 'center_x':0.08 }
                pos: ( -.38*self.width, mypad.center_y )
                text: root.xy_knob_ylab
                font_size: int(.5 + 1.14 * mypad.width / max(len(root.ids.x_axis.text), len(self.text)) )
                size: self.texture_size
                size_hint: (None,None)
                canvas.before:
                    PushMatrix
                    Rotate
                        angle: 90
                        origin: self.center
                canvas.after:
                    PopMatrix
            Label:
                id: trackinglabel
                pos: mypad.center
                text: str( root.xy_knob_trkval )
                size: self.texture_size
                size_hint: (None,None)
            #end rellay
        Label:
            width: 0.5 * ( vbox.width - mypad.width  )
            size_hint_x: None
            text: ''
    Label:
        id: xytitle
        text: root.xy_knob_title
        #font_size: int(.5 + 1.14 * mypad.width / len(self.text) )
        font_size: 15
        size: self.texture_size
        size_hint_y: None
    #end xyknob
#-----------------------
'''

class XYKnob(BoxLayout):

    xy_knob_trackx    = ListProperty( [] )
    xy_knob_tracky    = ListProperty( [] )
    xy_knob_trkval    = StringProperty( '' )
    xy_knob_trkvis    = BooleanProperty( False )

    xy_knob_xlab      = StringProperty( 'X-axis' )
    xy_knob_xmin      = NumericProperty(   0 )
    xy_knob_xmax      = NumericProperty( 100 )
    xy_knob_xval      = NumericProperty( 0 )

    xy_knob_ylab      = StringProperty( 'Y-axis' )
    xy_knob_ymin      = NumericProperty( 0 )
    xy_knob_ymax      = NumericProperty( 100 )
    xy_knob_yval      = NumericProperty( 0 )

    xy_knob_title     = StringProperty( 'Title' )
    xy_knob_crosshair = BooleanProperty( False )
  

    def _val2pos(self, valx, valy ):
    #
    # convert from a value back to a position
    #
        xv = (valx - self.xy_knob_xmin) / (self.xy_knob_xmax - self.xy_knob_xmin) * self.ids.mypad.width
        yv = (valy - self.xy_knob_ymin) / (self.xy_knob_ymax - self.xy_knob_ymin) * self.ids.mypad.height
        return xv, yv

    def _compute_pos_and_val(self,touch):
    #
    # determine the touch positionin a mypad cordinate space
    # clamps that position tothe size of mypad (overkill until until we move!)
    # and converts the cordinates into x,y values
    #
    #
        relative_position = list ( self.ids.mypad.to_widget(*touch.pos, True ) )

        relative_position[0] = sorted([ relative_position[0], 0, self.ids.mypad.width  ] )[1]
        relative_position[1] = sorted([ relative_position[1], 0, self.ids.mypad.height ] )[1]

        xval = int(  relative_position[0] / self.ids.mypad.width 
                   * (self.xy_knob_xmax - self.xy_knob_xmin)  
                   + self.xy_knob_xmin )
        yval = int(  relative_position[1] / self.ids.mypad.height
                   * (self.xy_knob_ymax - self.xy_knob_ymin) 
                   + self.xy_knob_ymin  )


        return relative_position,xval,yval


    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)

            rel_pos,xval,yval = self._compute_pos_and_val(touch)

            # position tracking label
            #self.xy_knob_trkval = '(' + str(xval) + ',' + str(yval)  +')'
            self.xy_knob_trkval = str(xval) + ',' + str(yval)

            #self.ids.trackinglabel.pos = rel_pos
            self.ids.trackinglabel.x = rel_pos[0] + (-1,0)[rel_pos[0]<.5*self.ids.mypad.width]  * self.ids.trackinglabel.size[0]
            self.ids.trackinglabel.y = rel_pos[1] + (-1,0)[rel_pos[1]<.5*self.ids.mypad.height] * self.ids.trackinglabel.size[1]

            # draw tracking lines
            self.xy_knob_tracky.extend( [rel_pos[0], 0,   rel_pos[0], self.ids.mypad.top   ] )
            self.xy_knob_trackx.extend( [0, rel_pos[1],   self.ids.mypad.right, rel_pos[1] ] )

            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:

            # position tracking label
            rel_pos,xval,yval = self._compute_pos_and_val(touch)
            #self.xy_knob_trkval = '(' + str(xval) + ',' + str(yval)  +')'
            self.xy_knob_trkval = str(xval) + ',' + str(yval)
            #self.ids.trackinglabel.pos = rel_pos
            self.ids.trackinglabel.x = max ( self.ids.y_axis.size[1],
                     rel_pos[0] + (-1,0)[rel_pos[0]<.5*self.ids.mypad.width]  * self.ids.trackinglabel.size[0] )
            self.ids.trackinglabel.y = max ( self.ids.x_axis.top, 
                     rel_pos[1] + (-1,0)[rel_pos[1]<.5*self.ids.mypad.height] * self.ids.trackinglabel.size[1] )

            # update tracking lines.
            self.xy_knob_tracky[0] = rel_pos[0]
            self.xy_knob_tracky[2] = rel_pos[0]

            self.xy_knob_trackx[1] = rel_pos[1]
            self.xy_knob_trackx[3] = rel_pos[1]

            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)

            # remove tracking lines and tracking label
            del(self.xy_knob_trackx[0:] )
            del(self.xy_knob_tracky[0:] )
            self.xy_knob_trkval = ''

            rel_pos,xval,yval = self._compute_pos_and_val(touch)
            # re-title the axis with the new value
            #self.ids.x_axis.text = self.xy_knob_xlab + "= " + str(xval)
            #self.ids.y_axis.text = self.xy_knob_ylab + "= " + str(yval)

            # Now move the dot to the new position
            self.xy_knob_xval = xval
            self.xy_knob_yval = yval


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
        cols: 6
        padding: 10
        spacing: 10
        
        XYKnob:
            id: primo
            #xy_knob_xlab: 'Cut-off'
            #xy_knob_ylab: "Res"
        XYKnob:
            id: two
            #size: 250,250
            #xy_knob_ylab: "Bal"
            #xy_knob_xmax: 11
            #xy_knob_ymax: 1
            #xy_knob_ymin: -1
        XYKnob:
            id: three
        XYKnob:
            id: four
        XYKnob:
        XYKnob:
        XYKnob:
            xy_knob_title: 'NotMe'
        XYKnob:
            xy_knob_crosshair: True
        XYKnob:
        XYKnob:
            xy_knob_crosshair: True
        XYKnob:
        XYKnob:

'''

    class XYKnobApp(App):
        def build(self):
            r = Builder.load_string(kv)
            return r

    XYKnobApp().run()
