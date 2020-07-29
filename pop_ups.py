

A common error that can drive you crazy is forgetting to store the handle of the popup window you create in some python variable that will remain alive (e.g. in a data member of the main window).

The following is a simple program that creates a main window with a button where pressing the button opens a popup

#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from PyQt4.Qt import *

class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)