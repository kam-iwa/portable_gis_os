import argparse
import geopandas

from time import time


TOOL = "SPATIAL JOIN"


def spatial_join(left_filename: str, right_filename: str, output_filename: str, join_type: str, join_relationship: str):
    t_start = time()
    left_file = geopandas.read_file(left_filename)
    right_file = geopandas.read_file(right_filename)

    output_file = geopandas.sjoin(left_file, right_file, how=join_type, op=join_relationship)
    output_file.to_file(output_filename)

    t_end = time()
    return f"{TOOL} - COMPLETED IN {t_end - t_start:.5f}s."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clip objects from layer by another layer.")
    parser.add_argument("-l", "--left", help="(required) left input file path")
    parser.add_argument("-r", "--right", help="(required) right input file path")
    parser.add_argument("-o", "--output", help="(required) output file path")
    parser.add_argument("-t", "--type", help="(required) type of join.\n Allowed: left, right, inner", type=str.lower)
    parser.add_argument("-e", "--relationship", help="(required) geometric relationship to base spatial join.\n"
                                                     "Allowed: intersects, contains, within, touches, crosses, overlaps", type=str.lower)
    args = parser.parse_args()

    if not args.left or not args.right or not args.output or not args.type or not args.relationship:
        for arg in vars(args):
            if getattr(args, arg) is None:
                print(f"{TOOL} - no `{arg}` parameter")

    else:
        if args.type not in ['left', 'right', 'inner']:
            print(f"{TOOL} - invalid `type` value")

        elif args.type not in ['intersects', 'contains', 'within', 'touches', 'crosses', 'overlaps']:
            print(f"{TOOL} - invalid `type` value")

        else:
            result = spatial_join(args.left, args.right, args.output, args.type, args.relationship)
            print(result)
