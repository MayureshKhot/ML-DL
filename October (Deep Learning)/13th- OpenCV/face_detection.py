import numpy as np
import cv2

#Load the Haar Cascade for frontface detection (from the the github)
face_classifier = cv2.CascadeClassifier(r"Path")
#load the image
image = cv2.imread(r"Path")

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found")
    exit()
    
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #checkout geeksforgeeks
faces = face_classifier.detectMultiScale(gray, 1.3,5) # for detecting multpile images

if len(faces)==0:
    print("no")
else:
    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y) (x+w, y+h), (127, 0, 255), 2)

    # Display the output image
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)  # Wait for a key press to close the window

# Close all OpenCV windows
cv2.destroyAllWindows()