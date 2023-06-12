from src.saver import save_test, test2, load_file_test1, save_gds_by_cells, test3
from src.configurator import config
from src.opener import get_cells_from_gds
from src.mixer import mix


def main():
    # print("main...")
    # save_test()
    # test2()
    # test3()
    cells_copy = mix(get_cells_from_gds(config["inputFile"]))
    save_gds_by_cells(cells_copy, config["outputFile"])
    # print(config)


if __name__ == "__main__":
    main()
else:
    print(f"${__name__} is not module!")
