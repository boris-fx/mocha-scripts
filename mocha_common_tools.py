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

from mocha.project import *
from mocha.ui import find_widget

# Try PySide2, if not try Pyside6
try:
    from PySide2.QtWidgets import QLineEdit
    from PySide2.QtWidgets import QSlider
except ImportError:
    from PySide6.QtWidgets import QLineEdit
    from PySide6.QtWidgets import QSlider


def get_surface_parameters(layer, time=0, view=View(0)) -> list:
    surface_corners = []
    for idx in range(0, 4):
        surface_corners.extend(layer.get_surface_position(idx, time, view))
    return surface_corners


def get_current_playhead_time() -> float:
    current_time_widget = find_widget('tcedtCurrentFrame', QLineEdit)
    current_time = float(current_time_widget.text())

    return current_time


def set_current_playhead_time(frame):
    current_time_slider = find_widget('sldrFrameNumber', QSlider)

    try:
        current_time_slider.setValue(int(frame))
    except RuntimeError as ex:
        print(ex)

    return current_time_slider.value()


def get_selected_layers(proj) -> list:
    layers = proj.layers
    selected_layers = []
    for layer in layers:
        if layer.selected:
            selected_layers.append(layer)
    return selected_layers


def get_selected_control_points(proj) -> list:
    selected_points = []

    for layer in proj.layers:
        if layer.selected:
            for contour in layer.contours:
                for point in contour.control_points:
                    if point.selected:
                        selected_points.append(point)
    return selected_points


def set_selected_layer_param(proj, param: list, value) -> None:
    '''
    Sets parameter value in a layer based on the parameter list
    For example:
    ["Basic", "MotionBlurMatte"] has a value of True or False
    ["Basic", "BlendMode"] has a value of 0 (Add), 1 (Subtract) or 3 (Transparent)
    Calling the function:
    set_selected_layer_param(project, ["Basic", "BlendMode"], 0)
    '''

    layers = proj.layers

    for layer in layers:
        if layer.selected:
            layer.parameter(param).set(value)
