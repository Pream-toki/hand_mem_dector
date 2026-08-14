def detect_gesture(hand):

    # Four fingers
    index_up = hand[8].y < hand[6].y
    middle_up = hand[12].y < hand[10].y
    ring_up = hand[16].y < hand[14].y
    pinky_up = hand[20].y < hand[18].y

    # Thumb
    thumb_tip = hand[4]
    thumb_ip = hand[3]
    thumb_mcp = hand[2]

    import math

    def distance(a, b):
        return math.sqrt(
            (a.x - b.x) ** 2 +
            (a.y - b.y) ** 2
        )

    thumb_extended = (
        distance(thumb_tip, hand[0])
        >
        distance(thumb_ip, hand[0])
    )

    # 👍 THUMBS UP
    if (
        thumb_extended
        and not index_up
        and not middle_up
        and not ring_up
        and not pinky_up
        and thumb_tip.y < thumb_mcp.y
    ):
        return "THUMBS UP"

    # ✊ FIST
    if (
        not index_up
        and not middle_up
        and not ring_up
        and not pinky_up
        and not thumb_extended
    ):
        return "FIST"

    # ✋ OPEN HAND
    if (
        index_up
        and middle_up
        and ring_up
        and pinky_up
    ):
        return "OPEN HAND"

    # ✌️ PEACE
    if (
        index_up
        and middle_up
        and not ring_up
        and not pinky_up
    ):
        return "PEACE"

    # ☝️ POINTING
    if (
        index_up
        and not middle_up
        and not ring_up
        and not pinky_up
    ):
        return "POINTING"

    return "OTHER"
