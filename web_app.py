import streamlit as st
import os
from PIL import Image

st.title("🖼️ Comic Strip Viewer")

comic_dir = "output"
comic_files = sorted([f for f in os.listdir(comic_dir) if f.endswith(".png")])

if not comic_files:
    st.warning("No comic strips found. Run `main.py` to generate them.")
else:
    selected = st.selectbox("Select a comic to view:", comic_files)
    image_path = os.path.join(comic_dir, selected)
    img = Image.open(image_path)
    st.image(img, caption=selected, use_column_width=True)

st.markdown("---")
if os.path.exists("output/comics.pdf"):
    with open("output/comics.pdf", "rb") as f:
        st.download_button("📥 Download All Comics (PDF)", f, file_name="comics.pdf")