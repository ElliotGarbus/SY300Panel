from kivy.app import App
from kivy.lang import Builder

kv = """
#:import XYKnob xyknob
#:import CircleKnob circleknob
#:import ADKnob adknob

<LFO@GridLayout>
    rows:2
    cols:4
    size_hint_x: .8
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            padding: 5
            orientation: 'vertical'
            canvas.after:
                Color:
                    rgba:[.4, .4 , .4, .7 ]
                Line:
                    width:2
                    rounded_rectangle: (*self.pos,*self.size, 2) # *self.size
            Label:    
                text: 'LFO'
            Switch:
        Spinner:
            text: 'Wave'
            values: ['SIN', 'SAW UP', 'SAW DOWN','TRI', 'SQR', 'RANDOM', 'S & H']
         
    CircleKnob:
        knob_title: 'PTCH DPTH'
    CircleKnob:
        knob_title: 'FLTR DPTH'
    CircleKnob:
        knob_title: 'AMP DPTH' 
    BoxLayout:
        canvas.after:
            Color:
                rgba:[.4, .4 , .4, .7 ]
            Line:
                width:2
                rounded_rectangle: (*self.pos,self.width *2, self.height, 2)
        BoxLayout:
            orientation: 'vertical'
            Label:    
                text: 'RATE/BPM'
            Spinner:
                text: 'RATE'
                values: ['0-100', 'Whole Note', 'Dotted Half Note', 'Triplet Whole Note', 'Half Note', 'Dotted Qtr Note', 'Triplet of Half Note', 'Qtr Note', 'Dotted 8th Note', 'Triplet of Qtr Note', '8th Note', 'Dotted 16th Note','Triplet of 8th Note', '16th Note', 'Dotted 32th Note', 'Triplet of 16th Note', '32th Note']                     
    CircleKnob:
        knob_title: 'RATE'          
    BoxLayout:
        canvas.after:
            Color:
                rgba:[.4, .4 , .4, .7 ]
            Line:
                width:2
                rounded_rectangle: (*self.pos,self.width *2, self.height, 2)
        BoxLayout:
            orientation: 'vertical'
            Label:    
                text: 'Dynamic Depth'
            Switch:                
    CircleKnob:
        knob_title: 'FADE TIME' 
#------------END LFO DEFINITION                            

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
#------------------------------------------ OSC 1 Filter Panel ------------------------------------------            
    GridLayout:
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
        
        XYKnob:
            xy_knob_title:'ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
  
        ADKnob:
        
        CircleKnob:
            knob_title: 'LEVEL'
        CircleKnob: 
            knob_title: 'PAN'   
                                
    LFO:
        id: LFO_1_1
    LFO:
        id: LFO_1_2          

#------------------------------------------------OSC 2 Wave Panel ------------------------------        
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
        
#------------------------------------------ OSC 2 Filer Panel ------------------------------------------            
    GridLayout:
        rows: 2
        cols: 3
        size_hint_x: .6
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
        
        XYKnob:
            xy_knob_title:'ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
  
        ADKnob:
        
        CircleKnob:
            knob_title: 'LEVEL'
        CircleKnob: 
            knob_title: 'PAN'   

    LFO:
        id: LFO_2_1
    LFO:
        id: LFO_2_2          

#  ------------------------------------------------OSC 3 Wave Panel ------------------------------        
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
                text: 'OSC 3'      
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
#------------------------------------------ OSC 3 Filter Panel ------------------------------------------            
    GridLayout:
        rows: 2
        cols: 3
        size_hint_x:.6
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
        
        XYKnob:
            xy_knob_title:'ENV'
            xy_knob_xlab: 'ATTACK'
            xy_knob_ylab: 'DEPTH'
  
        ADKnob:
        
        CircleKnob:
            knob_title: 'LEVEL'
        CircleKnob: 
            knob_title: 'PAN'   
        
    LFO:
        id: LFO_3_1
    LFO:
        id: LFO_3_2          

        
        
"""


class PanelApp(App):

    def build(self):
        return Builder.load_string(kv)


PanelApp().run()
