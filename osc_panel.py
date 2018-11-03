from kivy.app import App
from kivy.lang import Builder

kv = """
#:import XYKnob xyknob
#:import CircleKnob circleknob
#:import ADKnob adknob
GridLayout: # Holds all panels
    rows: 3
    cols: 4
    spacing: 5
 #------------------------------------------ OSC 1 Wave Panel ------------------------------------------    
    GridLayout:
        rows: 2
        cols: 5
        canvas.after:
            Color:
                rgba:[.4, .4 , .4, .7 ]
            Line:
                width:2
                rounded_rectangle: (*self.pos,self.width,self.height, 2)
                
        GridLayout:
            rows:3
            cols:1
            orientation: 'vertical'
            ToggleButton:
                text:'OSC 1'
            Spinner:
                text: 'SAW'
                values: ['SIN', 'SAW', 'TRI', 'SQR', 'PWM', 'DETUNE SAW', 'NOISE', 'INPUT']
            Label:
                text:''
        CircleKnob:
            knob_title: 'PITCH'
        CircleKnob:
            knob_title: 'FINE'
        CircleKnob:
            knob_title: 'PULSE WIDTH'
        CircleKnob:
            knob_title: 'DETUNE'
        CircleKnob:
            knob_title: 'SHARPNESS'
        
        XYKnob:
            xy_knob_title:' PWM ENV '   
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        XYKnob:
            xy_knob_title:'PITCH ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        CircleKnob:
            knob_title: 'PBEND DEPTH'
        CircleKnob:
            knob_title: 'PBEND CTL'
#------------------------------------------ OSC 1 Filer Panel ------------------------------------------            
    GridLayout:
        rows: 2
        cols: 3
        BoxLayout:
            orientation: 'vertical'
            Spinner:
                text: 'Type'
                values: ['BYPASS', 'LPF', 'HPF', 'BPF', 'PKG']
            Spinner:
                text: 'Slope'
                values: ['-12 dB', '-24 dB']
            Label:
                text:''
        
        XYKnob:
            xy_knob_title:'Filter'
            xy_knob_xlab: 'CUTOFF'
            xy_knob_ylab: 'RESO'
        
        XYKnob:
            xy_knob_title:'ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
  
        ADKnob:
        
        CircleKnob:
            knob_title: 'LEVEL'
        CircleKnob: 
            knob_title: 'PAN'   
        
    Button:
        text: 'Three'
        size_hint_x: .1
    Button:
        text: 'Four'
        size_hint_x: .1
#  ------------------------------------------------OSC 2 Wave Panel ------------------------------        
    GridLayout: 
        rows: 2
        cols: 5
        canvas.after:
            Color:
                rgba:[.4, .4 , .4, .7 ]
            Line:
                width:2
                rounded_rectangle: (*self.pos,self.width,self.height, 2)
                
        BoxLayout:
            orientation: 'vertical'
            spacing:2
            ToggleButton:
                text: 'OSC 2'      
            Spinner:
                text: 'SAW'
                values: ['SIN', 'SAW', 'TRI', 'SQR', 'PWM', 'DETUNE SAW', 'NOISE', 'INPUT']
            BoxLayout:
                ToggleButton:
                    text: 'Ring'
                    size_hint_x: .5                            
                Spinner:
                    text: 'Sync'
                    values: ['Sync Off', 'Sync On', 'Sync LoFi']                 
                
        CircleKnob:
            knob_title: 'PITCH'
        CircleKnob:
            knob_title: 'FINE'
        CircleKnob:
            knob_title: 'PULSE WIDTH'
        CircleKnob:
            knob_title: 'DETUNE'
        CircleKnob:
            knob_title: 'SHARPNESS'
        
        XYKnob:
            xy_knob_title:' PWM ENV '   # we space pad the title so it is about the same length as other titles
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        XYKnob:
            xy_knob_title:'PITCH ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        
        
        
        CircleKnob:
            knob_title: 'PBEND DEPTH'
        CircleKnob:
            knob_title: 'PBEND CTL'
        
    Button:
        text: 'Filter 2'
        size_hint_x: .1
    Button:
        text: 'Seven'
        size_hint_x: .1
    Button:
        text: 'Eight'
        size_hint_x: .1
    #  ------------------------------------------------OSC 2 Wave Panel ------------------------------        
    GridLayout: 
        rows: 2
        cols: 5
        canvas.after:
            Color:
                rgba:[.4, .4 , .4, .7 ]
            Line:
                width:2
                rounded_rectangle: (*self.pos,self.width,self.height, 2)
                
        BoxLayout:
            orientation: 'vertical'
            spacing:2
            ToggleButton:
                text: 'OSC 2'      
            Spinner:
                text: 'SAW'
                values: ['SIN', 'SAW', 'TRI', 'SQR', 'PWM', 'DETUNE SAW', 'NOISE', 'INPUT']
            BoxLayout:
                ToggleButton:
                    text: 'Ring'
                    size_hint_x: .5                            
                Spinner:
                    text: 'Sync'
                    values: ['Sync Off', 'Sync On', 'Sync LoFi']                 
                
        CircleKnob:
            knob_title: 'PITCH'
        CircleKnob:
            knob_title: 'FINE'
        CircleKnob:
            knob_title: 'PULSE WIDTH'
        CircleKnob:
            knob_title: 'DETUNE'
        CircleKnob:
            knob_title: 'SHARPNESS'
        
        XYKnob:
            xy_knob_title:' PWM ENV '   # we space pad the title so it is about the same length as other titles
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        XYKnob:
            xy_knob_title:'PITCH ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
        
        
        
        CircleKnob:
            knob_title: 'PBEND DEPTH'
        CircleKnob:
            knob_title: 'PBEND CTL'

    Button:
        text: 'Filter 3'
        size_hint_x: .1 
    Button:
        text: 'Elven'
        size_hint_x: .1
    Button:
        text: 'Twelve'
        size_hint_x: .1
        
        
"""


class PanelApp(App):

    def build(self):
        return Builder.load_string(kv)


PanelApp().run()
