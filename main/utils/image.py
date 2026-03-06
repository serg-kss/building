from PIL import Image


def compress_image(path, max_size=(1920, 1080), quality=75):
    img = Image.open(path)

    img.thumbnail(max_size)

    img.save(path, optimize=True, quality=quality)