import argparse
from img_util import add_watermark

def main(args):

    output_file =args.output
    input_file = args.input
    text = args.text
    color = args.color
    position = args.position

    add_watermark(input_file, output_file, text, color, position)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Watermark image maker')

    parser.add_argument('--input', '-i', default=None, required=True,type=str,
                        help='input file name')

    parser.add_argument('--output', '-o', default=None, required=True,type=str,
                        help='output file name without extension')

    parser.add_argument('--text', '-t', default=0, required=True,  type=str,
                        help='Text to write')

    parser.add_argument('--color', '-c', default='#126b6e', required=False,  type=str,
                        help='Text color')

    parser.add_argument('--position', '-p', default='right_bottom_corner', required=False,  type=str,
                        help='Watermark position. One of: left_top_corner | left_bottom_corner, | right_top_corner | right_bottom_corner | center')


    args = parser.parse_args()
    main(args)
