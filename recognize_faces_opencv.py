import cv2
import numpy as np
import pickle
from utils import mark_attendance

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

with open("features.pkl", "rb") as f:
    known_features, known_names = pickle.load(f)

def extract_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return cv2.normalize(hist, hist).flatten()

cap = cv2.VideoCapture(0)
detected_names = set()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        roi_resized = cv2.resize(roi, (100, 100))
        hist = extract_histogram(roi_resized)

        matched_name = "Unknown"
        max_corr = -1
        matched_index = -1

        for i, known_hist in enumerate(known_features):
            corr = cv2.compareHist(hist, known_hist, cv2.HISTCMP_CORREL)
            if corr > max_corr:
                max_corr = corr
                matched_index = i

        if max_corr > 0.7:  # threshold for good match
            matched_name = known_names[matched_index]
            if matched_name not in detected_names:
                mark_attendance(matched_name)
                detected_names.add(matched_name)
            print(f"[INFO] Match: {matched_name} with confidence {max_corr:.3f}")
        else:
            print("[INFO] No confident match.")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, matched_name, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Recognition", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
