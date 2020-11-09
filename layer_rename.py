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

import shiboken2
from PySide2.QtCore import *
from PySide2.QtGui import *


class LayerRenameDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self._widgets = dict()
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self._widgets['old_name'] = QLineEdit(self)
        self._widgets['new_name'] = QLineEdit(self)
        self._widgets['ok'] = QPushButton("OK", self)
        self._widgets['cancel'] = QPushButton("Cancel", self)

    def create_layout(self):
        main_layout = QGridLayout(self)
        form_layout = QFormLayout(self)
        form_layout.addRow("Old name:", self._widgets['old_name'])
        form_layout.addRow("New name:", self._widgets['new_name'])
        main_layout.addLayout(form_layout, 0, 0, 3, 3)
        main_layout.addWidget(self._widgets['ok'], 3, 1)
        main_layout.addWidget(self._widgets['cancel'], 3, 2)
        self.setLayout(main_layout)

    def create_connections(self):
        self._widgets['ok'].clicked.connect(self.do_rename)
        self._widgets['cancel'].clicked.connect(self.reject)

    def do_rename(self):
        proj = get_current_project()
        if not proj:
            self.reject()
        old_name = self._widgets['old_name'].text()
        new_name = self._widgets['new_name'].text()
        layers = proj.find_layers(old_name)
        if not layers:
            msg = QMessageBox(self)
            msg.setText("No layers with name %s" % old_name)
            msg.exec_()
            self.reject()
        map(lambda layer: setattr(layer, 'name', new_name), layers)
        self.accept()


if __name__ == "__main__":
    from mocha import ui

    mw = ui.get_widgets()['MainWindow']
    rename = LayerRenameDialog(parent=mw)
    rename.show()
