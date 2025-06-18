from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cpu")  # Use "cuda" if you have a GPU

def generate_image(prompt):
    result = pipe(prompt).images[0]
    return result