# 🤟 Hand Gesture Recognition - How to Use

This guide explains how to use the gesture recognition system to train and recognize custom hand gestures.

## 📋 Overview

The system has 4 files, but **only 3 are needed** for the main workflow:

### Main Pipeline (Use These):
1. **`collect_gestures.py`** - Collect gesture samples
2. **`train_model.py`** - Train the model
3. **`translator.py`** - Recognize gestures in real-time

### Extra File (Not Used):
- **`collect.py`** - Alternative collection script (different format, not compatible)

---

## 🎯 Step-by-Step Guide

### Step 1: Collect Gesture Data

**File:** `collect_gestures.py`

**Purpose:** Record hand gesture samples for training

**How to use:**
```bash
python collect_gestures.py
```

**Process:**
1. Enter a gesture label when prompted (e.g., "A", "B", "HELLO", "CLEAR")
2. Show the gesture to your webcam
3. Press **SPACE** to save each sample
4. Collect multiple samples (recommended: 20-50 per gesture)
5. Press **Q** to quit and save

**What it does:**
- Saves samples to `gesture_data/` folder
- Each gesture gets its own JSON file (e.g., `A.json`, `B.json`)
- Supports 1 or 2 hands
- Creates 126-length feature vectors (2 hands × 21 landmarks × 3 coordinates)

**Example:**
```bash
$ python collect_gestures.py
Enter the gesture label (e.g., A, B, HELLO): A
🎥 Recording samples for 'A' — press SPACE to save, 'q' to quit.
✅ Saved sample #1
✅ Saved sample #2
...
💾 Saved 25 samples to gesture_data/A.json
```

**Tips:**
- Collect samples from different angles
- Vary hand positions slightly
- Collect 20-50 samples per gesture for better accuracy
- Repeat for each gesture you want to recognize

---

### Step 2: Train the Model

**File:** `train_model.py`

**Purpose:** Train a machine learning model from collected samples

**How to use:**
```bash
python train_model.py
```

**Process:**
1. Reads all JSON files from `gesture_data/` folder
2. Trains a Support Vector Machine (SVM) classifier
3. Saves the trained model as `asl_model.joblib`

**What it does:**
- Loads all gesture samples
- Trains a linear SVM model
- Saves model to `asl_model.joblib`

**Example:**
```bash
$ python train_model.py
📦 Loaded 75 samples across 3 gestures: {'A', 'B', 'CLEAR'}
✅ Model trained and saved as asl_model.joblib
```

**Requirements:**
- Must have collected data using `collect_gestures.py` first
- Needs at least 2 different gestures to train
- Requires `scikit-learn` and `joblib` packages

---

### Step 3: Recognize Gestures

**File:** `translator.py`

**Purpose:** Real-time gesture recognition using the trained model

**How to use:**
```bash
python translator.py
```

**Process:**
1. Loads the trained model (`asl_model.joblib`)
2. Opens webcam
3. Recognizes gestures in real-time
4. Shows prediction and confidence percentage

**What it does:**
- Detects hands using MediaPipe
- Extracts hand landmarks
- Predicts gesture using trained model
- Displays result with confidence score

**Example output:**
- Green text if confidence > 70%
- Yellow text if confidence ≤ 70%
- Shows: `Gesture: A (85.3%)`

**Controls:**
- Press **Q** to quit

---

## 🔄 Complete Workflow Example

```bash
# 1. Collect gesture "A"
python collect_gestures.py
# Enter: A
# Press SPACE 25 times, then Q

# 2. Collect gesture "B"
python collect_gestures.py
# Enter: B
# Press SPACE 25 times, then Q

# 3. Collect gesture "CLEAR"
python collect_gestures.py
# Enter: CLEAR
# Press SPACE 25 times, then Q

# 4. Train the model
python train_model.py
# Output: Model saved as asl_model.joblib

# 5. Test recognition
python translator.py
# Show gestures to camera, see predictions!
```

---

## 📁 File Structure

After running the scripts, you'll have:

```
hand_gesture_recognition/
├── collect_gestures.py      # ✅ Use this to collect
├── collect.py               # ❌ Extra (not compatible)
├── train_model.py           # ✅ Use this to train
├── translator.py            # ✅ Use this to recognize
├── gesture_data/            # Created by collect_gestures.py
│   ├── A.json
│   ├── B.json
│   └── CLEAR.json
└── asl_model.joblib         # Created by train_model.py
```

---

## ⚠️ Important Notes

### Why `collect.py` is Extra:

- **`collect_gestures.py`** saves to `gesture_data/` with 126-length vectors (compatible)
- **`collect.py`** saves to `gesture_dataset/` with different format (NOT compatible)
- **`train_model.py`** only reads from `gesture_data/` folder
- So `collect.py` won't work with the training pipeline

### Data Format:

- **collect_gestures.py**: Creates 126-length vectors (2 hands × 21 landmarks × 3 coords)
- **collect.py**: Creates per-hand landmark arrays (different structure)
- **train_model.py**: Expects 126-length vectors from `gesture_data/`

---

## 🛠️ Troubleshooting

### "Model not found" error
- Run `train_model.py` first to create `asl_model.joblib`

### "No samples found"
- Make sure you've collected data using `collect_gestures.py`
- Check that `gesture_data/` folder exists and has JSON files

### Low accuracy
- Collect more samples (50+ per gesture)
- Collect samples from different angles
- Ensure consistent gesture performance

### Camera not working
- Check camera permissions
- Try different camera index: `cv2.VideoCapture(1)`

---

## 📦 Dependencies

Required packages:
```bash
pip install opencv-python mediapipe numpy scikit-learn joblib
```

---

## 💡 Tips for Best Results

1. **Consistent Gestures**: Perform gestures the same way each time
2. **Good Lighting**: Ensure hands are well-lit and visible
3. **Multiple Samples**: Collect 30-50 samples per gesture
4. **Variety**: Include slight variations in hand position
5. **Clean Background**: Use a plain background for better detection

---

## 🎯 Use Cases

- **ASL Translation**: Recognize sign language letters
- **Custom Controls**: Create custom gesture commands
- **Accessibility**: Control apps with gestures
- **Games**: Gesture-based game controls

---

## Summary

**Main Workflow:**
1. `collect_gestures.py` → Collect samples
2. `train_model.py` → Train model
3. `translator.py` → Recognize gestures

**Extra File:**
- `collect.py` → Not used (different format)

Happy gesture training! 🎉

