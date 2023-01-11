import cv2 # For image processing

# Load data set (haar cascade algorithm)
trained_face_data =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

'''
# Images to detect faces in
imgDR = cv2.imread('DR.png')
imgRG = cv2.imread('RG.png')
imgEW = cv2.imread('EW.png')
imgMulti = cv2.imread('Faces.jpg')
images = [imgDR, imgRG, imgEW, imgMulti]

# Convert images to grayscale
gsImgDR = cv2.cvtColor(imgDR, cv2.COLOR_BGR2GRAY)
gsImgRG = cv2.cvtColor(imgRG, cv2.COLOR_BGR2GRAY)
gsImgEW = cv2.cvtColor(imgEW, cv2.COLOR_BGR2GRAY)
gsImgMulti = cv2.cvtColor(imgMulti, cv2.COLOR_BGR2GRAY)
gsImages = [gsImgDR, gsImgRG, gsImgEW, gsImgMulti]

# Detect faces
for i in gsImages:
    face_coordinates = trained_face_data.detectMultiScale(i)
    # Draw squares around faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(i, (x, y), (x+w, y+h), (0, 0, 255), 2)
 
# Show image
for i in gsImages:
    cv2.imshow('Face Detector', i)
    cv2.waitKey()
'''

# WEBCAM

# Webcam to detect faces in
webcam = cv2.VideoCapture(0)
'''video file
webcam = cv2.VideoCapture(video.mp4)'''
# Iterate through every frame
while True:
    # Read current frame
    successful_frame_read, frame = webcam.read()
    # Convert to grayscale
    gsFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Show video
    cv2.imshow('Face Detector', gsFrame)
    cv2.waitKey(1)

print("Code Complete")

# TO DO LIST
# Turn into OOP(class and functions)
# Read in files automatically from directry
# Ask users if they want to upload an image/video or use the webcam
# Allow uploading of images/videos which are stored in the directory