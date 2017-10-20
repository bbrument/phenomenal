# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================

# ==============================================================================


class VoxelSegment(object):

    def __init__(self, voxels_position, polyline):

        self.voxels_position = voxels_position
        self.polyline = polyline

    def __len__(self):
        return len(self.voxels_position)