# Image to JPG Converter

A simple Streamlit app that converts images (HEIC, DNG, PNG, BMP, TIFF, etc.) to JPG format.

## Features

- Upload multiple images in various formats and convert them to JPG.
- Download all converted images as a ZIP file.
- Clear temporary files to reset the app.

## How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Streamlit app**:
   ```bash
   streamlit run image_converter_app.py
   ```

## File Structure

- **input/** - Temporary folder for uploaded images.
- **output/** - Temporary folder for converted JPG images.

## .gitignore

The `.gitignore` file excludes `input/`, `output/`, generated ZIP files, and other temporary files.

## Requirements

- Python 3.x
- Packages in `requirements.txt` (Pillow, Streamlit, pillow-heif)

