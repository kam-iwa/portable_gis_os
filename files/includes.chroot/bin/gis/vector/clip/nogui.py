import argparse
import geopandas

from time import time


TOOL = "CLIP"


def clip(input_filename: str, clip_filename: str, output_filename: str):
    t_start = time()
    input_file = geopandas.read_file(input_filename)
    clip_file = geopandas.read_file(clip_filename)

    output_file = geopandas.clip(input_file, clip_file)
    output_file.to_file(output_filename)

    t_end = time()
    return f"{TOOL} - COMPLETED IN {t_end - t_start:.5f}s."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clip objects from layer by another layer.")
    parser.add_argument("-i", "--input", help="(required) input file path")
    parser.add_argument("-c", "--clip", help="(required) clip file path")
    parser.add_argument("-o", "--output", help="(required) output file path")
    args = parser.parse_args()

    if not args.input or not args.output:
        for arg in vars(args):
            if getattr(args, arg) is None:
                print(f"{TOOL} - no `{arg}` parameter")

    else:
        result = clip(args.input, args.clip, args.output)
        print(result)
