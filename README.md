# Hand Gesture Meme Detector

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Landmarker-00A67E)](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker/python)

A webcam-powered Python project that recognizes hand gestures in real time and responds with a random meme from the matching gesture folder. It combines OpenCV video capture with MediaPipe hand landmarks and a lightweight, rule-based classifier—no custom model training required.

> **Portfolio snapshot:** real-time computer vision, landmark-based gesture classification, local asset management, and a simple interactive desktop experience.

## Features

- Live webcam capture with mirrored preview
- MediaPipe Hand Landmarker detection for one hand at a time
- Rule-based recognition for five gestures
- Random meme selection whenever the recognized gesture changes
- On-screen landmarks and current gesture label
- Automatic cleanup of the meme window when no hand is detected
- Project-relative asset paths, so the project can run from any working directory

## Supported gestures

| Gesture | Recognition rule | Meme folder |
| --- | --- | --- |
| ✊ FIST | All four fingers folded and thumb not extended | `fist/` |
| ☝️ POINTING | Index finger extended | `pointing/` |
| ✌️ PEACE | Index and middle fingers extended | `peace/` |
| ✋ OPEN HAND | All four fingers extended | `open_hand/` |
| 👍 THUMBS UP | Thumb extended upward; fingers folded | `thumbs_up/` |
| ❓ OTHER | Does not match a supported rule | — |

## Demo and usage

1. Run the application with `python hand_dector.py`.
2. Allow your webcam to open.
3. Hold a supported gesture in view.
4. A random image from its matching folder appears in the **MEME** window.

Press <kbd>Q</kbd> or <kbd>Esc</kbd> to close the application.

## How it works

```text
Webcam frame
    │
    ▼
OpenCV capture + RGB conversion
    │
    ▼
MediaPipe Hand Landmarker
    │
    ▼
gesture.py: landmark-position rules
    │
    ▼
meme.py: choose a random image for the gesture
    │
    ▼
OpenCV windows: camera preview + meme
```

The classifier compares finger-tip and joint positions in MediaPipe's normalized hand landmarks. This makes the project compact and easy to experiment with, while avoiding the overhead of collecting and training a custom dataset.

## Requirements

- Python 3.9 or later
- A webcam available to your operating system
- The MediaPipe model file: `hand_landmarker.task` in the repository root

Python dependencies are listed in [`requirements.txt`](requirements.txt).

## Installation

```bash
git clone --branch hand_mem_dector https://github.com/Pream-toki/hand_mem_dector.git
cd hand_mem_dector

python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Then start the app:

```bash
python hand_dector.py
```

> The entry script is intentionally named `hand_dector.py` to preserve the repository's existing command and avoid breaking current users.

## Add your own memes

Add `.jpg`, `.jpeg`, or `.png` files to the folder for the gesture you want to customize.

```text
peace/
├── reaction-1.jpg
├── reaction-2.png
└── reaction-3.jpeg
```

Folder names are derived from the gesture label by lowercasing and replacing spaces with underscores. For example, `OPEN HAND` uses `open_hand/`, and `THUMBS UP` uses `thumbs_up/`.

## Project structure

```text
hand_mem_dector/
├── fist/                  # Meme images for FIST
├── open_hand/             # Meme images for OPEN HAND
├── peace/                 # Meme images for PEACE
├── pointing/              # Meme images for POINTING
├── thumbs_up/             # Meme images for THUMBS UP
├── gesture.py             # Landmark-based gesture rules
├── hand_dector.py         # Webcam loop and MediaPipe integration
├── meme.py                # Project-relative random meme selection
├── hand_landmarker.task   # MediaPipe model asset
├── requirements.txt       # Python dependencies
└── README.md
```

## Troubleshooting

| Problem | Suggested fix |
| --- | --- |
| Webcam does not open | Close other applications using the camera and confirm your operating system has granted camera access. |
| `ModuleNotFoundError` | Activate the virtual environment, then run `python -m pip install -r requirements.txt`. |
| `hand_landmarker.task` cannot be found | Confirm the model file is in the repository root alongside `hand_dector.py`. |
| No meme appears | Check that the matching gesture folder exists and contains a supported image format (`.jpg`, `.jpeg`, or `.png`). |
| Gesture is `OTHER` | Improve lighting, keep the hand fully in frame, and face the camera more directly. |

## Limitations

- Detection is configured for one hand.
- Gesture rules are heuristic; lighting, hand orientation, and camera angle affect results.
- The project recognizes a small fixed set of gestures.
- Meme images open in a separate OpenCV window.
- The MediaPipe model asset must be available locally.

## Future improvements

- [ ] Add a screenshot or short demo GIF
- [ ] Support multiple hands and additional gestures
- [ ] Add confidence feedback and smoothing between frames
- [ ] Package the application with a friendlier desktop interface
- [ ] Add automated tests for the gesture rules
- [ ] Rename the legacy entry script in a backwards-compatible release

## Author

Built by [Pream-toki](https://github.com/Pream-toki).

## License

No license has been specified for this repository yet. Add a license before inviting others to reuse or distribute the code.
