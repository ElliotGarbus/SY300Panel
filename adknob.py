from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

kv = '''
<ADKnob>
    #BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        Label:
            id:pad_left
            text:'L'
            size_hint_x:.001
        #Label:
        #    id: x_axis_label
        #    text:'X-Axis Label'
        #    size_hint_x: None
        #    width: self.texture_size[1]
        #    canvas.before:
        #        PushMatrix
        #        Rotate
        #            angle: 90
        #            origin: self.center
        #    canvas.after:
        #        PopMatrix         
        Label:
            id:sq_pad
            text: 'Square Pad'
            size_hint_x: None
            width: self.size[1]
            canvas:
                Color:
                    rgba: [1,0,0,.5]
                Line:
                    width:5
                    points:[sq_pad.pos, (sq_pad.pos[0] + sq_pad.width, sq_pad.pos[1] + sq_pad.height)]
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
        text: 'Y-Axis Label'
        size_hint_y: None
        height: self.texture_size[1]
    Label:
        text: 'AMP ENV'
        size_hint_y: None
        height: self.texture_size[1]
    
    Label:
        text: 'Test pos'
        size_hint: (None, None)
        color:[1,1,1,1]
        size: self.texture_size
        pos: (sq_pad.pos[0] + 20,sq_pad.pos[1] + 20) 
'''


class ADKnob(BoxLayout):

    def on_touch_down(self, touch):
        if self.ids.sq_pad.collide_point(*touch.pos):
            sq_xy = [touch.pos[i]-self.ids.sq_pad.pos[i] for i in range(2)]
            scale_xy = [sq_xy[0] * 100//self.ids.sq_pad.width, sq_xy[1] * 100//self.ids.sq_pad.height]
            print('Self transformed pos:', sq_xy)
            print('Transformed and scaled', scale_xy)

        return super().on_touch_down(touch)


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

