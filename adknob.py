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
                    points: [root._ndx_to_pos(root.adknob_ndx)['attack'], sq_pad.pos[1], sq_pad.center_x, sq_pad.top]
                Line: # Decay Line
                    width: 2
                    cap: 'none'   
                    points: [root._ndx_to_pos(root.adknob_ndx)['decay'], sq_pad.pos[1], sq_pad.center_x, sq_pad.top]
            
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
    adknob_ndx = NumericProperty(50)         # from 0 to 100
    _scroll_direction = {'scrollup': 1, 'scrolldown': -1}

    def _ndx_to_pos(self, index): # need to pass adknob_ndx for KV to force update on change
        center_x = self.ids.sq_pad.center_x
        zero_attack = center_x
        zero_decay = self.ids.sq_pad.right
        curr_x = self.ids.sq_pad.width/100 * index + self.ids.sq_pad.x

        if index <50: # left of center, adjust attack, zero delay
            attack_pos = max(curr_x, self.ids.sq_pad.x)
            decay_pos = zero_decay
        elif index > 50:  # Right of center, set decay, zero attack
            attack_pos = zero_attack
            decay_pos = min(curr_x, self.ids.sq_pad.right)
        else:  # zero
            attack_pos = zero_attack
            decay_pos = zero_decay
        return {'attack':attack_pos,'decay':decay_pos}

    def _touch_to_ndx(self, touch):
        sq_xy = self.ids.sq_pad.to_widget(*touch.pos, True)
        self.adknob_ndx = sorted([0, int(sq_xy[0] * 100 / (self.ids.sq_pad.width)), 100])[1]

    def on_touch_down(self, touch):
        if self.ids.sq_pad.collide_point(*touch.pos):
            touch.grab(self)
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
            print('mouse scroll, ndx:', self.adknob_ndx)
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
        return Builder.load_string(kv + kv_test)

ADKnobApp().run()

