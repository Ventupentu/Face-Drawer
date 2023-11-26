import cv2
import numpy as np
import Image_Generator
import os

def draw_face(image, circles):
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        # Draw the eyes (should be half the radius of the circle) (should be green) (should be 50 pixels away from the center of the circle)
        cv2.circle(image, (circles[0][0] - 50, circles[0][1]), 25, (0, 255, 0), -1)
        cv2.circle(image, (circles[0][0] + 50, circles[0][1]), 25, (0, 255, 0), -1)

        # Draw the pupils (should be half the radius of the circle) (should be blue)
        cv2.circle(image, (circles[0][0] - 50, circles[0][1]), 10, (255, 0, 0), -1)
        cv2.circle(image, (circles[0][0] + 50, circles[0][1]), 10, (255, 0, 0), -1)
        
        # Draw the mouth (should be green) (should be 50 pixels away from the center of the circle) (should be 50 pixels long) (should be a semicircle)
        cv2.ellipse(image, (circles[0][0], circles[0][1] + 50), (50, 50), 0, 0, 180, (0, 255, 0), -1)
        
def process_image(image_name):
    # Load the image
    image = cv2.imread(image_name)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply the HoughCircles transform to detect circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.5, 10)

    # Draw the face
    draw_face(image, circles)

    return image

def display_image(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_image(image, folder_name, file_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    cv2.imwrite(file_path, image)


# Generate image
image_name = "Image.jpg"
url = 'https://img.freepik.com/free-photo/coffee-cup-on-ground-coffee-close-up_1220-6147.jpg'
Image_Generator.generate_image(url, image_name)

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