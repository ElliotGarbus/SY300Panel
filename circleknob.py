from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty
from kivy.lang import Builder

Builder.load_string('''
#-------------------------------
# Knob class
#  Properties are: text, values, value
#
#-------------------------------
<CircleKnob>
    orientation: 'vertical'
    opacity: .25 if root.disabled else 1
    Label:
        font_size: 25
        color: [144/255, 228/255 , 1, 1] 
        text: root.values[root.value]
    
        canvas:
            Color:
                rgba: [.4, .4 , .4, .5] 
            Line:         
                circle: self.center_x, self.center_y, self.height/2 *.9, -140, 140
                cap: 'square'
                width: dp(3)
        canvas.after:
            Color:
                rgba: [144/255, 228/255 , 1, 1] 
            Line:         
                circle:
                    (
                    self.center_x, self.center_y,
                    self.height/2 *.9,
                    -140, -140 + root.value * 280 / ( len(root.values) - 1 )
                    )
                cap: 'square'
                width: dp(3)
    Label:
        font_size: 15
        text: root.text
        size: self.texture_size
        size_hint_y: None
        color: [144/255, 228/255 , 1, 1]
#-------------------------------
''')

class CircleKnob(BoxLayout):
    text = StringProperty()
    values = ListProperty([str(i) for i in range(101)])
    value = NumericProperty(0)
    #disabled = BooleanProperty(False)
    addresses = ListProperty( [] )
    _scroll_direction = {'scrollup': 1, 'scrolldown': -1}

    def on_touch_down(self, touch):
        if self.disabled is True:
            return False
        elif self.collide_point(*touch.pos):
            touch.grab(self)
            return True
        return False

    def on_touch_move(self, touch):
        if self.disabled is True:
            return False
        elif touch.grab_current is self and touch.dy:
            #sorted(min, val, max)[1] works to clamp val to floor or ceiling
            self.value = (sorted((0, self.value + int(touch.dy), len(self.values)-1))[1])
            return True
        return False

    def on_touch_up(self, touch):
        if self.disabled is True:
            return False
        elif touch.is_mouse_scrolling and touch.grab_current is self:
            # sorted(min, val, max)[1] works to clamp val to floor or ceiling
            self.value = (sorted((0, self.value + self._scroll_direction[touch.button],
                                    len(self.values) - 1))[1])
            return True
        elif touch.grab_current is self:
            touch.ungrab(self)
            return True
        return False

if __name__ == '__main__':
    kv_test = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: .1
        Button:
            text: "What an I doing here?"
        Button:
            text: "good question"
        Button:
            text: "knob input is obsolete"
        TextInput
            text: '1'
            on_text: primo.value =  int(self.text)
            multiline: False

    GridLayout:
        rows: 2
        cols: 6

        CircleKnob:
            id: primo
            text: "Pulse\\nWidth"
            values:  [str(x) for x in range(101)]
        CircleKnob:
            values: [str(x) for x in range(-24, 25)]
            value: 24
            text: 'Pitch'
        CircleKnob:
            values: ['L'+str(-x) for x in range(-50, 0)] + ['CTR'] + ['R'+ str(x) for x in range(1, 51)]
            value: 50
            text: 'Pan'
        CircleKnob:
            text: "Rate"
            disabled: True
        CircleKnob:
            text: "One"
            values:  [str(x) for x in range(101)]
        CircleKnob:
            values: [str(x) for x in range(-24, 25)]
            value: 3
            text: 'Pitch Bend'
        CircleKnob:
            values: ['L'+str(-x) for x in range(-50, 0)] + ['CTR'] + ['R'+ str(x) for x in range(1, 51)]
            value: 1
            text: 'Pan'
        CircleKnob:
            text: "Default"
        CircleKnob:
            text: "Pulse Width"
            values:  [str(x) for x in range(101)]
        CircleKnob:
            values: [str(x) for x in range(-24, 25)]
            value: 3
            text: 'Pitch'
        CircleKnob:
            values: ['L'+str(-x) for x in range(-50, 0)] + ['CTR'] + ['R'+ str(x) for x in range(1, 51)]
            value: 1
            text: 'Pan'
        CircleKnob:
            text: "Rate"
    '''

    class CircleKnobApp(App):

        def build(self):
            return Builder.load_string(kv_test)

    CircleKnobApp().run()
