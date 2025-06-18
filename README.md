# Comic Generator

A Python project that generates comic strips from story prompts using AI-powered image generation and comic panel layout logic.
![Web Preview](https://github.com/user-attachments/assets/e2f95375-46ec-4ae7-ad57-c7f87681b13c)

---

## Features

### Core Capabilities
- **Story Processing**
  - Parses text prompts
  - Breaks story into scenes
  - Maintains character consistency
  - Extracts simple dialog

- **Comic Generation**
  - Generates 4-panel comic strips
  - AI-generated images
  - Speech bubble placement
  - Clean panel layout

- **Style Options**
  - Choose between art styles
  - Set color schemes
  - Use different fonts and panel arrangements

### Bonus
- Character library support
- Sound effect text support
- Web comic viewer

---

## Requirements

- Python 3.8+
- Libraries:
  - `diffusers`
  - `transformers`
  - `torch`
  - `nltk`
  - `Pillow`
  - `streamlit`

Install all dependencies with:

```bash
pip install -r requirements.txt
```

Also download NLTK tokensizer:

```bash
import nltk
nltk.download('punkt')
```

---

### Project Structure

comic_generator/

├── main.py                # Main runner

├── image_generator.py     # Image generation logic

├── layout_engine.py       # Panel layout logic

├── story_processor.py     # Scene/dialog extraction

├── web_viewer.py          # Web preview tool

├── data/
│   ├── prompts.txt        # Input stories

│   └── output/            # Comic outputs

├── .gitignore

├── requirements.txt

└── README.md

---

### Usage

1. Add Prompts
  - Add stories(one per line) in data/prompts.txt. Each should be in 3-5 sentences.
2. Run Comic Generator

```bash
python main.py
```
  - Each line in prompts.txt becomes a 4-panel comic in data/output/ 

3. Run Web Viewer

```bash
streamlit run web_app.py
```
  - Then open http://localhost:5000 in your browser.

### Sample Prompts
- Tom sees a strange light in the sky. He calls Liza to check. They find a UFO landed nearby. An alien waves hello.
- Lily finds a time machine in her garage. She tests it. She ends up in the future. Robots greet her with a party.
- A dog finds a magical bone. It grants him superpowers. He saves the city. The mayor gives him a medal.
- Max and Zoe enter a haunted house. They hear whispers. A friendly ghost guides them out. They thank the ghost.
- Nina opens an old book. A dragon flies out! She calms it down. They become friends. She rides it through the clouds.
- Leo finds a mysterious watch. It freezes time. He plays harmless pranks. But then he returns everything to normal.

### Deliverables
- Comic generator scripts
- 10+ sample comics
- Style guide options (fonts/colors)
- Character consistency demonstration
- Web viewer

### Evaluation Criteria
| Criteria              | Weight |
| --------------------- | ------ |
| Visual Quality        | 40%    |
| Story Coherence       | 25%    |
| Character Consistency | 20%    |
| Creativity            | 15%    |
