import cv2
import mediapipe as mp
import numpy as np
import joblib
import os

# --- MediaPipe setup ---
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,  # ✅ now supports both hands
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6
)

# --- Load trained model ---
if not os.path.exists("asl_model.joblib"):
    raise FileNotFoundError("❌ Model not found. Train it first using train_model.py")

model = joblib.load("asl_model.joblib")

# --- Open webcam ---
cap = cv2.VideoCapture(0)
print("🤟 ASL Translator active — show your gesture (1 or 2 hands). Press 'q' to quit.")

def extract_landmarks(results):
    """
    Extract normalized landmarks for up to two hands.
    Pads with zeros if only one hand detected.
    Returns a 126-length flattened list (63 × 2).
    """
    all_landmarks = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Each hand: 21 landmarks × (x, y, z)
            coords = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()
            all_landmarks.append(coords)
    # If only one hand detected, pad the second one with zeros
    if len(all_landmarks) == 1:
        all_landmarks.append(np.zeros(63))
    elif len(all_landmarks) == 0:
        all_landmarks = [np.zeros(63), np.zeros(63)]

    # Flatten to single vector of length 126
    return np.concatenate(all_landmarks)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        # Draw both hands
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        landmarks = extract_landmarks(results)

        try:
            pred = model.predict([landmarks])[0]
            prob = model.predict_proba([landmarks]).max()

            color = (0, 255, 0) if prob > 0.7 else (0, 255, 255)
            text = f"Gesture: {pred} ({prob*100:.1f}%)"

            cv2.putText(frame, text, (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        except Exception as e:
            cv2.putText(frame, "Prediction error", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "No hands detected", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)

    cv2.imshow("ASL Translator (1 or 2 hands)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
