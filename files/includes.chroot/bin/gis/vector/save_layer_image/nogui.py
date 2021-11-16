import argparse
import geopandas

from time import time
from matplotlib import pyplot as plt


TOOL = "SAVE LAYER IMAGE"


def save_layer_image(input_filename: str, output_filename: str, color: str):

    t_start = time()

    fig, ax = plt.subplots()
    input_file = geopandas.read_file(input_filename)
    input_file.plot(ax=ax, color=color)
    fig.savefig(output_filename)

    t_end = time()
    return f"{TOOL} - COMPLETED IN {t_end - t_start:.5f}s."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display vector layer in new window. If output is defined, save image to file in output path")
    parser.add_argument("-i", "--input", help="(required) input file path")
    parser.add_argument("-o", "--output", help="(required) output image path")
    parser.add_argument("-c", "--color", help="(required) border color in hex (e.g #FFFFFF)")
    args = parser.parse_args()
    if not args.input or not args.color:
        for arg in vars(args):
            if getattr(args, arg) is None:
                print(f"{TOOL} - no `{arg}` parameter")
    else:
        result = save_layer_image(args.input, args.output, args.color)
        print(result)
