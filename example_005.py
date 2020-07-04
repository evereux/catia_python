#! /usr/bin/python3.6

"""
    Example 5:

    Creates a new CATIA file.

    Reads a csv file containing point data and adds to the new catia part.


    Formatting of csv data should be:
        <point_name>,<x coordinate>,<y coordinate>,<z coordinate>

"""

from pycatia import catia
from pycatia.scripts.csv_tools import create_points

# # disable display refreshing to try tp speed up point generation.
# catia.refresh_display = False
# # hide catia window
# catia.visible = False

documents = catia.documents
# create a new part.
documents.add('Part')

document = catia.active_document
part = document.part()

# full path name to csv file.
file = r'tests\Sample_Point_CSV_File1_small.csv'

# create the points.
create_points(part, file, units='in', geometry_set_name='Points_Construction')

# # re-enable display refresh
# catia.refresh_display = True
# # unhide catia window
# catia.visible = True