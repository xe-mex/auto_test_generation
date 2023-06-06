from dotenv import load_dotenv
import argparse
from os import environ

load_dotenv(".env")

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--in", dest="inputFile", default=None)
parser.add_argument("-o", "--out", dest="outputFile", default=None)
parser.add_argument("-c", "--count", dest="countTests", default=None)
parser.add_argument("-mu", "--mu", dest="mu", default=None)
parser.add_argument("-s", "--sigma", dest="sigma", default=None)
args = parser.parse_args()

config = {
    "inputFile": args.inputFile or environ.get("inputFile") or input("Input path to gds example file:\n"),
    "outputFile": args.outputFile or environ.get("outputFile") or "./out.gds",
    "countTests": args.countTests or environ.get("countTests") or 1,
    "mu": args.mu or environ.get("mu") or 0,
    "sigma": args.sigma or environ.get("sigma") or 1
}

# print(int(config["countTests"]))
