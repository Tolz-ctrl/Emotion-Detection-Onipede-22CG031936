"""
Flask Application for Emotion Detection
This app uses a pre-trained TensorFlow model to detect emotions from uploaded images.
Author: Onipede-22CG031936
"""

from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Emotion labels (adjust based on your model's output classes)
EMOTION_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Load the pre-trained emotion detection model
MODEL_PATH = 'face_emotionModel.h5'
try:
    model = keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension
    Args:
        filename: Name of the uploaded file
    Returns:
        Boolean indicating if file extension is allowed
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_path):
    """
    Preprocess the uploaded image for model prediction
    Args:
        image_path: Path to the uploaded image
    Returns:
        Preprocessed image array ready for prediction
    """
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    
    # Convert to grayscale (most emotion models use grayscale)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect face using Haar Cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) == 0:
        # If no face detected, use the whole image
        face_roi = gray
    else:
        # Use the first detected face
        (x, y, w, h) = faces[0]
        face_roi = gray[y:y+h, x:x+w]
    
    # Resize to model's expected input size (typically 48x48 for emotion models)
    face_roi = cv2.resize(face_roi, (48, 48))
    
    # Normalize pixel values to [0, 1]
    face_roi = face_roi.astype('float32') / 255.0
    
    # Reshape for model input: (1, 48, 48, 1) for grayscale
    face_roi = np.expand_dims(face_roi, axis=0)
    face_roi = np.expand_dims(face_roi, axis=-1)
    
    return face_roi


def predict_emotion(image_path):
    """
    Predict emotion from the uploaded image
    Args:
        image_path: Path to the uploaded image
    Returns:
        Tuple of (predicted_emotion, confidence_score)
    """
    if model is None:
        return "Model not loaded", 0.0
    
    try:
        # Preprocess the image
        processed_image = preprocess_image(image_path)
        
        # Make prediction
        predictions = model.predict(processed_image)
        
        # Get the emotion with highest probability
        emotion_index = np.argmax(predictions[0])
        confidence = float(predictions[0][emotion_index]) * 100
        
        # Get emotion label
        emotion = EMOTION_LABELS[emotion_index]
        
        return emotion, confidence
    
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Error", 0.0


@app.route('/', methods=['GET'])
def index():
    """
    Render the main page
    """
    return render_template('index.htm')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle image upload and emotion prediction
    """
    # Check if file was uploaded
    if 'file' not in request.files:
        return render_template('index.htm', error="No file uploaded")
    
    file = request.files['file']
    
    # Check if file was selected
    if file.filename == '':
        return render_template('index.htm', error="No file selected")
    
    # Check if file type is allowed
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Predict emotion
        emotion, confidence = predict_emotion(filepath)
        
        # Render template with results
        return render_template('index.htm', 
                             emotion=emotion, 
                             confidence=round(confidence, 2),
                             image_path=filepath)
    else:
        return render_template('index.htm', error="Invalid file type. Please upload an image (PNG, JPG, JPEG, GIF)")


@app.route('/reset', methods=['GET'])
def reset():
    """
    Reset the page and clear previous results
    """
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Run the Flask app
    # Set debug=False in production
    app.run(debug=True, host='0.0.0.0', port=5000)

