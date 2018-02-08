# watermark-image
Python script that adds a watermark text to an image

## Dependencies
- python 3
- PIL

## Usage

python watermark_image.py -i <INPUT_IMG> -o <OUTPUT_IMG> -p "<POSITION>" -t "<TEXT>" -c "<COLOR>"

The available positions are:
- left_top_corner
- left_bottom_corner
- right_top_corner
- right_bottom_corner
- center

## Examples

Watermark in the top left corner

![Alt text](examples/left_top.jpg?raw=true "Watermark in the top left corner")

Watermark in the top right corner

![Alt text](examples/right_top.jpg?raw=true "Watermark in the top right corner")

Watermark in the bottom left corner

![Alt text](examples/left_bottom.jpg?raw=true "Watermark in the bottom left corner")

Watermark in the bottom right corner

![Alt text](examples/right_bottom.jpg?raw=true "Watermark in the bottom right corner")

Watermark in the center

![Alt text](examples/center.jpg?raw=true "Watermark in the center")
