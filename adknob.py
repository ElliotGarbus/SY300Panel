from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.properties import ListProperty

Builder.load_string('''
<ADKnob>
    orientation: 'vertical'
    id:vbox
    BoxLayout:
        Label:
            id:pad_left
            text:''
            width: 0.5 * (vbox.width - sq_pad.width) # set widths forces Box + Relativelayout to behave
            size_hint_x:None
        RelativeLayout:
            Label:
                id:sq_pad
                text: str(root.adknob_ndx - 50)
                font_size: 25
                size_hint_x: None
                width: self.size[1]
                color: [144/255, 228/255 , 1, 1]
                canvas.before:
                    Color:
                        rgba: [.4, .4 , .4, .5 ]
                    Line:  # Middle Bar
                        width:4
                        cap: 'none'
                        points:[(sq_pad.center_x,sq_pad.pos[1]), (sq_pad.center_x, sq_pad.top)]
                    Color:
                        rgba: [ 36/255, 129/255, 215/255, 1 ]
                    Line: # Attack Line
                        width: 2
                        cap: 'none'
                        points: [sq_pad.center_x if(root.adknob_ndx > 50) else  sq_pad.x + root.adknob_ndx/100 * sq_pad.width, sq_pad.y, sq_pad.center_x, sq_pad.top]
                        
                    Line: # Decay Line
                        width: 2
                        cap: 'none'   
                        points: [sq_pad.right if (root.adknob_ndx < 51) else  sq_pad.right + (50-root.adknob_ndx)/100 * sq_pad.width, sq_pad.y, sq_pad.center_x, sq_pad.top]
                    Color:
                        rgba:[.4, .4 , .4, .7 ]
                    Line:
                        width:2
                        rectangle: (*self.pos,self.width,self.height)
                    
            Label:
                text: 'Slow\\nAttack'
                font_size: 13 
                size_hint: (None, None)
                color:[.4, .4 , .4, .7 ]
                size: self.texture_size
                pos: (sq_pad.x +4, sq_pad.top - self.height -2)
            
            Label:
                text: ' Short\\nDecay' 
                font_size: 13
                size_hint: (None, None)
                color:[.4, .4 , .4, .7 ]
                size: self.texture_size
                pos: (sq_pad.right - self.width -4, sq_pad.top - self.height -2)   

                
        Label:
            id:pad_right
            text: ''
            size_hint_x: .001 
    Label:
        text: 'AMP ENV'
        font_size: 15
        size_hint_y: None
        height: self.texture_size[1]
        color: [144/255, 228/255 , 1, 1]
''')


class ADKnob(BoxLayout):
    adknob_ndx = NumericProperty(50)         # from 0 to 100
    addresses  = ListProperty( [] )
    _scroll_direction = {'scrollup': 1, 'scrolldown': -1}

    def _touch_to_ndx(self, touch):
        sq_xy = self.ids.sq_pad.to_widget(*touch.pos, True)
        self.adknob_ndx = sorted([0, int(sq_xy[0] * 100 / (self.ids.sq_pad.width)), 100])[1]

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            if not touch.is_mouse_scrolling:
                self._touch_to_ndx(touch)
            return super().on_touch_down(touch)
        return False

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self._touch_to_ndx(touch)
            return super().on_touch_move(touch)
        return False

    def on_touch_up(self, touch): 
        if touch.is_mouse_scrolling and touch.grab_current is self:
            self.adknob_ndx = sorted((0, self.adknob_ndx + self._scroll_direction[touch.button], 100))[1]
            return super().on_touch_up(touch)
        elif touch.grab_current is self:
            touch.ungrab(self)
            return super().on_touch_up(touch)
        return False

if __name__ == '__main__':
    kv_test = '''
GridLayout:
    rows: 3
    cols: 3
    ADKnob:
    ADKnob:
    ADKnob:
    ADKnob:       
    ADKnob:
    ADKnob:
    ADKnob:
    ADKnob:       
    ADKnob:       

    '''


    class ADKnobApp(App):


        def build(self):
            return Builder.load_string(kv_test)

    ADKnobApp().run()

