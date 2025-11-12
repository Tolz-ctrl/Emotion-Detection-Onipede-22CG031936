# 🎭 Emotion Detection Web Application

**Author:** Onipede - 22CG031936
**Technology Stack:** Flask, TensorFlow, OpenCV, HTML/CSS

---

## 📋 Project Overview

This is a Flask-based web application that detects human emotions from uploaded images using a pre-trained TensorFlow deep learning model. The application can identify 7 different emotions: Happy, Sad, Angry, Surprise, Fear, Disgust, and Neutral.

---

## 🗂️ Project Structure

```
Onipede-22CG031936/
│
├── app.py                  # Main Flask application
├── face_emotionModel.h5    # Pre-trained TensorFlow model (to be added)
├── requirements.txt        # Python dependencies
├── link_web_app.txt       # Deployment link placeholder
├── README.md              # Project documentation
│
├── templates/
│   └── index.htm          # HTML template for the web interface
│
└── static/
    ├── styles.css         # CSS styling
    └── uploads/           # Folder for uploaded images (auto-created)
```

---

## ✨ Features

- **Image Upload:** Users can upload images in PNG, JPG, JPEG, or GIF format
- **Face Detection:** Automatically detects faces in uploaded images using Haar Cascade
- **Emotion Recognition:** Predicts emotions using a pre-trained TensorFlow model
- **Confidence Score:** Displays prediction confidence percentage
- **Responsive Design:** Modern, mobile-friendly interface
- **Visual Feedback:** Shows uploaded image with predicted emotion and emoji

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project
```bash
cd Onipede-22CG031936
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Add the Pre-trained Model
Place your trained `face_emotionModel.h5` file in the root directory of the project (Onipede-22CG031936/).

**Model Requirements:**
- Input shape: (48, 48, 1) - Grayscale images
- Output: 7 classes (Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral)
- Format: Keras/TensorFlow .h5 file

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Web App
Open your browser and navigate to:
```
http://localhost:5000
```

---

## 🎯 How to Use

1. **Open the Application** in your web browser
2. **Click "Choose Image File"** to select an image from your device
3. **Click "Detect Emotion"** to upload and analyze the image
4. **View Results:**
   - Uploaded image with border
   - Predicted emotion in bold text
   - Confidence score percentage
   - Emotion emoji
5. **Upload Another Image** using the reset button

---

## 🧠 Model Information

The application expects a TensorFlow/Keras model with the following specifications:

- **Input:** 48x48 grayscale images
- **Architecture:** CNN (Convolutional Neural Network)
- **Output Classes:** 7 emotions
  1. Angry 😠
  2. Disgust 🤢
  3. Fear 😨
  4. Happy 😊
  5. Sad 😢
  6. Surprise 😲
  7. Neutral 😐

---

## 📦 Dependencies

- **Flask 3.0.0** - Web framework
- **TensorFlow 2.18.0** - Deep learning model
- **OpenCV 4.8.1.78** - Image processing and face detection
- **NumPy 1.24.3** - Numerical operations
- **Werkzeug 3.0.1** - WSGI utilities
- **Pillow 10.1.0** - Image handling

---

## 🌐 Deployment

### Local Deployment
```bash
python app.py
# Access at http://localhost:5000
```

### Production Deployment Options

1. **Render** (Recommended)
   - Free tier available
   - Easy GitHub integration
   - Automatic deployments

2. **Heroku**
   - Popular PaaS platform
   - Free tier with limitations

3. **PythonAnywhere**
   - Python-specific hosting
   - Simple setup

4. **Google Cloud / AWS**
   - Enterprise-grade hosting
   - Scalable infrastructure

**Note:** Update `link_web_app.txt` with your deployed URL.

---

## 🛠️ Configuration

### File Upload Settings (in `app.py`)
```python
UPLOAD_FOLDER = 'static/uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
```

### Model Path
```python
MODEL_PATH = 'face_emotionModel.h5'
```

### Server Settings
```python
app.run(debug=True, host='0.0.0.0', port=5000)
# Set debug=False for production
```

---

## 🐛 Troubleshooting

### Model Not Loading
- Ensure `face_emotionModel.h5` is in the root directory
- Check TensorFlow version compatibility
- Verify model file is not corrupted

### Face Not Detected
- Use clear, well-lit images
- Ensure face is visible and frontal
- Try images with larger face sizes

### Upload Errors
- Check file size (max 16MB)
- Verify file format (PNG, JPG, JPEG, GIF)
- Ensure `static/uploads/` folder exists

---

## 📝 Code Structure

### `app.py`
- Flask application initialization
- Model loading and prediction logic
- Image preprocessing and face detection
- Route handlers for upload and prediction

### `templates/index.htm`
- HTML structure
- File upload form
- Results display section
- JavaScript for file name display

### `static/styles.css`
- Modern gradient design
- Responsive layout
- Button and form styling
- Animation effects

---

## 🔒 Security Considerations

- File type validation
- Secure filename handling
- File size limits
- Input sanitization
- Debug mode disabled in production

---

## 📈 Future Enhancements

- [ ] Real-time webcam emotion detection
- [ ] Multiple face detection in single image
- [ ] Emotion history tracking
- [ ] API endpoint for programmatic access
- [ ] Database integration for storing results
- [ ] User authentication system
- [ ] Batch image processing

---

## 📄 License

This project is created for educational purposes as part of academic coursework.

---

## 👤 Author

**Onipede**
Student ID: 22CG031936

---

## 🙏 Acknowledgments

- TensorFlow team for the deep learning framework
- OpenCV community for computer vision tools
- Flask developers for the web framework

---

**Last Updated:** 2025-11-12

