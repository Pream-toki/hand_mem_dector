# Hand Gesture Meme Detector

Points your webcam at your hand, recognizes the gesture, and pops up a
matching meme. Built with OpenCV + MediaPipe while I was learning computer
vision.

## Gestures

FIST, PEACE, OPEN HAND, POINTING, THUMBS UP — each one picks a random meme
from its folder (`fist/`, `peace/`, `open_hand/`, `pointing/`). Press `q`
to quit.

## Status

Work in progress. A few files aren't pushed yet (`gesture.py`, `meme.py`
and the `hand_landmarker.task` model) — once those are in, it runs with:

```bash
pip install opencv-python mediapipe
python gesture.py
```

Made for learning, so expect rough edges.
