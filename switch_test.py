from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    BoxLayout:    #put the switch outside of the OSC wave box, it controls all the parts.
        id:outbox
        orientation: 'vertical'
        width: osc_name.texture_size[0]
        size_hint_x: None   
        Label:
            text:''
            size_hint_y: 1.2
        Switch:
            canvas.before:
                PushMatrix
                Rotate
                    angle: 90
                    origin: self.center
            canvas.after:
                PopMatrix         
        Label:           
            id:osc_name
            text:'OSC 1'
            halign: 'left' 
            canvas.before:
                PushMatrix
                Rotate
                    angle: 90
                    origin: self.center
            canvas.after:
                PopMatrix 
        Label:
            text:''        
            size_hint_y: 1.2       
        #Widget:
        #   Scatter:
        #       center: self.parent.center
        #       size: stext.size
        #       size_hint: (None,None)
        #       pos: (outbox.top, outbox.center_y)
        #       do_rotation: False
        #       do_translation: False
        #       do_scale: False
        #       rotation: 90
        #       #translation: 
        #       Label:
        #           id: stext
        #           text:'Scatter Text'    
            
    GridLayout:
        rows:2
        cols:2
        Button:
            text: 'Touch Here'
        Button:
            text: 'Touch Here'
        
        Button:
            text: 'Touch Here'
        Button:
            text: 'Touch Here'

     
        

'''


class SWtestApp(App):

    def build(self):
        return Builder.load_string(kv)

SWtestApp().run()
