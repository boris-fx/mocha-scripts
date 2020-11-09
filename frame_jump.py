# BSD 3-Clause License
#
# Copyright (c) 2020, Boris FX
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
from mocha_common_tools import *
from mocha.tools import *

# If v6, use Pyside2. If V5 or earlier use Pyside
try:
    from PySide import QtGui, QtCore
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    from PySide2 import QtCore, QtWidgets
    # from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *

from mocha.project import get_current_project
from mocha.ui import get_widgets

main_window = get_widgets()['MainWindow']


class FrameJump(QDialog):
    def __init__(self, parent=main_window):
        if sys.version[0] == 3:
            super().__init__(parent)  # initialise using Python 3
        else:
            super(FrameJump, self).__init__(parent)  # initialise using Python 2
        self._widgets = dict()
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.proj = get_current_project()
        self.setWindowFlags(Qt.Tool)

    def create_widgets(self):
        self._widgets['Back'] = QPushButton("<", self)
        self._widgets['Frames'] = QLineEdit(self)
        self._widgets['Forward'] = QPushButton(">", self)
        self._widgets['Frames'].insert('10')

    def create_layout(self):
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self._widgets['Back'])
        main_layout.addWidget(self._widgets['Frames'])
        main_layout.addWidget(self._widgets['Forward'])

        self.setLayout(main_layout)

    def create_connections(self):
        self._widgets['Back'].clicked.connect(lambda: self.do_jump(-1))
        self._widgets['Forward'].clicked.connect(lambda: self.do_jump(+1))

    def do_jump(self, mult):
        current_time = int(get_current_playhead_time())
        frame_value = self._widgets['Frames'].text()
        next_frame = current_time + (int(frame_value) * mult)

        proj_range = self.proj.in_out_range

        if proj_range[0] < next_frame < proj_range[1]:
            err = set_current_playhead_time(next_frame)
        elif next_frame <= proj_range[0]:
            err = set_current_playhead_time(proj_range[0])
        elif next_frame >= proj_range[1]:
            err = set_current_playhead_time(proj_range[1])

        QCoreApplication.processEvents()
