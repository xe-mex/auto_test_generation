from dotenv import load_dotenv
import argparse
from os import environ
from json import load

load_dotenv(".env")

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--in", dest="inputFile", default=None)
parser.add_argument("-o", "--out", dest="outputFile", default=None)
parser.add_argument("-c", "--count", dest="countTests", default=None)
parser.add_argument("-mu", "--mu", dest="mu", default=None)
parser.add_argument("-s", "--sigma", dest="sigma", default=None)
parser.add_argument("-f", "--config", dest="config", default=None)
parser.add_argument("-n", "--name", dest="func_name", default=None)
args = parser.parse_args()


def show_help():
    print("""
        Expected path to input file and function name
        
        Examples:
            python main.py -i ./test1.gds -n area
            python main.py --in ./test1.gds --name area
            set inputFile=./test1.gds && set fucn_name=area && python main.py
    """)
    # raise Exception("specify path to input file")
    # print("specify path to input file")
    exit(-1)


config = {
    "inputFile": args.inputFile or environ.get("inputFile") or show_help(),
    "outputFile": args.outputFile or environ.get("outputFile") or "./out.gds",
    "countTests": args.countTests or environ.get("countTests") or 1,
    "mu": args.mu or environ.get("mu") or 0,
    "sigma": args.sigma or environ.get("sigma") or 1,
    "config": args.config or environ.get("config") or None,
    "func_name": args.func_name or environ.get("func_name") or show_help()
}

_advanced_config = None

if config["config"]:
    with open(config["config"], 'r', encoding="utf-8") as f:
        _advanced_config = load(f)
        # print(config_json)


def get_config_for_cell(cell_name):
    if not _advanced_config:
        return None
    return (_advanced_config.get("cells") and _advanced_config.get("cells").get(cell_name)) or _advanced_config.get("global")

# print(int(config["countTests"]))
