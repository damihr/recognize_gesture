# train_model.py
import os
import json
import numpy as np
from sklearn import svm
import joblib

DATA_DIR = "gesture_data"

X, y = [], []

for file in os.listdir(DATA_DIR):
    if file.endswith(".json"):
        label = file.replace(".json", "")
        with open(os.path.join(DATA_DIR, file), "r") as f:
            data = json.load(f)
            for sample in data:
                X.append(sample)
                y.append(label)

X = np.array(X)
y = np.array(y)

print(f"📦 Loaded {len(X)} samples across {len(set(y))} gestures: {set(y)}")

# --- Train simple linear SVM ---
clf = svm.SVC(kernel="linear", probability=True)
clf.fit(X, y)

joblib.dump(clf, "asl_model.joblib")
print("✅ Model trained and saved as asl_model.joblib")
