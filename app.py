import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests
from bs4 import BeautifulSoup
import io

st.set_page_config(page_title="Creative WordCloud Generator", page_icon="🌈", layout="wide")

st.title("🌈 Creative WordCloud Generator")
st.write("Generate stylish word clouds from **text or topics** with shapes, colors, and fonts — all free!")

# --- Input mode ---
mode = st.radio("Choose Input Mode:", ["Text", "Topic (Wikipedia)"])

if mode == "Text":
    text = st.text_area("Paste your text here:", height=200)
else:
    topic = st.text_input("Enter a topic (e.g. Artificial Intelligence):")
    text = ""
    if topic:
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            text = " ".join(p.get_text() for p in soup.find_all("p"))
            st.success(f"Fetched text from Wikipedia for '{topic}' ✅")
        except:
            st.error("Could not fetch data. Try another topic.")

# --- Upload mask (optional shape) ---
mask_file = st.file_uploader("Upload a PNG/JPG mask for custom shape (optional):", type=["png","jpg","jpeg"])
mask = None
if mask_file:
    mask = np.array(Image.open(mask_file))

# --- Settings ---
col1, col2 = st.columns(2)
with col1:
    bg_color = st.color_picker("Background Color", "#000000")
    contour_color = st.color_picker("Contour Color", "#FF0000")
with col2:
    colormap = st.selectbox("Color Map", ["viridis","plasma","magma","cool","coolwarm","inferno"])
    max_words = st.slider("Max Words", 50, 500, 200)

# --- Generate Button ---
if st.button("✨ Generate WordCloud"):
    if text.strip() == "":
        st.warning("Please enter text or topic first.")
    else:
        stopwords = set(STOPWORDS)
        wc = WordCloud(
            background_color=bg_color,
            mask=mask,
            stopwords=stopwords,
            contour_width=2,
            contour_color=contour_color,
            colormap=colormap,
            max_words=max_words
        )
        wc.generate(text)

        # Display
        fig, ax = plt.subplots(figsize=(10,10))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

        # Download
        buf = io.BytesIO()
        wc.to_file("wordcloud.png")
        st.download_button("⬇️ Download WordCloud", data=open("wordcloud.png","rb"), file_name="wordcloud.png", mime="image/png")
