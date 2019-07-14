from imutils import paths
import numpy as np
import imutils
import pickle
import cv2
import os

# Initialize lists of extracted faces
extractionList = []
# Initialize list of Names
nameList = []
# Initialize count for face processing
count = 0

# Initialize the image face extraction
print("[+] Loading face extractor")
# Path to the .prototxt file with text description of the network architecture.
proto = os.path.sep.join(["face_detection_model", "deploy.prototxt"])
# Path to the .caffemodel file with learned network.
model = os.path.sep.join(["face_detection_model",
	"res10_300x300_ssd_iter_140000.caffemodel"])
# Read the Deep Neural Network from the Caffe and Proto
faceExtract = cv2.dnn.readNetFromCaffe(proto, model)

# Load in the OpenFace Torch Net for the Deep Neural Network
print("[+] loading face Detection")
# Use the pre-trained OpenFace torch file for face detection
faceDetect = cv2.dnn.readNetFromTorch("nn4.small2.v1.t7")

# Create a list of all test data
print("[+] Finding Test Data")
imageDataset = list(paths.list_images("TrainingData"))

# loop over the image paths
for (i, imagePath) in enumerate(imageDataset):
	# extract the person name from the image path and print the image process
	print("[+] processing image {}/{}".format(i + 1,
		len(imageDataset)))
	# Use split to pull the Array name data
	name = imagePath.split(os.path.sep)[-2]

	# load the image, resize it to have a width of 600 pixels (while
	# maintaining the aspect ratio), and then grab the image
	# dimensions
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=600)
	(height, width) = image.shape[:2]

	# construct a blob from the image
	imageBlob = cv2.dnn.blobFromImage(
		cv2.resize(image, (300, 300)), 1.0, (300, 300),
		(104.0, 177.0, 123.0), swapRB=False, crop=False)

	# apply OpenCV's deep learning-based face faceExtract to localize
	# faces in the input image
	faceExtract.setInput(imageBlob)
	detections = faceExtract.forward()

	# ensure at least one face was found
	if len(detections) > 0:
		# we're making the assumption that each image has only ONE
		# face, so find the bounding box with the largest probability
		i = np.argmax(detections[0, 0, :, 2])
		confidence = detections[0, 0, i, 2]

		# Filter out weak detection
		if confidence > 0.5:
			# calculate the coordinates of the face box
			rectangle = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
			(startX, startY, endX, endY) = rectangle.astype("int")

			# extract the face ROI and grab the ROI dimensions
			face = image[startY:endY, startX:endX]
			(faceHeight, faceWidth) = face.shape[:2]

			# ensure the face width and height are sufficiently large
			if faceWidth < 20 or faceHeight < 20:
				continue

			# construct a blob for the face ROI, then pass the blob
			# through our face embedding model to obtain the 128-d
			# quantification of the face
			faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
				(96, 96), (0, 0, 0), swapRB=True, crop=False)
			faceDetect.setInput(faceBlob)
			vec = faceDetect.forward()

			# add the name of the person + corresponding face
			# embedding to their respective lists
			nameList.append(name)
			extractionList.append(vec.flatten())
			count += 1

# Output the Names and Face Extractions to the pickle file
print("[+] Dumping Pickle Data".format(count))
data = {"embeddings": extractionList, "names": nameList}
f = open("PickleFiles/extraction.pickle", "wb")
f.write(pickle.dumps(data))
f.close()
