from kivy.config import Config
from kivy.utils import platform
import ctypes
'''
This code must be at the top of the 'main' executable file.  The call to SetCurrentProcessExplicitAppUserModelID()
is required to have windows display the correct icon on the toolbar.

Config.set('graphics'...) are used to set the size of the main window. 
'''
Config.set('graphics', 'width', 1725)
Config.set('graphics', 'height', 710)
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'top', 285)
Config.set('graphics', 'left', 185)

if platform == 'win':
    myappid = 'SY300 Panel'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
