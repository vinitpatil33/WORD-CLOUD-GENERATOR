import os
import requests

# -------------------------
# Helper function to download files
# -------------------------
def download_file(url, path):
    if not os.path.exists(path):
        print(f"Downloading {os.path.basename(path)} ...")
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
        else:
            print(f"Failed to download: {url}")
    else:
        print(f"Already exists: {path}")

# -------------------------
# Create folder structure
# -------------------------
folders = [
    "assets/masks",
    "assets/fonts",
    "assets/backgrounds",
    "generated"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# -------------------------
# Files to download
# -------------------------

# 🎭 Masks
mask_urls = {
    "heart.png": "https://raw.githubusercontent.com/amueller/word_cloud/master/examples/masks/heart.png",
    "star.png": "https://raw.githubusercontent.com/amueller/word_cloud/master/examples/masks/star.png",
    "cloud.png": "https://raw.githubusercontent.com/amueller/word_cloud/master/examples/masks/cloud.png",
}

# ✍️ Fonts (Google Fonts TTF)
font_urls = {
    "lobster.ttf": "https://github.com/google/fonts/raw/main/ofl/lobster/Lobster-Regular.ttf",
    "pacifico.ttf": "https://github.com/google/fonts/raw/main/ofl/pacifico/Pacifico-Regular.ttf",
}

# 🌅 Backgrounds
bg_urls = {
    "gradient.png": "https://raw.githubusercontent.com/ghosh/uiGradients/master/gradients.json",  # placeholder JSON, you can replace
}

# -------------------------
# Download everything
# -------------------------
for name, url in mask_urls.items():
    download_file(url, f"assets/masks/{name}")

for name, url in font_urls.items():
    download_file(url, f"assets/fonts/{name}")

for name, url in bg_urls.items():
    download_file(url, f"assets/backgrounds/{name}")

print("\n✅ Assets setup complete! Your assets/ folder is ready.")
