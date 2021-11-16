import argparse
import geopandas

from time import time


TOOL = "BUFFER"


def buffer(input_filename: str, output_filename: str, distance: float):
    t_start = time()

    input_file = geopandas.read_file(input_filename)
    output_file = input_file.buffer(distance)
    output_file.to_file(output_filename)

    t_end = time()
    return f"{TOOL} - COMPLETED IN {t_end - t_start:.5f}s."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Make buffer from objects of layer. Buffer distance is in input layer units.")
    parser.add_argument("-i", "--input", help="(required) input file path")
    parser.add_argument("-o", "--output", help="(required) output file path")
    parser.add_argument("-d", "--distance", type=float, help="(required) buffer distance in layer units")
    args = parser.parse_args()
    if not args.input or not args.output or not args.distance:
        for arg in vars(args):
            if getattr(args, arg) is None:
                print(f"{TOOL} - no `{arg}` parameter")

    else:
        result = buffer(args.input, args.output, args.distance)
        print(result)
