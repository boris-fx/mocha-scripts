# BSD 3-Clause License
#
# Copyright (c) 2021, Boris FX
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

__author__ = 'Boris FX'

from mocha import ui


mocha_widgets = ui.get_widgets()
main_window = mocha_widgets['MainWindow']

main_window.setStyleSheet(
    "QMainWindow { background-color: #21252B;}"
    "QMainWindow::separator {background-color: #282C34;}"
    "QDockWidget QWidget {background-color: #21252B;}"
    "QPushButton { background-color: #21252B; color: #979EAA; font: bold}"
    "QPushButton::hover { background-color: #4f545E; color: #979EAA; font: bold}"
    "QToolButton { background-color: #21252B; }"
    "QToolButton:checked { background-color: #6494ED; }"
    "QToolButton:hover { background-color: #4f545E; }"
    "QLabel {font: 14px;}"
    "QFrame {background-color: #21252B;}"
    "QToolBox {background-color: #282C34;}"
    "QListView {background-color: #282C34;}"
    "QTreeView {background-color: #282C34;}"
    "QLineEdit {background-color: #21252B;}"
    "QComboBox {background-color: #282C34;}"
    "QGroupBox {background-color: #282C34;}"
    "QCheckBox {background-color: #282C34;}"
    "QRadioButton {background-color: #282C34;}"
    "QToolBar {background-color: #282C34;}"
    "QTableView {background-color: #282C34;}"
    "QMenu {background-color: #282C34;}"
    "QMenuBar {background-color: #282C34;}"
    "QProgressBar {background-color: #282C34;}"
    "QSlider {background-color: #282C34;}"
    "QScrollBar {background-color: #282C34;}"
    "QDialog {background-color: #282C34;}"
    "QTextFrame {background-color: 21252B;}"
    "QStatusBar {background-color: #282C34;}"
    "#timelineControlsW {background-color: #282C34;}"
    "#sldrFrameNumber::enabled {selection-background-color: red;}"
    "QTabBar::tab {background: #2E2B30;}"
    "QTabBar::tab:selected {background: black;}"
    "QTabWidget::pane QWidget{background-color: #282C34;}"
)
