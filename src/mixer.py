import gdspy
from random import normalvariate, triangular, randrange
from src.configurator import config
from math import pi


def mix(cells):
    mixed_cells = {}
    for name, cell in cells.items():
        temp_cell = gdspy.Cell(name)
        temp_pol = _mix_polygons(cell.get_polygons())
        temp_cell.add(temp_pol)
        mixed_cells[name] = temp_cell
    return mixed_cells


def _mix_polygons(polygons):
    mixed_polygons = []
    for polygon in polygons:
        # print(polygon)
        new_polygon = gdspy.Polygon(polygon)
        step = 0
        while True:
            _update_polygon(new_polygon, step)
            if _check_polygon(new_polygon, mixed_polygons):
                break
            else:
                step += 1
        mixed_polygons.append(new_polygon)
    return mixed_polygons


def _update_polygon(polygon, modify=1, step=0):
    polygon.translate((modify * _gen_var()) + step, (modify * _gen_var()) + step)
    # polygon.translate(_gen_var(), _gen_var())
    polygon.scale(_gen_var(), _gen_var())
    polygon.rotate(triangular(0, pi, float(config["mu"])))
    pass


def _check_polygon(polygon, polygons):
    for pol in polygons:
        # temp_pol = gdspy.Polygon(pol)
        result = gdspy.boolean(polygon, pol, "and")
        if result:
            print("match detected")
            return False
    return True


def _gen_var():
    return normalvariate(float(config["mu"]), float(config["sigma"]))
    # return randrange(1, 2)
