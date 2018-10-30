from kivy.app import App
from kivy.lang import Builder

kv = '''
FloatLayout:  # combine a FloatLayout and BoxLayout
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Widget:
                #text:'PL'
            Label:
                text:'X-Axis Label'
                size_hint_x: None
                width: self.texture_size[1]
                canvas.before:
                    PushMatrix
                    Rotate
                        angle: 90
                        origin: self.center
                canvas.after:
                    PopMatrix         
            
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
            Widget:
                #id:pad_right
                #text: 'PR'
        Label:
            text: 'Y-Axis Label'
            size_hint_y: None
            height: self.texture_size[1]
        Label:
            text: 'Attack Decay Knob'
            size_hint_y: None
            height: self.texture_size[1]
    
    Label:
        text: 'Label from FloatLayout'
        size_hint: (None, None)
        color:[1,1,1,1]
        size: self.texture_size
        pos: (sq_pad.pos[0] + 200,sq_pad.pos[1] + 200) 
'''


class ADKnobApp(App):

    def build(self):
        return Builder.load_string(kv)

ADKnobApp().run()

