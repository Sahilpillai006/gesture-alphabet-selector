import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

alphabet = [chr(i) for i in range(65, 91)]  # A-Z
radius = 120

# Word storage
current_word = ""
letter_added = False
space_added = False
erase_done = False

# Start video
cap = cv2.VideoCapture(0)

def fingers_up(hand):
    landmarks = hand.landmark
    fingers = []

    # Tip ids: index, middle, ring, pinky
    tip_ids = [8, 12, 16, 20]

    for tip in tip_ids:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers  # [index, middle, ring, pinky]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Rotary position (right side)
    cx = int(w * 0.75)
    cy = int(h * 0.5)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    finger_x, finger_y = None, None
    selected_letter = None

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        # Index finger tip
        lm = hand.landmark[8]
        finger_x = int(lm.x * w)
        finger_y = int(lm.y * h)

        # Finger states
        up = fingers_up(hand)

        only_index = up == [1, 0, 0, 0]
        index_middle = up == [1, 1, 0, 0]
        fist = up == [0, 0, 0, 0]

        # Rotary angle
        dx = finger_x - cx
        dy = finger_y - cy
        angle = math.degrees(math.atan2(dy, dx))
        angle = (angle + 360) % 360

        slice_angle = 360 / 26
        index = int(angle // slice_angle)
        selected_letter = alphabet[index]

        # Pointer line
        cv2.line(frame, (cx, cy), (finger_x, finger_y), (0, 255, 0), 2)

        # Add letter
        if only_index and not letter_added:
            current_word += selected_letter
            letter_added = True

        if not only_index:
            letter_added = False

        # Add space
        if index_middle and not space_added:
            current_word += " "
            space_added = True

        if not index_middle:
            space_added = False

        # Erase word (fist)
        if fist and not erase_done:
            current_word = ""
            erase_done = True

        if not fist:
            erase_done = False

    # Draw rotary circle
    cv2.circle(frame, (cx, cy), radius, (255, 255, 0), 2)

    # Draw letters
    for i, char in enumerate(alphabet):
        theta = math.radians(i * (360 / 26))
        text_x = cx + int((radius + 40) * math.cos(theta))
        text_y = cy + int((radius + 40) * math.sin(theta))

        color = (255, 255, 255)
        if selected_letter == char:
            color = (0, 0, 255)

        cv2.putText(
            frame, char,
            (text_x - 10, text_y + 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color, 2
        )

    # Display word
    cv2.putText(
        frame, current_word,
        (50, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 255, 0), 3
    )

    cv2.imshow("Side Rotary Alphabet Selector", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
