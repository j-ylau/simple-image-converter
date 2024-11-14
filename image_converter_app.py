import streamlit as st
from PIL import Image
from pillow_heif import register_heif_opener
import os
import shutil

# Register HEIF support with Pillow
register_heif_opener()

# Directories for inputs and outputs
input_dir = "input"
output_dir = "output"
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Helper function to convert images
def convert_image_to_jpg(input_path, output_path):
    try:
        with Image.open(input_path) as image:
            image = image.convert("RGB")
            image.save(output_path, "JPEG")
        return output_path
    except Exception as e:
        st.error(f"Error converting {input_path}: {e}")
        return None

# Clear input and output folders
def clear_directories():
    if os.path.exists(input_dir):
        shutil.rmtree(input_dir)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

# Streamlit UI
st.title("Simple Image to JPG Converter")
st.write("Upload images in any format (e.g., HEIC, DNG, PNG, BMP, TIFF) to convert them to JPG.")

# Button to clear temporary files and reset the app
if st.button("Clear Temporary Files and Reset"):
    clear_directories()
    st.experimental_rerun()  # Reset the app to its initial state

# Upload images
uploaded_files = st.file_uploader("Upload images", type=["heic", "dng", "png", "bmp", "tiff", "jpeg", "jpg"], accept_multiple_files=True)

# Processing and downloading only if files are uploaded
if uploaded_files:
    # Displaying progress
    total_files = len(uploaded_files)
    progress_bar = st.progress(0)
    
    # User feedback message
    st.info(f"Converting {total_files} images. Please wait...")

    converted_files = []
    for i, uploaded_file in enumerate(uploaded_files):
        # Define input and output paths
        input_path = os.path.join(input_dir, uploaded_file.name)
        output_path = os.path.join(output_dir, f"{os.path.splitext(uploaded_file.name)[0]}.jpg")
        
        # Save uploaded file to input directory
        with open(input_path, "wb") as f:
            f.write(uploaded_file.read())
        
        # Convert the image to JPG
        converted_path = convert_image_to_jpg(input_path, output_path)
        if converted_path:
            converted_files.append(converted_path)

        # Update progress bar
        progress_bar.progress((i + 1) / total_files)

    # Notify user that conversion is complete
    st.success("All images have been converted and saved to the `/output` directory.")
    
    # Display download section at the top
    st.write("### Download All Converted Images")
    zip_path = "converted_images.zip"
    shutil.make_archive("converted_images", 'zip', output_dir)

    # Allow user to download ZIP without resetting the app
    with open(zip_path, "rb") as file:
        st.download_button(
            label="Download All as ZIP",
            data=file,
            file_name="converted_images.zip",
            mime="application/zip"
        )
    
    # Notify the user that the ZIP file is ready
    st.balloons()
    st.info("Your images are ready! Download the ZIP file with all converted images.")
else:
    # Initial instructions for first-time use
    st.info("Please upload images to start the conversion process.")

    # Explanation message for Clear button when no files are uploaded
    st.write("To reset the app or clear any temporary files, click the 'Clear Temporary Files and Reset' button above.")
