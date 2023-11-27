import cv2
import os
import Image_generator
from processor import process_image, display_image, save_image

def main():
    # Generate image
    image_name = "Image.jpg"
    url = 'https://img.freepik.com/free-photo/coffee-cup-on-ground-coffee-close-up_1220-6147.jpg'
    Image_generator.generate_image(url, image_name)

    # Process the image
    image = process_image(image_name)

    # Call the function to display the image
    display_image(image)

    # Call function to save image locally
    folder_name = "Processed"
    file_name = "Processed_Image.jpg"
    save_image(image, folder_name, file_name)

    # Remove the original image
    os.remove(image_name)

if __name__ == "__main__":
    main()
