import cv2
import os

def capture_faces(name):
    os.makedirs(f"dataset/{name}", exist_ok=True)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)
    count = 0
    capturing = False

    print("[INFO] Press '0' to start capturing. Webcam is on. Press 'q' to quit anytime.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to read from webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            if capturing and count < 20:
                roi = gray[y:y + h, x:x + w]
                roi = cv2.resize(roi, (100, 100))
                cv2.imwrite(f"dataset/{name}/{count}.jpg", roi)
                print(f"[CAPTURED] Image {count+1}/20")
                count += 1

        cv2.imshow("Webcam - Press '0' to Capture | 'q' to Quit", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('0') and not capturing:
            print("[INFO] Starting capture of 20 face images...")
            capturing = True

        if key == ord('q') or (capturing and count >= 20):
            print("[INFO] Exiting webcam.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    user = input("Enter your name: ")
    capture_faces(user)
