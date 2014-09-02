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

from geometry import *
import graph
shape = graph.graph()
map_mapply([lambda x : [shape.connect((8, 4, 1), x)],lambda x : [dropPerpendicular(x, 2)],lambda x : connect3(x, 2),lambda x : [shape.connect((1, 5, 6), x)],lambda x : [shape.connect((13, 6, 8), x)]], map(lambda t : bezier_form(t, ((4, 1, 0), (2, 14, 5), (12, 10, 7), (10, 10, 15))), make_scalar_list(10)))
shape.create_mesh('test.mesh')
return shape

