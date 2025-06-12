# ==================================================
# main.py — Wallpaper Generator (CTk Version)
# ==================================================
import tempfile
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from tkinter import colorchooser
import os
import screeninfo
import random
import ast

# --------------------------------------
# Initial config
# --------------------------------------
source_dir = None
DEFAULT_COLUMNS = 7
DEFAULT_BG_COLOR = "#000000"
MARGIN = 10

# --------------------------------------
# Import utility functions
# --------------------------------------
from utils import (
    estimate_needed_images,
    correct_image_orientation,
    set_wallpaper
)


# --------------------------------------
# Choose the color from a selector
# --------------------------------------
def choose_color():
    color = colorchooser.askcolor(title="Choose background color")
    if color[1]:
        entry_color.delete(0, "end")
        entry_color.insert(0, color[1])

# --------------------------------------
# Generate wallpaper collage
# --------------------------------------
def generate_collage():
    global source_dir

    try:
        columns = int(entry_columns.get())
    except ValueError:
        status_label.configure(text="Invalid number of columns", text_color="red")
        return

    color_value = entry_color.get()
    try:
        # If the input is a tuple like "(255,255,255)", it will be converted
        bg_color = ast.literal_eval(color_value) if color_value.startswith("(") else color_value
    except:
        status_label.configure(text="Invalid color format", text_color="red")
        return
    
    # --- Get screen resolution ---
    screen = screeninfo.get_monitors()[0]
    screen_width = screen.width
    screen_height = screen.height

    needed_image_count = estimate_needed_images(screen_width, screen_height, columns, MARGIN)

    image_paths = [
        os.path.join(source_dir, f)
        for f in os.listdir(source_dir)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ]

    random.shuffle(image_paths)
    image_paths = image_paths[:needed_image_count]

    column_width = (screen_width - (columns + 1) * MARGIN) // columns
    resized_images = []

    for path in image_paths:
        img = Image.open(path)
        img = correct_image_orientation(img)
        img = img.convert("RGB")
        scale = column_width / img.width
        new_height = int(img.height * scale)
        resized = img.resize((column_width, new_height), Image.LANCZOS)
        resized_images.append(resized)

    column_heights = [MARGIN] * columns
    columns_images = [[] for _ in range(columns)]

    for img in resized_images:
        min_col_index = column_heights.index(min(column_heights))
        columns_images[min_col_index].append(img)
        column_heights[min_col_index] += img.height + MARGIN

    final_height = max(column_heights)
    final_image = Image.new("RGB", (screen_width, final_height), bg_color)

    for col_index, images in enumerate(columns_images):
        x = MARGIN + col_index * (column_width + MARGIN)
        y = MARGIN
        for img in images:
            final_image.paste(img, (x, y))
            y += img.height + MARGIN

    cropped = final_image.crop((0, 0, screen_width, screen_height))
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bmp") as temp_file:
        temp_path = temp_file.name
        cropped.save(temp_path, "BMP")  # Windows needs BMP format for wallpaper
    set_wallpaper(temp_path)

    status_label.configure(text="Wallpaper created.", text_color="green")

# --------------------------------------
# Select folder dialog
# --------------------------------------
def select_folder():
    global source_dir
    folder = filedialog.askdirectory()
    if folder:
        source_dir = folder
        folder_label.configure(text=folder)
        generate_button.configure(state="normal")
        status_label.configure(text="")

# --------------------------------------
# CTk Interface
# --------------------------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Wallpaper Collage Generator")
app.geometry("600x320")

select_button = ctk.CTkButton(app, text="Choose Folder", command=select_folder)
select_button.pack(pady=(20, 10))

folder_label = ctk.CTkLabel(app, text="No folder selected", wraplength=550)
folder_label.pack()

entry_columns = ctk.CTkEntry(app, placeholder_text="Number of columns", width=200)
entry_columns.insert(0, str(DEFAULT_COLUMNS))
entry_columns.pack(pady=(10, 5))

entry_color = ctk.CTkEntry(app, placeholder_text="Background color (hex or RGB)", width=300)
#entry_color.insert(0, default_bg_color)
#entry_color.pack(pady=(5, 5))

choose_color_button = ctk.CTkButton(app, text="Choose Color", command=choose_color)
choose_color_button.pack(pady=(5, 15))

generate_button = ctk.CTkButton(app, text="Generate Wallpaper", command=generate_collage, state="disabled")
generate_button.pack()

status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=(10, 5))

app.mainloop()


