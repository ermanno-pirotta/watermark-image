from PIL import Image, ImageDraw, ImageFont


def add_watermark(input_file ,output_file, text, color, position):
    watermarked_image = add_text_to_image(input_file, text, position, color)
    watermarked_image.save(output_file, 'PNG')

def add_text_to_image(output_file, text, position, color):
    image = Image.open(output_file).convert('RGBA')
    imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(imageWatermark)

    width, height = image.size
    margin = 10
    font = ImageFont.truetype('fonts/Norican-Regular.ttf', int(height / 15))
    textWidth, textHeight = draw.textsize(text, font)

    if position == 'right_bottom_corner':
        x = width - textWidth - margin
        y = height - textHeight - margin
    elif position == 'right_top_corner':
        x = width - textWidth - margin
        y = margin
    elif position == 'left_bottom_corner':
        x = margin
        y = height - textHeight - margin
    elif position == 'left_top_corner':
        x = margin
        y = margin
    elif position == 'center':
        x = (width / 2) - (textWidth / 2)
        y = (height / 2) - (textHeight / 2)

    draw.text((x, y), text,font=font , fill=color)

    return Image.alpha_composite(image, imageWatermark)
