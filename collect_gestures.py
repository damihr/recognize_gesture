# collect_gestures.py
import cv2
import mediapipe as mp
import numpy as np
import os
import json

# --- Setup ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,  # ✅ Allow up to 2 hands
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

DATA_DIR = "gesture_data"
os.makedirs(DATA_DIR, exist_ok=True)

label = input("Enter the gesture label (e.g., A, B, HELLO): ").strip().upper()
samples = []

cap = cv2.VideoCapture(0)
print(f"🎥 Recording samples for '{label}' — press SPACE to save, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    all_landmarks = []

    if res.multi_hand_landmarks:
        for hand_landmarks in res.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Collect all 21 (x, y, z) landmarks per hand
            lm = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()
            all_landmarks.extend(lm)

    # Ensure we always have the same input size (2 hands * 21 landmarks * 3 coords = 126 values)
    # If only one hand is visible, pad with zeros
    if len(all_landmarks) < 126:
        all_landmarks.extend([0.0] * (126 - len(all_landmarks)))

    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):
        samples.append(all_landmarks)
        print(f"✅ Saved sample #{len(samples)}")

    cv2.putText(frame, f"Label: {label} | Samples: {len(samples)}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Collect Gestures", frame)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# --- Save dataset ---
save_path = os.path.join(DATA_DIR, f"{label}.json")
with open(save_path, "w") as f:
    json.dump(samples, f)

print(f"💾 Saved {len(samples)} samples to {save_path}")
