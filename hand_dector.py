import cv2
from pathlib import Path

import mediapipe as mp

from gesture import detect_gesture
from meme import get_random_meme


# ==========================================
# CAMERA
# ==========================================

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open webcam.")
    exit()


# ==========================================
# MEDIAPIPE
# ==========================================

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=str(Path(__file__).with_name("hand_landmarker.task"))
    ),
    running_mode=RunningMode.IMAGE,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)


# ==========================================
# VARIABLES
# ==========================================

current_gesture = None
current_meme = None


# ==========================================
# START
# ==========================================

with HandLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = camera.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        result = landmarker.detect(mp_image)

        gesture = "NO HAND"


        # ==========================================
        # HAND DETECTED
        # ==========================================

        if result.hand_landmarks:

            hand = result.hand_landmarks[0]

            gesture = detect_gesture(hand)


            # ==========================================
            # ONLY CHANGE MEME WHEN GESTURE CHANGES
            # ==========================================

            if gesture != current_gesture:

                current_gesture = gesture

                print("Gesture:", gesture)

                valid_gestures = [
                    "FIST",
                    "POINTING",
                    "PEACE",
                    "OPEN HAND",
                    "THUMBS UP"
                ]

                if gesture in valid_gestures:

                    meme_path = get_random_meme(gesture)

                    if meme_path:

                        new_meme = cv2.imread(meme_path)

                        if new_meme is not None:

                            current_meme = new_meme

                            print(
                                "Showing:",
                                meme_path
                            )

                    else:

                        # No meme for this gesture
                        current_meme = None


            # ==========================================
            # DRAW LANDMARKS
            # ==========================================

            height, width, _ = frame.shape

            for landmark in hand:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                cv2.circle(
                    frame,
                    (x, y),
                    6,
                    (0, 255, 0),
                    -1
                )


        # ==========================================
        # NO HAND
        # ==========================================

        else:

            if current_gesture != "NO HAND":

                current_gesture = "NO HAND"

                # Remove the old meme
                current_meme = None


        # ==========================================
        # SHOW GESTURE
        # ==========================================

        cv2.putText(
            frame,
            f"Gesture: {gesture}",
            (30, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 255, 0),
            3
        )


        # ==========================================
        # SHOW MEME
        # ==========================================

        if current_meme is not None:

            cv2.imshow(
                "MEME",
                current_meme
            )

        else:

            # Close the meme window when
            # there is no current meme
            try:
                cv2.destroyWindow("MEME")
            except:
                pass


        # ==========================================
        # SHOW CAMERA
        # ==========================================

        cv2.imshow(
            "Hand Gesture Camera",
            frame
        )


        # ==========================================
        # QUIT
        # ==========================================

        key = cv2.waitKey(10) & 0xFF

        if key == ord("q") or key == ord("Q") or key == 27:

            break


# ==========================================
# CLEANUP
# ==========================================

camera.release()

cv2.destroyAllWindows()
