from imutils.video import VideoStream
import numpy as np
import imutils
import pickle
import time
import cv2
import os

# A silly function that allows a return functionallity within the while True
# video loop.
def loopReturn(name):
	return(name)

#Run the facial detection function
def facialRecognition():

	# Initialize face detection
	print("[+] Initiating video facial detection")
	# Path to the .prototxt file with text description of the network architecture.
	proto = os.path.sep.join(["face_detection_model", "deploy.prototxt"])
	# Path to the .caffemodel file with learned network.
	model = os.path.sep.join(["face_detection_model",
		"res10_300x300_ssd_iter_140000.caffemodel"])
	# Read the Deep Neural Network from the Caffe and Proto
	faceExtract = cv2.dnn.readNetFromCaffe(proto, model)

	# load our serialized face embedding model from disk
	print("[+] loading face Detection")
	# Use the pre-trained OpenFace torch file for face detection
	embedder = cv2.dnn.readNetFromTorch("nn4.small2.v1.t7")

	# Read in the pickle file containing the facial detection data.
	detection = pickle.loads(open("PickleFiles/faceDetection.pickle", "rb").read())
	# Read in the picle file containing the named labels
	nameLabel = pickle.loads(open("PickleFiles/namedLabels.pickle", "rb").read())

	# initialize the video I/O
	print("[+] Initializing video feed")
	video = VideoStream(src=0).start()
	time.sleep(2.0)

	# Begin the video loop
	while True:
		# capture each frame for processing
		videoCapture = video.read()

		# resize the frame to have a width of 600 pixels (while
		# maintaining the aspect ratio), and then grab the image
		# dimensions
		videoCapture = imutils.resize(videoCapture, width=600)
		(height, width) = videoCapture.shape[:2]

		# construct a blob from the image
		imageBlob = cv2.dnn.blobFromImage(
			cv2.resize(videoCapture, (300, 300)), 1.0, (300, 300),
			(104.0, 177.0, 123.0), swapRB=False, crop=False)

		# apply OpenCV's deep learning-based face detector to localize
		# faces in the input image
		faceExtract.setInput(imageBlob)
		faceDetection = faceExtract.forward()

		# loop over the detections
		for i in range(0, faceDetection.shape[2]):
			# Assign probability associated wit the prediction
			confidence = faceDetection[0, 0, i, 2]

			# filter out weak detections
			if confidence > 0.5:
				# calculate the coordinates of the face box
				box = faceDetection[0, 0, i, 3:7] * np.array([width, height, width, height])
				(startX, startY, endX, endY) = box.astype("int")

				# extract the face ROI
				face = videoCapture[startY:endY, startX:endX]
				(faceHeight, faceWidth) = face.shape[:2]

				# ensure the face width and height are sufficiently large
				if faceWidth < 20 or faceHeight < 20:
					continue

				# construct a blob for the face ROI, then pass the blob
				# through our face detction model to obtain the 128-d
				# quantification of the face
				faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
					(96, 96), (0, 0, 0), swapRB=True, crop=False)
				embedder.setInput(faceBlob)
				vec = embedder.forward()

				# perform classification to recognize the face
				prediction = detection.predict_proba(vec)[0]
				x = np.argmax(prediction)
				probability = prediction[x]
				name = nameLabel.classes_[x]
				# Return name detection from running while loop 
				loopReturn(name)
				# Draw the rectangle around the face along with it's probability
				description = "{}: {:.2f}%".format(name, probability * 100)
				y = startY - 10 if startY - 10 > 10 else startY + 10
				cv2.rectangle(videoCapture, (startX, startY), (endX, endY),
					(0, 0, 255), 2)
				cv2.putText(videoCapture, description, (startX, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

		# show the output frame
		cv2.imshow("Frame", videoCapture)

		# if the `ESC` key was pressed, break from the loop
		escape = cv2.waitKey(30) & 0xff
		if escape == 27:
	    		break

	# Cleanup
	cv2.destroyAllWindows()
	video.stop()

facialRecognition()
