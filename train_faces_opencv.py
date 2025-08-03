import cv2
import os
import numpy as np
import pickle

def extract_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return cv2.normalize(hist, hist).flatten()

features = []
labels = []

for person in os.listdir("dataset"):
    person_folder = os.path.join("dataset", person)
    for img_file in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_file)
        img = cv2.imread(img_path, 0)
        hist = extract_histogram(img)
        features.append(hist)
        labels.append(person)

with open("features.pkl", "wb") as f:
    pickle.dump((features, labels), f)

print("[INFO] Features extracted and saved.")
