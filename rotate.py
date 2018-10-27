from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    Button:
        size_hint_x: .1
        Label:
            text: 'I am label one'
            size: self.texture_size   
            y: self.parent.center_y - .5 * self.height
            x: self.parent.center_x - 0.5 * self.width
            
            canvas.before:
                PushMatrix
                Rotate
                    angle: 90
                    origin: self.center
            canvas.after:
                PopMatrix  
    
    Button:
        text: 'My name is label two'
        size:self.texture_size
 
'''





class RotateApp(App):

    def build(self):
        return Builder.load_string(kv)


RotateApp().run()

