# Gesture Recognition - All in One

Train and recognize custom hand gestures using MediaPipe and machine learning. Available as both Python scripts and a web application!

## Web Version (GitHub Pages)

**Try it online:** https://damihr.github.io/recognize_gesture/

The web version runs entirely in your browser with three integrated modes:
1. **Collect** - Record gesture samples
2. **Train** - Train the ML model
3. **Test** - Recognize gestures in real-time

## Python Version

For running locally with Python scripts.

### Requirements

- **Python 3.9** (recommended)
- Webcam/camera

### Installation

```bash
git clone git@github.com:damihr/recognize_gesture.git
cd recognize_gesture
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to Use

### Web Version (Recommended)

1. Open `index.html` in your browser
2. **Collect Mode:**
   - Enter a gesture label (e.g., "A", "B", "HELLO")
   - Click "Start Collecting"
   - Show the gesture and press SPACE to save samples
   - Collect 20-50 samples per gesture
3. **Train Mode:**
   - Click "Load Dataset" to see collected gestures
   - Click "Train Model" to train
   - Wait for training to complete
4. **Test Mode:**
   - Click "Start Testing"
   - Show gestures to camera
   - See real-time predictions!

### Python Version

See `HOW_TO_USE.md` for detailed instructions.

**Quick workflow:**
```bash
# 1. Collect gestures
python collect_gestures.py

# 2. Train model
python train_model.py

# 3. Test recognition
python translator.py
```

## Deploy to GitHub Pages

1. Push to GitHub
2. Go to Settings → Pages
3. Select branch: `main`, folder: `/ (root)`
4. Your app will be live at: `https://damihr.github.io/recognize_gesture/`

## 📁 Files

- **`index.html`** - All-in-one web application
- **`collect_gestures.py`** - Python data collection
- **`train_model.py`** - Python model training
- **`translator.py`** - Python gesture recognition
- **`requirements.txt`** - Python dependencies
- **`HOW_TO_USE.md`** - Detailed Python usage guide

## 🎯 Use Cases

- ASL (American Sign Language) recognition
- Custom gesture controls
- Accessibility applications
- Gesture-based games
- Hand gesture commands

## 📝 Notes

- Web version uses TensorFlow.js (runs client-side)
- Python version uses scikit-learn SVM
- Both support 1 or 2 hands
- Data format: 126-length vectors (2 hands × 21 landmarks × 3 coords)

## License

MIT License

