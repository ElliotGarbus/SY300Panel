import configstartup  # brings in commands to size window, and sets to correct windows taskbar icon
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty, StringProperty, NumericProperty, ListProperty
from spinnerknob import SpinnerKnob
from sy300midi import set_sy300, get_midi_ports, req_sy300
import mido
from kivy.clock import Clock
import os, sys

kivy.require('1.10.1')


class Filter(GridLayout):
    pass


class OSC(GridLayout):
    text = StringProperty('')


class LFO(GridLayout):
    text = StringProperty('')
    lfo_num = NumericProperty(0)


class RateComboKnob(SpinnerKnob):
    addresses = ListProperty([])

    # if the spinner is at zero, selecting 0-100, then the knob associated with the spinner is active.
    # There is a single address for the RateComboKnob with values from 0 to 116
    # The logic is in set_knob method of the RateComboKnob class

    def set_knob(self, adr, value):
        if value <= 100:
            self.parent.parent.ids.rate_knob.value = value
            self.text = self.values[0]
        else:
            self.text = self.values[value - 100]


class OSCStrip(BoxLayout):
    is_osc_1 = BooleanProperty(False)
    osc_text = StringProperty('')
    osc_adr = NumericProperty()


class NoSY300Connected(Popup):
    pass


class PanelApp(App):
    title = 'SY300 OSC Sound Generation Control Panel'
    # Window.size = (1725, 710)  # This code was replaced by Config.set code in configstartup.py
    # Window.top = 285  # 0 is the top of the screen
    # Window.left = 185
    adr2knob = {}

    def open_settings(self, *largs):  # prevents the kivy settings panel from opening
        pass

    @staticmethod
    def close_it():  # close the app if the SY300 is not connected and the quit button is pressed.
        exit(0)

    def build(self):
        if getattr(sys, 'frozen', False):    # required so data files can be packed by pyinstaller
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)
        iconfile = os.path.join(application_path, 'SY300logo64.png')
        kvfile = os.path.join(application_path, 'osc_panel.kv')

        self.icon = iconfile
        r = Builder.load_file(kvfile)
        # rate/combo switch needs special dealings, as there is ONE address for TWO widgets.... don't drop them!
        for osc in r.children:    # these children should be the three strips
            for c in osc.walk(restrict=True, loopback=False):
                if hasattr(c, 'addresses'):
                    for a in c.addresses:
                        self.adr2knob[osc.osc_adr,  a] = c
                if hasattr(c, 'comaddresses'):
                    for a in c.comaddresses:
                        self.adr2knob[0x18, a] = c

        # remove bogus key(s)
        boguskeys = [(o, a) for o, a in self.adr2knob.keys() if a > 400]
        for bogus in boguskeys:
            del self.adr2knob[bogus]

        # print('DEBUG: collected knobs for:')
        # for k in sorted(self.adr2knob.keys(),key=lambda x: x[0]*100+x[1]):
        #    if hasattr(self.adr2knob[k], 'text'):
        #        print('  ', k, ' text is ', self.adr2knob[k].text, self.adr2knob[k])
        #    else:
        #        print('  ', k , '(knob does not have text field)', self.adr2knob[k])
        return r

    @staticmethod
    def send2midi(osc, adr, val):
        global to_sy300
        to_sy300.send(set_sy300([0x20, 0x00, osc, adr], [val]))

    def callback_read_midi(self, dt):
        global from_sy300  # Message from MIDI: sysex data=(65,16,0,0,0,19,18,32,0,32,1,3,60)
        for msg in from_sy300.iter_pending():
            if msg.type == 'sysex':
                adr = msg.data[9:11]
                for d in msg.data[11:-1]:
                    if adr in self.adr2knob:
                        self.adr2knob[adr].set_knob(adr[1], d)
                    adr = (adr[0], adr[1]+1)

    def on_start(self):
        global to_sy300
        global from_sy300
        global midi_ports
        midi_ports = get_midi_ports()
        if not midi_ports:
            # print("Connection Failure: SY300 not connected")
            no_sy300_popup = NoSY300Connected()
            no_sy300_popup.open()
        else:
            # print(f"SYS300 input:{midi_ports['in']}  output: {midi_ports['out']}")
            to_sy300 = mido.open_output(midi_ports['out'])
            from_sy300 = mido.open_input(midi_ports['in'])
            Clock.schedule_interval(self.callback_read_midi, .1)  # read the midi port at a regular interval
            to_sy300.send(set_sy300([0x7F, 0x00, 0x00, 0x01], [0x01]))  # set the SY300 into verbose or editor mode
            to_sy300.send(req_sy300([0x20, 0x00, 0x18, 0x00], [4]))  # req the state of the ring and Sync for osc 2&3
            to_sy300.send(req_sy300([0x20, 0x00, 0x20, 0x00], [0x29]))  # req all of the knob settings for OSC1
            to_sy300.send(req_sy300([0x20, 0x00, 0x28, 0x00], [0x29]))  # ...OSC2
            to_sy300.send(req_sy300([0x20, 0x00, 0x30, 0x00], [0x29]))  # ...and OSC 3

    def on_stop(self):
        global to_sy300
        global from_sy300
        global midi_ports
        if midi_ports:      # if the midi_ports were not opened, do not close at shutdown.
            to_sy300.send(set_sy300([0x7F, 0x00, 0x00, 0x01], [0x00]))  # set the SY300 to turn off verbose/editor mode
            to_sy300.close()
            from_sy300.close()


PanelApp().run()
