import argparse
import geopandas

from time import time


TOOL = "DISSOLVE"


def dissolve(input_filename: str, output_filename: str, attribute: str = None):
    t_start = time()

    input_file = geopandas.read_file(input_filename)

    if not attribute:
        output_file = input_file.dissolve()
    else:
        output_file = input_file.dissolve(attribute)

    output_file.to_file(output_filename)

    t_end = time()
    return f"{TOOL} - COMPLETED IN {t_end - t_start:.5f}s."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dissolve objects from layer by attribute or into one object.")
    parser.add_argument("-i", "--input", help="(required) input file path")
    parser.add_argument("-o", "--output", help="(required) output file path")
    parser.add_argument("-a", "--attribute", help="attribute to dissolve")
    args = parser.parse_args()

    if not args.input or not args.output:
        for arg in vars(args):
            if getattr(args, arg) is None and str(arg) != "attribute":
                print("DISSOLVE - no `{}` parameter".format(arg))
    else:
        if args.attribute:
            result = dissolve(args.input, args.output, args.attribute)
        else:
            result = dissolve(args.input, args.output)
        print(result)
