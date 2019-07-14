from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle

# load the face embeddings
print("[+] Loading extracted faces")
data = pickle.loads(open("PickleFiles/extraction.pickle", "rb").read())

# encode the labels
print("[+] Adding names to face detection labels")
nameLabel = LabelEncoder()
labels = nameLabel.fit_transform(data["names"])

# train the model used to accept the 128-d embeddings of the face and
# then produce the actual face recognition
print("[+] Training Bob's eyes")
detection = SVC(C=1.0, kernel="linear", probability=True)
detection.fit(data["embeddings"], labels)

# write the actual face recognition to pickle file
file = open("PickleFiles/faceDetection.pickle", "wb")
file.write(pickle.dumps(detection))
file.close()

# Write the name labels to pickle file
file = open("PickleFiles/namedLabels.pickle", "wb")
file.write(pickle.dumps(nameLabel))
file.close()
