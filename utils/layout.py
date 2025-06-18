from PIL import Image, ImageDraw, ImageFont

def add_speech(img, text):
    img = img.resize((512, 512))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.rectangle([5, 5, 502, 45], fill="white")
    draw.text((10, 10), text, fill="black", font=font)
    return img

def combine_panels(images):
    w, h = 512, 512
    comic = Image.new("RGB", (w*2, h*2), "white")
    positions = [(0, 0), (w, 0), (0, h), (w, h)]
    for img, pos in zip(images, positions):
        comic.paste(img, pos)
    return comic