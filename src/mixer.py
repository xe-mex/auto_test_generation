import gdspy
from src.randomizer import gen_value_scale, gen_rotate_angular, gen_value_translate


def mix(cells):
    mixed_cells = {}
    for name, cell in cells.items():
        temp_cell = gdspy.Cell(name)
        temp_pol = _mix_polygons(cell, name)
        temp_cell.add(temp_pol)
        mixed_cells[name] = temp_cell
    return mixed_cells


def _mix_polygons(cell, cell_name):
    # polygons = cell.get_polygons()
    mixed_polygons = []
    # for polygon in polygons:
    for polygon in cell.polygons:
        # print(polygon)
        # new_polygon = gdspy.Polygon(polygon)
        new_polygon = polygon
        step = 0
        while True:
            _update_polygon(new_polygon, cell_name, step=step)
            if _check_polygon(new_polygon, mixed_polygons):
                break
            else:
                step += 1
        mixed_polygons.append(new_polygon)
    return mixed_polygons


def _update_polygon(polygon, cell_name, *, modify=1, step=0):
    polygon.scale(gen_value_scale(cell_name))
    (m1, m2) = (gen_value_translate(cell_name, modify=modify, step=step))
    polygon.translate(m1, m2)
    # polygon.translate(_gen_var(), _gen_var())
    # polygon.rotate(gen_rotate_angular(cell_name))
    pass


def _check_polygon(polygon, polygons):
    for pol in polygons:
        # temp_pol = gdspy.Polygon(pol)
        # print([method for method in dir(polygon) if method.startswith('__') is False])
        if polygon.layers[0] != pol.layers[0]:
            continue
        result = gdspy.boolean(polygon, pol, "and")
        if result:
            print("match detected")
            return False
    return True
