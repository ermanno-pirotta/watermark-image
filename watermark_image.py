import argparse
import glob
import re

from img_util import add_watermark

def is_unix_path(path):
    match =re.match(r'.*\*+.*',path)
    if (match):
        return True
    else:
        return False

def build_output_file_name(input_name):
    return input_name + '_with_watermark.png'

def main(args):
    input_path = args.input
    text = args.text
    color = args.color
    position = args.position

    if is_unix_path(input_path):
        print('input recognised as unix path: processing multiple elements')
        for file_name in glob.glob(input_path):
            print('processing file %s' % file_name)
            add_watermark(file_name, build_output_file_name(file_name), text, color, position)
    else:
        add_watermark(input_path, build_output_file_name(input_path), text, color, position)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Watermark image maker')

    parser.add_argument('--input', '-i', default=None, required=True,type=str,
                        help='input file name. Supports single file or multiple file if path is in the form of unix pattern. I.e. ./input_dir/*.jpg')

    parser.add_argument('--text', '-t', default=0, required=True,  type=str,
                        help='Text to write')

    parser.add_argument('--color', '-c', default='#126b6e', required=False,  type=str,
                        help='Text color')

    parser.add_argument('--position', '-p', default='right_bottom_corner', required=False,  type=str,
                        help='Watermark position. One of: left_top_corner | left_bottom_corner, | right_top_corner | right_bottom_corner | center')


    args = parser.parse_args()
    main(args)
