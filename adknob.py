from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty


kv = '''
<ADKnob>
    orientation: 'vertical'
    BoxLayout:
        Label:
            id:pad_left
            text:'L'
            size_hint_x:.001
        Label:
            id:sq_pad
            text: str(root.adknob_ndx - 50)
            font_size: 15
            size_hint_x: None
            width: self.size[1]
            canvas.before:
                Color:
                    rgba: [.4, .4 , .4, .5 ]
                Line:  # Middle Bar
                    width:4
                    cap: 'none'
                    points:[(sq_pad.center_x,sq_pad.pos[1]), (sq_pad.center_x, sq_pad.top)]
                Color:
                    rgba: [0, 0 , 1, .9]
                Line: # Attack Line
                    width: 2
                    cap: 'none'
                    points: [root.adknob_attack_pos, sq_pad.pos[1], sq_pad.center_x, sq_pad.top]
                Line: # Decay Line
                    width: 2
                    cap: 'none'   
                    points: [root.adknob_decay_pos, sq_pad.pos[1], sq_pad.center_x, sq_pad.top]
            
                Color:
                    rgba:[1,1,1,1]
                Line:
                    width:2
                    rectangle: (*self.pos,self.width,self.height)

                
        Label:
            id:pad_right
            text: 'R'
            size_hint_x: .001 
    Label:
        text: 'AMP ENV'
        font_size: 15
        size_hint_y: None
        height: self.texture_size[1]
    
    Label:
        text: 'Test pos:' # + str()
        size_hint: (None, None)
        color:[1,1,1,1]
        size: self.texture_size
        pos: (sq_pad.pos[0] + 20,sq_pad.pos[1] + 20) 
'''


class ADKnob(BoxLayout):
    adknob_decay_pos = NumericProperty(0)   # position from 0 to center
    adknob_attack_pos = NumericProperty(0)  # Position from center to right
    adknob_ndx = NumericProperty(0)         # from 0 to 100


    def on_touch_down(self, touch):
        if self.ids.sq_pad.collide_point(*touch.pos):
            touch.grab(self)
            sq_xy = self.ids.sq_pad.to_widget(*touch.pos, True)
            scale_xy = [int(sq_xy[0] * 100/(self.ids.sq_pad.width)), int(sq_xy[1] * 100/(self.ids.sq_pad.height))]
            print('Self transformed pos:', sq_xy)
            print('Transformed and scaled', scale_xy)
            print('pos', touch.pos)
            print('to local', self.ids.sq_pad.to_widget(*touch.pos, True))
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            print('on touch move')
            sq_xy= self.ids.sq_pad.to_widget(*touch.pos, True)
            #clamp the move to stay in sq_pad
            sq_x = sorted([0, int(sq_xy[0]),self.ids.sq_pad.width])[1]  # from 0 to width in pixels
            print('sq_x', sq_x)
            center_x = self.ids.sq_pad.center_x - self.ids.sq_pad.pos[0]

            if sq_x == center_x:    # at center, set value to zero
                self.adknob_decay_pos = self.ids.sq_pad.rigth
                self.adknob_attack_pos = self.ids.sq_pad.center[0]
                self.adknob_ndx = 50 # values go from [-50 to +50] 50 value is a 0 ndx
            if sq_x < self.ids.sq_pad.center[0]:  # left of center set attack, zero decay
                self.ids.adknob_decay_pos = self.ids.sq_pad.right
                self.ids.adknob_attack_pos = sq_x
                self.ids.adknob_attack_value = sq_x - 50 # 




            return True
        return False

    def on_touch_up(self, touch):
        #if touch.is_mouse_scrolling and touch.grab_current is self:
            # sorted(min, val, max)[1] works to clamp val to floor or ceiling
            #self.knob_ndx = (sorted((0, self.knob_ndx + self._scroll_direction[touch.button],
            #                        len(self.knob_vals) - 1))[1])
            #return True
        if touch.grab_current is self:
            touch.ungrab(self)
            return True
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
        return Builder.load_string(kv + kv_test)

ADKnobApp().run()

