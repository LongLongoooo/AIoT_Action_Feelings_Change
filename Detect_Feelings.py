import time
print("Hallo AI")
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model(r"keras_model.h5", compile=False)

# Load the labels
class_names = open(r"labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)
#camera = cv2.VideoCapture("http://192.168.1.6:4747/video")

def image_detector():
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Detection Webcam", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    image_detector.Class_name1 = class_name[2:]
    image_detector.Confidence_Score = str(np.round(confidence_score * 100))[:-2]
    print("Class:", image_detector.Class_name1, end="")
    print("Confidence Score:", image_detector.Confidence_Score, "%")


