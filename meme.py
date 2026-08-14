import os
import random
import cv2


PROJECT_FOLDER = r"your directory"

MEME_FOLDER = PROJECT_FOLDER


def get_random_meme(gesture):

    # Convert:
    # "OPEN HAND" → "open_hand"
    # "THUMBS UP" → "thumbs_up"

    folder_name = gesture.lower().replace(" ", "_")

    folder_path = os.path.join(
        MEME_FOLDER,
        folder_name
    )

    if not os.path.exists(folder_path):

        print("Folder not found:", folder_path)

        return None

    images = []

    for filename in os.listdir(folder_path):

        if filename.lower().endswith(
                (".jpg", ".jpeg", ".png")
        ):

            images.append(
                os.path.join(
                    folder_path,
                    filename
                )
            )

    if not images:

        print(
            "No images found in:",
            folder_path
        )

        return None

    return random.choice(images)
