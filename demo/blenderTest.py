# This file is part of Architype.
# Architype is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# Architype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Architype.  If not, see <http://www.gnu.org/licenses/>.
# Author Jonathan Byrne 2014

import os
os.chdir('../')

from geometry import *
import graph


shape = graph.graph()


#map_result = map(lambda t : bezier_form(t, ((0, 7, 4), (10, 11, 14), (6, 2, 7), (4, 7, 5))), make_scalar_list(9))

#mapply_result = map_mapply([lambda x : [shape.connect((10, 2, 10), x)]], map(lambda t : bezier_form(t, ((0, 7, 4), (10, 11, 14), (6, 2, 7), (4, 7, 5))), make_scalar_list(9)))
#print "map:", map_result
#print "mapply:", mapply_result


#map_mapply([lambda x : [shape.connect((0, 0, 4), x)]], map(lambda t : circlePath(t, 12, (12, 5, 3), 2), make_scalar_list(2)))
print map(lambda t : circlePath(t, 0, (4000, 9000, 4000), 2), make_scalar_list(6))

print map_mapply([lambda x : connect3(shape, x, 0)], map(lambda t : circlePath(t, 0, (4000, 9000, 4000), 2), make_scalar_list(6)))

shape.create_mesh("blender")
