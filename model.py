"""
Emotion Detection Model Training Script
Author: Onipede - 22CG031936
Date: November 2025

This script contains the complete CNN architecture and training code
for the emotion detection model used in the Flask web application.

Model Specifications:
- Input: 48x48 grayscale images
- Output: 7 emotion classes (Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral)
- Framework: TensorFlow/Keras
- Architecture: Convolutional Neural Network (CNN)
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import numpy as np
import os

# Set random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# ============================================================================
# MODEL ARCHITECTURE
# ============================================================================

def create_emotion_model(input_shape=(48, 48, 1), num_classes=7):
    """
    Create CNN model for emotion detection
    
    Args:
        input_shape: Shape of input images (height, width, channels)
        num_classes: Number of emotion classes to predict
    
    Returns:
        Compiled Keras model
    """
    model = models.Sequential([
        # First Convolutional Block
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape, padding='same'),
        layers.BatchNormalization(),
        layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Second Convolutional Block
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Third Convolutional Block
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Fourth Convolutional Block
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Flatten and Dense Layers
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        
        # Output Layer
        layers.Dense(num_classes, activation='softmax')
    ])
    
    return model

# ============================================================================
# DATA PREPROCESSING AND AUGMENTATION
# ============================================================================

def create_data_generators(train_dir, val_dir, batch_size=32):
    """
    Create data generators for training and validation
    
    Args:
        train_dir: Directory containing training data
        val_dir: Directory containing validation data
        batch_size: Batch size for training
    
    Returns:
        train_generator, validation_generator
    """
    # Data augmentation for training set
    train_datagen = ImageDataGenerator(
        rescale=1./255,              # Normalize pixel values to [0, 1]
        rotation_range=20,           # Randomly rotate images
        width_shift_range=0.2,       # Randomly shift images horizontally
        height_shift_range=0.2,      # Randomly shift images vertically
        horizontal_flip=True,        # Randomly flip images horizontally
        zoom_range=0.2,              # Randomly zoom images
        shear_range=0.2,             # Randomly apply shear transformation
        fill_mode='nearest'          # Fill mode for new pixels
    )
    
    # Only rescaling for validation set (no augmentation)
    val_datagen = ImageDataGenerator(rescale=1./255)
    
    # Create generators
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(48, 48),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True
    )
    
    validation_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(48, 48),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False
    )
    
    return train_generator, validation_generator

# ============================================================================
# MODEL COMPILATION
# ============================================================================

def compile_model(model, learning_rate=0.001):
    """
    Compile the model with optimizer, loss function, and metrics

    Args:
        model: Keras model to compile
        learning_rate: Learning rate for optimizer

    Returns:
        Compiled model
    """
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)

    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',  # Multi-class classification loss
        metrics=['accuracy']               # Track accuracy during training
    )

    return model

# ============================================================================
# TRAINING CALLBACKS
# ============================================================================

def create_callbacks(model_save_path='face_emotionModel.h5'):
    """
    Create callbacks for training

    Args:
        model_save_path: Path to save the best model

    Returns:
        List of callbacks
    """
    # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True,
        verbose=1
    )

    # Reduce learning rate when validation loss plateaus
    reduce_lr = ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=5,
        min_lr=1e-7,
        verbose=1
    )

    # Save the best model during training
    model_checkpoint = ModelCheckpoint(
        model_save_path,
        monitor='val_accuracy',
        save_best_only=True,
        mode='max',
        verbose=1
    )

    return [early_stopping, reduce_lr, model_checkpoint]

# ============================================================================
# TRAINING FUNCTION
# ============================================================================

def train_model(train_dir, val_dir, epochs=50, batch_size=32):
    """
    Complete training pipeline for emotion detection model

    Args:
        train_dir: Directory containing training data organized by class
        val_dir: Directory containing validation data organized by class
        epochs: Number of training epochs
        batch_size: Batch size for training

    Returns:
        Trained model and training history
    """
    print("=" * 70)
    print("EMOTION DETECTION MODEL TRAINING - Onipede 22CG031936")
    print("=" * 70)

    # Create model
    print("\n[1/5] Creating model architecture...")
    model = create_emotion_model(input_shape=(48, 48, 1), num_classes=7)

    # Display model summary
    print("\nModel Architecture:")
    model.summary()

    # Compile model
    print("\n[2/5] Compiling model...")
    model = compile_model(model, learning_rate=0.001)

    # Create data generators
    print("\n[3/5] Creating data generators...")
    train_generator, validation_generator = create_data_generators(
        train_dir, val_dir, batch_size
    )

    print(f"Training samples: {train_generator.samples}")
    print(f"Validation samples: {validation_generator.samples}")
    print(f"Classes: {list(train_generator.class_indices.keys())}")

    # Create callbacks
    print("\n[4/5] Setting up training callbacks...")
    callbacks = create_callbacks('face_emotionModel.h5')

    # Train model
    print("\n[5/5] Starting training...")
    print(f"Epochs: {epochs}")
    print(f"Batch size: {batch_size}")
    print("-" * 70)

    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator,
        callbacks=callbacks,
        verbose=1
    )

    print("\n" + "=" * 70)
    print("TRAINING COMPLETED!")
    print("=" * 70)

    return model, history

# ============================================================================
# MODEL EVALUATION
# ============================================================================

def evaluate_model(model, test_dir, batch_size=32):
    """
    Evaluate the trained model on test data

    Args:
        model: Trained Keras model
        test_dir: Directory containing test data
        batch_size: Batch size for evaluation

    Returns:
        Test loss and accuracy
    """
    print("\n" + "=" * 70)
    print("MODEL EVALUATION")
    print("=" * 70)

    # Create test data generator
    test_datagen = ImageDataGenerator(rescale=1./255)

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(48, 48),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False
    )

    # Evaluate model
    print(f"\nEvaluating on {test_generator.samples} test samples...")
    test_loss, test_accuracy = model.evaluate(test_generator, verbose=1)

    print(f"\nTest Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
    print("=" * 70)

    return test_loss, test_accuracy

# ============================================================================
# SAVE MODEL
# ============================================================================

def save_model(model, filepath='face_emotionModel.h5'):
    """
    Save the trained model to disk

    Args:
        model: Trained Keras model
        filepath: Path to save the model
    """
    print(f"\nSaving model to {filepath}...")
    model.save(filepath)
    print(f"✓ Model saved successfully!")

    # Display file size
    file_size = os.path.getsize(filepath) / (1024 * 1024)  # Convert to MB
    print(f"Model file size: {file_size:.2f} MB")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    """
    Main execution block for training the emotion detection model

    DATASET STRUCTURE:
    ------------------
    The dataset should be organized as follows:

    data/
    ├── train/
    │   ├── angry/
    │   ├── disgust/
    │   ├── fear/
    │   ├── happy/
    │   ├── sad/
    │   ├── surprise/
    │   └── neutral/
    ├── validation/
    │   ├── angry/
    │   ├── disgust/
    │   ├── fear/
    │   ├── happy/
    │   ├── sad/
    │   ├── surprise/
    │   └── neutral/
    └── test/
        ├── angry/
        ├── disgust/
        ├── fear/
        ├── happy/
        ├── sad/
        ├── surprise/
        └── neutral/

    RECOMMENDED DATASETS:
    ---------------------
    - FER-2013 (Facial Expression Recognition 2013)
    - CK+ (Extended Cohn-Kanade Dataset)
    - JAFFE (Japanese Female Facial Expression Database)
    - AffectNet

    USAGE:
    ------
    1. Download and prepare your dataset in the structure above
    2. Update the paths below to point to your dataset
    3. Run this script: python model.py
    4. The trained model will be saved as 'face_emotionModel.h5'
    """

    # ========================================================================
    # CONFIGURATION
    # ========================================================================

    # Dataset paths (UPDATE THESE PATHS TO YOUR DATASET LOCATION)
    TRAIN_DIR = 'data/train'
    VAL_DIR = 'data/validation'
    TEST_DIR = 'data/test'

    # Training hyperparameters
    EPOCHS = 50
    BATCH_SIZE = 32

    # Model save path
    MODEL_SAVE_PATH = 'face_emotionModel.h5'

    # ========================================================================
    # TRAINING PIPELINE
    # ========================================================================

    print("\n" + "=" * 70)
    print("EMOTION DETECTION MODEL TRAINING SCRIPT")
    print("Author: Onipede - 22CG031936")
    print("=" * 70)

    # Check if dataset directories exist
    if not os.path.exists(TRAIN_DIR):
        print(f"\n⚠️  ERROR: Training directory not found: {TRAIN_DIR}")
        print("\nPlease ensure your dataset is organized in the following structure:")
        print("data/train/, data/validation/, data/test/")
        print("Each directory should contain subdirectories for each emotion class.")
        print("\nRecommended datasets: FER-2013, CK+, JAFFE, AffectNet")
        print("\nOnce you have prepared the dataset, update the paths in this script")
        print("and run again: python model.py")
    else:
        # Train the model
        model, history = train_model(
            train_dir=TRAIN_DIR,
            val_dir=VAL_DIR,
            epochs=EPOCHS,
            batch_size=BATCH_SIZE
        )

        # Evaluate on test set (if available)
        if os.path.exists(TEST_DIR):
            evaluate_model(model, TEST_DIR, BATCH_SIZE)

        # Save the final model
        save_model(model, MODEL_SAVE_PATH)

        print("\n" + "=" * 70)
        print("✓ ALL DONE!")
        print("=" * 70)
        print(f"\nYour trained model is ready: {MODEL_SAVE_PATH}")
        print("You can now use this model in your Flask application!")
        print("\nAuthor: Onipede - 22CG031936")
        print("=" * 70 + "\n")

