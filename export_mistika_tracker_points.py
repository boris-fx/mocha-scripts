
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

from mocha.exporters import *

# If v6, use Pyside2. If V5 or earlier use Pyside
try:
    from PySide.QtCore import QByteArray
except ImportError:
    from PySide2.QtCore import QByteArray

class MistikaExporter(AbstractTrackingDataExporter):
    """
    Implementation of the Mistika Track exporter.
    """

    def __init__(self):
        super(MistikaExporter, self).__init__("Mistika Point Tracker File (*.trk)", "")  # Define the Mistika exporter
        self._project = None

    def error_string(self):
        return ""

    # Get the corner points of the surface for a given time and layer
    def get_surface_parameters(self, layer, time, view):
        surface_corners = []

        return surface_corners

    # Do the actual export
    def do_export(self, project, layer, tracking_file_path, time, view, options):
        ba = QByteArray()

        layer_in = layer.in_point()
        layer_out = layer.out_point()

        header = str(4) + "\n\n"  # initalize file with number of corner points
        point_header = str(layer_out) + "\n"  # number of frames
        mistika_order = [2, 3, 1, 0]

        
        ba.append(header.encode('utf-8'))
        for idx in mistika_order:
            ba.append(point_header.encode('utf-8'))
            for frame in range(layer_in, (layer_out)):
                surface_corner = layer.get_surface_position(idx, frame, view)
                result = format(frame, '.6f') + " " + " ".join(map(lambda x: str(format(x, '.6f')), surface_corner)) + " 0.000000 " + "\n"
                ba.append(result.encode('utf-8'))
            ba.append("\n\n".encode('utf-8'))
        return {tracking_file_path if tracking_file_path.lower().endswith(".trk") else tracking_file_path + '.trk': ba}
