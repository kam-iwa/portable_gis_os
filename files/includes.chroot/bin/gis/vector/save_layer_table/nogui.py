import argparse
import geopandas

from time import time


TOOL = "SAVE LAYER TABLE"


def save_layer_table(input_filename: str, output_filename: str):
    t_start = time()

    input_file = geopandas.read_file(input_filename)
    input_file = input_file.drop('geometry', axis=1)
    input_file.to_csv(output_filename, sep=';', index=True, header=True)

    t_end = time()
    return f"{TOOL} - COMPLETED IN {t_end - t_start:.5f}s."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Save attribute table from vector layer file to text file")
    parser.add_argument("-i", "--input", help="(required) input file path")
    parser.add_argument("-o", "--output", help="(required) output file path")
    args = parser.parse_args()

    if not args.input or not args.output:
        for arg in vars(args):
            if getattr(args, arg) is None:
                print(f"{TOOL} - no `{arg}` parameter")
    else:
        result = save_layer_table(args.input, args.output)
        print(result)
