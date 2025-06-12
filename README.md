# Wallpaper Collage Generator

This is a small personal project I built in Python.
The idea was simple: I wanted to take a folder full of images and automatically generate a collage that fits my screen resolution, with the option to apply it directly as my Windows wallpaper.
I gave it a minimal interface using CustomTkinter.

**Note:** This version only works on **Windows**, since setting the wallpaper relies on a Windows-specific API. The project is open-source and you’re welcome to fork, modify, or adapt it for other platforms.

---

## Features

- Simple GUI (thanks to CustomTkinter)
- Detects your screen size automatically
- Lets you pick how many columns the collage should have
- You can choose the background color (either manually or with a visual color picker)
- Images are placed smartly like a masonry grid (Pinterest-style)
- It also handles image orientation based on EXIF metadata
- When the collage is ready, it's applied as your wallpaper instantly

---

## Preview

### Launch the script / the .exe

![Step 1 - Select folder](screenshots/ctk_windows.pn)

### 1. Select a folder with images

![Step 1 - Select folder](screenshots/select-folder.png)

### 2. Pick a background color

![Step 2 - Pick color](screenshots/pick-color.png)

### 3. Generate the collage (example with 3 columns)

![Step 3 - Result](screenshots/wallpaper.png)

---

## How to Use It

### Option 1: Use the executable

If you don't want to deal with Python or installations:

1. Go to the [Releases](https://github.com/asmabnouir/wallpaper-collage-generator/releases/tag/v1.0)
2. Download the latest ZIP file
3. Extract it
4. Run the `.exe` — that’s it!

You’ll get a small interface where you can:

- Select a folder with images
- Choose how many columns you want
- Pick a background color
- Generate and apply the collage as your wallpaper

### Option 2: Run it from source (Python)

If you're a developer or just curious:

```bash
pip install -r requirements.txt
python main.py
```

---

## Project Structure

```
wallpaper-collage-generator/
├── main.py
├── utils.py
├── README.md
├── requirements.txt
├── dist/            # compiled .exe
├── screenshots/     # for visuals in this README
```

## License

This project is released under the MIT License.

---

## Credits

Made with Python, PIL, and CustomTkinter.
Created by asmabnouir.
