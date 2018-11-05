from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty, StringProperty

kv = """
#:import XYKnob xyknob
#:import CircleKnob circleknob
#:import ADKnob adknob

<OSC>
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
            text: root.text      
        Spinner:
            text: 'SAW'
            values: ['SIN', 'SAW', 'TRI', 'SQR', 'PWM', 'DETUNE SAW', 'NOISE', 'INPUT']
        BoxLayout:
            ToggleButton:
                text: 'Ring'
                size_hint_x: .5
                opacity:   0 if root.is_osc_1 is True else 1
                disabled:  1 if root.is_osc_1 is True else 0                        
            Spinner:
                text: 'Sync'
                values: ['Sync Off', 'Sync On', 'Sync LoFi']
                opacity:   0 if root.is_osc_1 is True else 1
                disabled:  1 if root.is_osc_1 is True else 0                 
            
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


# ------------------------------ Filter --------------------------------------------
<Filter@GridLayout>
    size_hint_x: .6
    rows: 2
    cols: 3
    canvas.after:
        Color:
            rgba:[.4, .4 , .4, .7 ]
        Line:
            width:2
            rounded_rectangle: (*self.pos,self.width,self.height, 2)
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
        xy_knob_laboffset: 0
        xy_knob_xval: 0
        xy_knob_yval: 0
    
    XYKnob:
        xy_knob_title:'ENV'
        xy_knob_xlab: 'ATTACK'
        xy_knob_ylab: 'DEPTH'

    ADKnob:
    
    CircleKnob:
        knob_title: 'LEVEL'
    CircleKnob: 
        knob_title: 'PAN'   

# --------------------------------------LFO ------------------------------
<LFO> 
    rows:2
    cols:5
    canvas.after:
        Color:
            rgba:[.4, .4 , .4, .7 ]
        Line:
            width:2
            rounded_rectangle: (*self.pos,self.width,self.height, 2)
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            padding: 5
            orientation: 'vertical'
            canvas.after:
                Color:
                    rgba:[.4, .4 , .4, .7 ]
                Line:
                    width:1
                    dash_offset: 2
                    dash_length: 5
                    rounded_rectangle: (self.x + 5, self.y + 5,self.width -10, self.height * .85, 2) # *self.size
                    
            Label:    
                text: root.text
            Switch:
        Spinner:
            size_hint_y: .4
            text: 'Wave'
            values: ['SIN', 'SAW UP', 'SAW DOWN','TRI', 'SQR', 'RANDOM', 'S & H']
         
    CircleKnob:
        knob_title: 'PTCH DPTH'
    CircleKnob:
        knob_title: 'FLTR DPTH'
    CircleKnob:
        knob_title: 'AMP DPTH'
    CircleKnob:
        knob_title: 'PWM DPTH'
    Label:
        text:''
         
    BoxLayout:
        canvas.after:
            Color:
                rgba:[.4, .4 , .4, .7 ]
            Line:
                width:1
                dash_offset: 2
                dash_length: 5
                rounded_rectangle: (*self.pos,self.width *2, self.height, 2)
        BoxLayout:
            orientation: 'vertical'
            Label:    
                text: 'RATE/BPM'
            Spinner:
                size_hint_y: .4
                text: 'RATE'
                values: ['0-100', 'Whole', 'Dotted Half', 'Triplet Whole', 'Half', 'Dotted Qtr', 'Triplet of Half', 'Qtr', 'Dotted 8th', 'Triplet of Qtr', '8th', 'Dotted 16th','Triplet of 8th', '16th', 'Dotted 32th', 'Triplet of 16th', '32th']                     
    CircleKnob:
        knob_title: 'RATE'          
    BoxLayout:
        canvas.after:
            Color:
                rgba:[.4, .4 , .4, .7 ]
            Line:
                width:1
                dash_offset: 2
                dash_length: 5
                rounded_rectangle: (*self.pos,self.width *2, self.height, 2)
        BoxLayout:
            orientation: 'vertical'
            Label:    
                text: 'Dynamic\\n   Depth'
            Switch:                
    CircleKnob:
        knob_title: 'FADE TIME' 
#------------END LFO DEFINITION                            



GridLayout: # Holds all panels
    rows: 3
    cols: 4
    spacing: 10
    padding: 5
#------------------------------------------ OSC 1 Controls -------------------------   
    OSC:
        id: osc_1
        text: 'OSC 1'
        is_osc_1: True
    Filter:
        id: filter_1
                                
    LFO:
        id: LFO_1_1
        text: 'LFO 1/1'
    LFO:
        id: LFO_1_2
        text: 'LFO 1/2'         

#------------------------------------------ OSC 2 Controls ------------------------------           
    OSC:
        id: osc_2
        text: 'OSC 2'
    Filter:
        id: filter_2
    
    LFO:
        id: LFO_2_1
        text: 'LFO 2/1'   
    LFO:
        id: LFO_2_2
        text: 'LFO 2/2'             

#------------------------------------------ OSC 3 Controls -------------------------------            
    OSC:
        id: osc_3
        text: 'OSC 3'
    Filter:
        id: filter_3
    LFO:
        id: LFO_3_1
        text: 'LFO 3/1'   
    LFO:
        id: LFO_3_2
        text: 'LFO 3/2'            
"""

class OSC(GridLayout):
    is_osc_1 = BooleanProperty(False)
    text = StringProperty('')

class LFO(GridLayout):
    text = StringProperty('')



class PanelApp(App):

    def build(self):
        return Builder.load_string(kv)


PanelApp().run()
