import argparse
import geopandas

from time import time


TOOL = "CENTROID"


def centroid(input_filename: str, output_filename: str, within: bool):
    t_start = time()

    input_file = geopandas.read_file(input_filename)

    if not within:
        output_file = input_file.centroid()
    else:
        output_file = input_file.representative_point()

    output_file.to_file(output_filename)

    t_end = time()
    return f"{TOOL} - COMPLETED IN {t_end - t_start:.5f}s."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Make centroid from ")
    parser.add_argument("-i", "--input", help="(required) input file path")
    parser.add_argument("-o", "--output", help="(required) output file path")
    parser.add_argument("-w", "--within", help="use if centroids has to be within objects", action='store_true')
    args = parser.parse_args()

    if not args.input or not args.output:
        for arg in vars(args):
            if getattr(args, arg) is None:
                print(f"{TOOL} - no `{arg}` parameter")

    else:
        result = centroid(args.input, args.output, args.within)
        print(result)
