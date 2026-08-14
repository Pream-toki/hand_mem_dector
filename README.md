# 🤚 Hand Gesture Meme Detector

A Python computer-vision project that uses your webcam to detect hand gestures in real time and display a random meme for the detected gesture.

The project uses **OpenCV** for webcam processing and **MediaPipe Hand Landmarker** for hand landmark detection.

## ✨ Features

- Real-time webcam hand detection
- MediaPipe hand landmark detection
- Rule-based gesture recognition
- Random meme selection for supported gestures
- Automatically removes the meme when no hand is detected
- Project-relative meme folders, so the code does not depend on your personal computer path

## 🤚 Supported Gestures

| Gesture | Meaning |
|---|---|
| ✊ FIST | Closed hand |
| ☝️ POINTING | Index finger extended |
| ✌️ PEACE | Index and middle fingers extended |
| ✋ OPEN HAND | Four fingers extended |
| 👍 THUMBS UP | Thumb extended upward |
| ❓ OTHER | Gesture does not match a supported pattern |

## 🛠️ Technologies

- Python
- OpenCV
- MediaPipe
- Computer Vision

## 📁 Project Structure

```text
hand_mem_dector/
│
├── fist/          # Meme images for FIST
├── open_hand/     # Meme images for OPEN HAND
├── peace/         # Meme images for PEACE
├── pointing/      # Meme images for POINTING
├── thumbs_up/     # Meme images for THUMBS UP
│
├── gesture.py     # Gesture recognition rules
├── hand_dector.py # Webcam and MediaPipe processing
├── meme.py        # Random meme selection
├── hand_landmarker.task
└── README.md
```

## 💻 Requirements

- Python 3.9 or newer
- A working webcam
- OpenCV
- MediaPipe
- The MediaPipe `hand_landmarker.task` model file

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pream-toki/hand_mem_dector.git
cd hand_mem_dector
```

### 2. Create a virtual environment (recommended)

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install opencv-python mediapipe
```

## ▶️ Run the Project

Make sure `hand_landmarker.task` is in the project directory, then run:

```bash
python hand_dector.py
```

A webcam window will open. Show a supported hand gesture to the camera.

Press **Q** or **Esc** to quit.

## 🧠 How It Works

```text
Webcam
   ↓
OpenCV captures a frame
   ↓
MediaPipe detects hand landmarks
   ↓
gesture.py checks landmark positions
   ↓
A gesture is identified
   ↓
meme.py finds a random image
   ↓
The meme is displayed
```

The gesture classifier in `gesture.py` uses landmark positions rather than a custom trained machine-learning model. For example, it compares the positions of finger joints to determine whether fingers are extended.

## 🖼️ Adding Your Own Memes

Put `.jpg`, `.jpeg`, or `.png` images inside the matching gesture folder.

Example:

```text
peace/
├── meme1.jpg
├── meme2.png
└── meme3.jpg
```

When the PEACE gesture is detected, one of the images in `peace/` is selected randomly.

Make sure the folder name matches the gesture after converting it to lowercase and replacing spaces with underscores.

For example:

```text
OPEN HAND  →  open_hand/
THUMBS UP  →  thumbs_up/
```

## 🔧 Customizing Gestures

The gesture rules are in `gesture.py`.

You can modify the conditions or add new gesture patterns using MediaPipe's hand landmarks.

Possible future gestures include:

- 🤟 I Love You
- 🤙 Call Me
- 👌 OK
- 🤘 Rock

## 🐛 Troubleshooting

### Webcam does not open

Make sure your webcam is connected and is not being used by another application.

### `ModuleNotFoundError`

Install the dependencies again:

```bash
pip install opencv-python mediapipe
```

### `hand_landmarker.task` not found

Make sure the model file is located in the same project directory as `hand_dector.py`.

### `Folder not found`

Make sure the required meme folder exists and uses the correct name, such as `peace`, `open_hand`, or `thumbs_up`.

### No meme appears

Make sure the corresponding folder contains at least one `.jpg`, `.jpeg`, or `.png` image.

## ⚠️ Current Limitations

- The project currently processes one hand.
- Lighting and camera angle can affect detection.
- Some gestures may be classified as `OTHER`.
- Gesture recognition uses hand-landmark rules rather than a trained custom classifier.
- The model file must be present locally.

## 🔮 Future Improvements

- [ ] Add more gestures
- [ ] Improve gesture accuracy
- [ ] Support multiple hands
- [ ] Add a graphical user interface
- [ ] Add gesture confidence information
- [ ] Add automated dependency management with `requirements.txt`
- [ ] Rename `hand_dector.py` to `hand_detector.py`
- [ ] Add screenshots or a demo GIF

## 📚 What This Project Demonstrates

This project demonstrates practical experience with:

- Python programming
- OpenCV
- MediaPipe
- Computer vision
- Webcam processing
- Hand landmark detection
- Rule-based gesture recognition
- File and folder handling
- Git and GitHub

## 👨‍💻 Author

**Pream-toki**

GitHub: https://github.com/Pream-toki

## 📄 License

No open-source license has been specified yet.
