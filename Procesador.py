import cv2
import numpy as np
import Generador_de_imagen
#Generate image
nombre_imagen="Imagen.jpg"
url='https://www.ikea.com/es/es/images/products/bravur-reloj-pared-baja-tension-negro__0633568_pe695902_s5.jpg' #The url of the jpg you want
Generador_de_imagen.generar_imagen(url,nombre_imagen)

# Load the image
image = cv2.imread(nombre_imagen)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply the HoughCircles transform to detect circles
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.5, 10)


# If circles are found, draw a happy face inside one of them
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    #Draw the eyes(has to be half of the radius of the circle)(has to be green)(has to be 50 pixels away from the center of the circle)
    cv2.circle(image, (circles[0][0] - 50, circles[0][1]), 25, (0, 255, 0), -1)
    cv2.circle(image, (circles[0][0] + 50, circles[0][1]), 25, (0, 255, 0), -1)

    #Draw the pupils(has to be half of the radius of the circle)(has to be Blue)
    cv2.circle(image, (circles[0][0] - 50, circles[0][1]), 10, (255, 0, 0), -1)
    cv2.circle(image, (circles[0][0] + 50, circles[0][1]), 10, (255, 0, 0), -1)
    
    #Draw the mouth(has to be green)(has to be 50 pixels away from the center of the circle)(has to be 50 pixels long)(Has to be a semicircle)
    cv2.ellipse(image, (circles[0][0], circles[0][1] + 50), (50, 50), 0, 0, 180, (0, 255, 0), -1)


# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
