import cv2

def facialThread():
    # To capture video from webcam.
    cap = cv2.VideoCapture(0)

    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')

    while True:

        # Load the cascade
        face_cascade = cv2.CascadeClassifier('/home/manualman/github/Project-Bob/FacialRecognition/haarcascade_frontalface_tree.xml')

        # Read the frame
        _, frame = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display
        cv2.imshow('frame', frame)

        # Stop if escape key is pressed
        escape = cv2.waitKey(30) & 0xff
        if escape == 27:
            break

    # Release the VideoCapture object
    cap.release()
