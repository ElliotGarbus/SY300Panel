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
        Button:
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
        
        Button:
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
        Button:
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
    
    Button:
        text: 'Test pos'
        size_hint: (None, None)
        color:[1,1,1,1]
        size: self.texture_size
        pos: (sq_pad.pos[0] + 20,sq_pad.pos[1] + 20) 
'''


class ADKnob(BoxLayout):

    def on_touch_down(self, touch):
        print('Touch Down')
        if self.collide_point(*touch.pos):
            print('Touch in widget:', self.ids.sq_pad.to_widget(touch.pos, True))
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

