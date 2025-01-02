
# Dominant Color Palette Generator

This Streamlit application allows you to upload an image and extract its dominant color palette using the **K-Means clustering algorithm**. The application displays the dominant colors along with their RGB values and a color picker for visualization.

## Features
1. **Image Upload**: Users can upload images in `.jpg`, `.jpeg`, or `.png` formats.
2. **Dominant Color Extraction**: Extracts up to 5 dominant colors from the uploaded image using K-Means clustering.
3. **Color Palette Display**: Shows the dominant colors as RGB values and provides a color picker for each color.

## How It Works
1. **Image Preprocessing**: Resizes the uploaded image to 150x150 pixels for faster processing.
2. **Color Clustering**: Flattens the image data and applies the K-Means algorithm to group pixels into 5 clusters.
3. **Dominant Colors**: The cluster centers represent the dominant colors in the image.

## Requirements
- **Python 3.x**
- **Streamlit**: For building the interactive web app.
- **Pillow**: For image processing.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For the K-Means clustering algorithm.

## How to Run
1. Install the required dependencies:
   ```bash
   pip install streamlit pillow numpy scikit-learn
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Upload an image through the file uploader.
2. Wait for the application to process and generate the dominant color palette.
3. View the dominant colors with their RGB values and use the color picker for visualization.

## Example
- **Uploaded Image**: Displays the uploaded image.
- **Dominant Colors**: Displays up to 5 dominant colors, their RGB values, and a color picker for each color.

## Code Overview
### Main Functions
#### `get_dominant_colors(image, n_colors)`
- Resizes the image to 150x150 pixels.
- Converts the image into an array of RGB values.
- Applies the K-Means algorithm to extract `n_colors` dominant colors.
- Returns the RGB values of the dominant colors.

### Streamlit Interface
1. **Title and Instructions**: Guides users to upload an image.
2. **Image Upload**: Allows the user to select an image file.
3. **Color Palette Display**: Generates and displays the dominant colors with an interactive color picker.

## Notes
- The image is resized to optimize performance and speed up clustering.
- Extracted colors are approximate due to resizing and clustering.

## License
This project is provided for educational purposes.  
**© 2025 Nefrit Mahardika. All rights reserved.**
