import gdspy


def save_test():
    # The GDSII file is called a library, which contains multiple cells.
    lib = gdspy.GdsLibrary()

    # Geometry must be placed in cells.
    cell = lib.new_cell('FIRST')

    # Create the geometry (a single rectangle) and add it to the cell.
    rect = gdspy.Rectangle((0, 0), (2, 1))
    cell.add(rect)

    # Save the library in a file called 'first.src'.
    lib.write_gds('./files/first.gds')

    # Optionally, save an image of the cell as SVG.
    cell.write_svg('./files/first.svg')

    # Display all cells using the internal viewer.
    gdspy.LayoutViewer()


def test2():
    lib = gdspy.GdsLibrary()

    # Layer/datatype definitions for each step in the fabrication
    ld_fulletch = {"layer": 1, "datatype": 3}
    ld_partetch = {"layer": 2, "datatype": 3}
    ld_liftoff = {"layer": 0, "datatype": 7}

    p1 = gdspy.Rectangle((-3, -3), (3, 3), **ld_fulletch)
    p2 = gdspy.Rectangle((-5, -3), (-3, 3), **ld_partetch)
    p3 = gdspy.Rectangle((5, -3), (3, 3), **ld_partetch)
    p4 = gdspy.Round((0, 0), 2.5, number_of_points=6, **ld_liftoff)

    # Create a cell with a component that is used repeatedly
    contact = lib.new_cell("CONTACT")
    contact.add([p1, p2, p3, p4])

    # Manually connect the hole to the outer boundary
    cutout = gdspy.Polygon(
        [(0, 0), (5, 0), (5, 5), (0, 5), (0, 0), (2, 2), (2, 3), (3, 3), (3, 2), (2, 2)]
    )

    # Create a cell with the complete device
    device = lib.new_cell("DEVICE")
    device.add(cutout)
    # Add 2 references to the component changing size and orientation
    ref1 = gdspy.CellReference(contact, (3.5, 1), magnification=0.25)
    ref2 = gdspy.CellReference(contact, (1, 3.5), magnification=0.25, rotation=90)
    device.add([ref1, ref2])

    # The final layout has several repetitions of the complete device
    main = lib.new_cell("MAIN")
    main.add(gdspy.CellArray(device, 3, 2, (6, 7)))
    lib.write_gds("./files/second.gds")
    main.write_svg("./files/second.svg")


def load_file_test1():
    lib = gdspy.GdsLibrary(infile="./files/second.gds")
    cells = lib.cells
    pass


def save_gds_by_cells(cells, output_path):
    print(cells)
    lib = gdspy.GdsLibrary()
    # b = lib.new_cell("test")
    # a = gdspy.Rectangle((-5, -3), (5, 3), layer=1)

    # c = gdspy.Rectangle((-3, -5), (3, 5), layer=1)
    # b.add(a)
    # b.add(c)
    # polygons = b.get_polygons()
    # print(polygons)
    # cutout = gdspy.Polygon(
    #     [(0, 0), (5, 0), (5, 5), (0, 5), (0, 0), (2, 2), (2, 3), (3, 3), (3, 2), (2, 2)]
    # )
    # cutout = gdspy.Polygon(
    #     [(2, 2), (2, 3), (3, 3), (3, 2), (2, 2), (1, 1), (5, 1), (5, 5), (1, 5), (1, 1)]
    # )
    # cutout = gdspy.Polygon(
    #     [
    #      (0, 0), (5, 0), (5, 5), (0, 5), (0, 0),
    #      (1, 1), (1, 4), (4, 4), (4, 1), (1, 1),
    #      (2, 2), (2, 3), (3, 3), (3, 2), (2, 2)
    #     ]
    # )
    # b.add(cutout)
    for name, cell in cells.items():
        # print(cell.get_polygons())
        lib.add(cell)
        # cell.write_svg(f"./files/cell_{name}.svg")
    # lib.add(b, include_dependencies=True, update_references=True)
    lib.write_gds(output_path)
    # b.write_svg("./files/out.svg")
    gdspy.LayoutViewer(lib)
