import gdspy
from copy import deepcopy


def get_cells_from_gds(path):
    cells = gdspy.GdsLibrary(infile=path, unit="import").cells
    return deepcopy(cells)
