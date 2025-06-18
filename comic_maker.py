from image_generator import generate_image
from story_processor import extract_scenes
from utils.layout import add_speech, combine_panels

def make_comic(story, output_path):
    scenes = extract_scenes(story)
    images = []

    for scene in scenes[:4]:
        img = generate_image(scene)
        img = add_speech(img, scene)
        images.append(img)

    comic = combine_panels(images)
    comic.save(output_path)