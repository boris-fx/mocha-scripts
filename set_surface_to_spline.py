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

from mocha.project import get_current_project
from mocha.ui import get_widgets

# If 2026, use PySide6. If 2025.5 or earlier (to v6), use Pyside2.
try:
    from PySide2.QtWidgets import QApplication
except ImportError:
    from PySide6.QtWidgets import QApplication

class SetSurfaceToSpline():

    def __init__(self):

        self.app = QApplication.instance()

        print("INITIALISING SET LAYER SURFACE CLASS")
        self.proj = get_current_project()
        layer_tree = self.get_layer_tree()
        self.selected_idxs = layer_tree.selectedIndexes()

    def get_layer_tree(self):
        widgets = get_widgets()
        return widgets['LayerControl']

    def get_surface_parameters(self, layer):

        name = layer.name

        # replace spaces in name with underscores to match internal project names
        if ' ' in name:
            name = name.replace(' ', '_')

        surface_corners = []
        for idx in range(0, 4):
            xy_data = [self.proj.parameter([name, u'Surface' + str(idx) + u'X']).get(),
                       self.proj.parameter([name, u'Surface' + str(idx) + u'Y']).get()]
            surface_corners.append(xy_data)
        surface_frame = self.proj.parameter([name, u'SurfaceFrame']).get()

        # print(surface_corners)
        return surface_corners, surface_frame

    def set_surface_corners(self):

        for idx in self.selected_idxs:
            layer = self.proj.layer(idx.row())

        name = layer.name
        # replace spaces in name with underscores to match internal project names
        if ' ' in name:
            name = name.replace(' ', '_')

        contour_points = layer.contours[0].control_points

        surface_corners = self.get_surface_parameters(layer)[0]

        if len(contour_points) > 4:
            print("Choose a layer with only 4 spline points")
        else:
            try:
                point_xy_data = []
                for point in contour_points:
                    data = point.get_point_data(0)
                    point_xy_data.append([data.x, data.y])

                min_sum = min([sum(p) for p in point_xy_data])
                max_sum = max([sum(p) for p in point_xy_data])

                c0 = [p for p in point_xy_data if sum(p) == min_sum][0]
                c3 = [p for p in point_xy_data if sum(p) == max_sum][0]

                point_xy_data.remove(c0)
                point_xy_data.remove(c3)

                min_sum = min([sum(p) for p in point_xy_data])
                max_sum = max([sum(p) for p in point_xy_data])

                c1 = [p for p in point_xy_data if sum(p) == min_sum][0]
                c2 = [p for p in point_xy_data if sum(p) == max_sum][0]

                self.proj.parameter([name, u'Surface0X']).set(c0[0])
                self.proj.parameter([name, u'Surface0Y']).set(c0[1])
                self.proj.parameter([name, u'Surface1X']).set(c2[0])
                self.proj.parameter([name, u'Surface1Y']).set(c2[1])
                self.proj.parameter([name, u'Surface2X']).set(c1[0])
                self.proj.parameter([name, u'Surface2Y']).set(c1[1])
                self.proj.parameter([name, u'Surface3X']).set(c3[0])
                self.proj.parameter([name, u'Surface3Y']).set(c3[1])
            except:
                return 0
