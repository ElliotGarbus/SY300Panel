from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kv = '''
<TryIt>
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
            id: b1
            text: 'Touch Here'
        Button:
            id: b2
            text: 'Touch Here'
        
        Button:
            id: b3
            text: 'Touch Here'
        Button:
            id: b4
            text: 'Touch Here to set b1'
            on_press: root.setb1()
    
TryIt:    
    

'''
class TryIt(BoxLayout):

    def setb1(self):
        map_to_knob = {1: self.ids.b1,
                       2: self.ids.b2,
                       3: self.ids.b3
                       }
        print('setb1 called')
        map_to_knob[2].text = 'Double WTF???'
        print(dir(self.ids.b1))


class SWtestApp(App):


    def build(self):
        return Builder.load_string(kv)

SWtestApp().run()
