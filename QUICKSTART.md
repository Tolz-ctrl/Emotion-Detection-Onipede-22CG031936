# 🚀 Quick Start Guide

## Get Your Emotion Detection App Running in 5 Minutes!

---

### Step 1: Install Dependencies
```bash
cd Onipede-22CG031936
pip install -r requirements.txt
```

**Expected output:** All packages installed successfully

---

### Step 2: Add Your Model

Place your trained `face_emotionModel.h5` file in the project root:

```
Onipede-22CG031936/
├── face_emotionModel.h5  ← PUT YOUR MODEL HERE
├── app.py
└── ...
```

**Don't have a model?** See `MODEL_PLACEHOLDER.txt` for training instructions.

---

### Step 3: Run the Application
```bash
python app.py
```

**Expected output:**
```
Model loaded successfully!
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

---

### Step 4: Open in Browser

Navigate to: **http://localhost:5000**

---

### Step 5: Test the App

1. Click **"Choose Image File"**
2. Select a photo with a clear face
3. Click **"Detect Emotion"**
4. View the results! 🎉

---

## 📸 Test Images

For best results, use images with:
- ✅ Clear, frontal faces
- ✅ Good lighting
- ✅ Single person (or primary face)
- ✅ Formats: JPG, PNG, JPEG, GIF

---

## ⚠️ Troubleshooting

### "Model not loaded" error
- Ensure `face_emotionModel.h5` is in the root directory
- Check file name spelling (case-sensitive)

### "No face detected"
- Use clearer images with visible faces
- Ensure face is frontal and well-lit

### Port already in use
```bash
# Change port in app.py (last line):
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

## 🎯 Next Steps

- Deploy to Render, Heroku, or PythonAnywhere
- Update `link_web_app.txt` with your deployed URL
- Share your app with friends!

---

**Need Help?** Check `README.md` for detailed documentation.

**Author:** Onipede - 22CG031936

