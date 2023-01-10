import cv2 # For image processing

# Load data set (haar cascade algorithm)
trained_face_data =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Images to detect faces in
imgDR = cv2.imread('DR.png')
imgRG = cv2.imread('RG.png')
imgEW = cv2.imread('EW.png')
images = [imgDR, imgRG, imgEW]

# Convert images to grayscale
gsImgDR = cv2.cvtColor(imgDR, cv2.COLOR_BGR2GRAY)
gsImgRG = cv2.cvtColor(imgRG, cv2.COLOR_BGR2GRAY)
gsImgEW = cv2.cvtColor(imgEW, cv2.COLOR_BGR2GRAY)
gsImages = [gsImgDR, gsImgRG, gsImgEW]

# Detect faces
for i in gsImages:
    face_coordinates = trained_face_data.detectMultiScale(i)
    #print(face_coordinates)
    # Draw squares  around faces
    (x, y, w, h) = face_coordinates[0]
    cv2.rectangle(i, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('Face Detector', i)
    cv2.waitKey()
 
# Show image
for i in images:
    (x, y, w, h) = face_coordinates[0]
    cv2.rectangle(i, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('Face Detector', i)
    cv2.waitKey()


print("Code Complete")