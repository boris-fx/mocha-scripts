# BSD 3-Clause License
#
# Copyright (c) 2026, Boris FX
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


# If 2026, use PySide6. If 2025.5 or earlier (to v6), use Pyside2.
try:
    from PySide2.QtWidgets import *
except ImportError:
    from PySide6.QtWidgets import *

from mocha.project import get_current_project
from mocha.ui import get_widgets


class LayerPrepend():

    def __init__(self):

        self.app = QApplication.instance()
        self.layer_tree = self.get_layer_tree()
        self.layer_prepend()

    def get_layer_tree(self):
        widgets = get_widgets()
        return widgets['LayerControl']

    def layer_prepend(self):

        selected_layers = self.layer_tree.selectedIndexes()

        if len(selected_layers) > 0:
            dlg = QDialog()
            layout = QFormLayout()
            edt = QLineEdit()
            layout.addRow("Prefix", edt)
            btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            btn_box.accepted.connect(dlg.accept)
            btn_box.rejected.connect(dlg.reject)
            layout.addRow(btn_box)
            dlg.setLayout(layout)
            if dlg.exec_() == QDialog.Accepted:
                self.prepend_selected_layers(edt.text())
                #self.layer_tree.update()

    def prepend_selected_layers(self, prefix):

        project = get_current_project()
        selected_layers = self.layer_tree.selectedIndexes()

        for idx in selected_layers:
            layer = project.layer(idx.row())
            layer.name = prefix + layer.name
