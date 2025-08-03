# Automated Attendance System using OpenCV

This project implements an automated attendance system using face recognition with OpenCV. It captures face images using your webcam, trains a recognition model using those images, and then recognizes and marks attendance of individuals in real-time.

All attendance records are saved in a CSV file with the current date in the `/attendance/` folder.

---

## How to Run the Project

### 0. (Optional but Recommended) Create and Activate a Virtual Environment

Using a virtual environment helps you manage project-specific dependencies cleanly.

#### 🔹 Create a virtual environment:

```bash
python -m venv venv
```

#### 🔹 Activate it:

- On **Windows**:
```bash
venv\Scripts\activate
```

- On **macOS/Linux**:
```bash
source venv/bin/activate
```

When activated, your terminal should show something like: `(venv)` at the beginning.

---

### 1. Install All Required Dependencies

Make sure you are in the project directory and run:

```bash
pip install -r requirements.txt
```

This installs the following libraries used in the project:

- **opencv-python** – used to access your webcam, capture video frames, detect and recognize faces using Haar cascades.
- **numpy** – used for matrix and image array operations, like calculating histogram features.
- **pickle** – used to store and load known face features and names after training.
- **csv** – used to write attendance data to a CSV file.
- **os, datetime** – used for file handling and tracking the current date.

---

### 2. Capture Face Images

To register a new user, run:

```bash
python capture_faces_opencv.py
```

- Enter your name when prompted.
- The webcam will open and capture multiple images of your face.
- The images will be stored in the `/dataset/<your_name>/` directory.

---

### 3. Train the Face Recognition System

After you’ve collected images for all users, run the following to train the model:

```bash
python train_faces_opencv.py
```

- This script reads all face images from the `/dataset/` folder.
- It extracts features (histogram of grayscale values) from each face.
- The features and corresponding names are saved to a file called `features.pkl`.

---

### 4. Recognize Faces and Mark Attendance

To detect faces in real-time and mark attendance:

```bash
python recognize_faces_opencv.py
```

- The webcam will open.
- If a known face is detected, the person's name and timestamp will be recorded in a CSV file in `/attendance/<today's-date>.csv`.
- Duplicate entries for the same person on the same day are avoided.

---

## Project Structure

```
automated_attendance_opencv/
│
├── capture_faces_opencv.py       # Script to capture face images and save to dataset
├── train_faces_opencv.py         # Script to extract face features and save them for training
├── recognize_faces_opencv.py     # Script to detect and recognize faces in real-time and mark attendance
├── utils.py                      # Contains helper functions like mark_attendance()
├── features.pkl                  # Stored face encodings and names (generated after training)
├── haarcascade_frontalface_default.xml  # Haar Cascade face detector
├── requirements.txt              # List of required Python libraries
│
├── dataset/                      # Folder to store face images organized by name
│   └── <name>/                   # Each user's face images
│
├── attendance/                   # Folder where attendance CSV files are stored by date
│   └── YYYY-MM-DD.csv            # Auto-generated daily attendance logs
```
