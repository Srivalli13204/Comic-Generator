import os
from story_processor import get_stories
from comic_maker import make_comic
from PIL import Image

os.makedirs("output", exist_ok=True)

def main():
    stories = get_stories("data/prompts.txt")
    comic_paths = []

    for i, story in enumerate(stories, 1):
        out_path = f"output/comic_{i}.png"
        print(f"Generating Comic {i}...")
        make_comic(story, out_path)
        comic_paths.append(out_path)

    # Combine into PDF
    images = [Image.open(p).convert("RGB") for p in comic_paths]
    images[0].save("output/comics.pdf", save_all=True, append_images=images[1:])

if __name__ == "__main__":
    main()