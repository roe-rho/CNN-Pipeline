# -*- coding: utf-8 -*-
"""CNN TASK COMPLETE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tTWal9gygJuTABb-3TjAHWvXwIE--MFE

# Imports
"""

import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

"""# Data Analysis and Preparation"""

# Save results
RESULTS_DIR = './results'
PLOTS_DIR = os.path.join(RESULTS_DIR, 'plots')
MODEL_DIR = os.path.join(RESULTS_DIR, 'saved_models')
os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# Load and prepare data
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
y_train, y_test = to_categorical(y_train, 10), to_categorical(y_test, 10)

"""# Model Construction and Training"""

# Define CNN model
def create_cnn(input_shape=(32, 32, 3), num_classes=10):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Create and compile the model
model = create_cnn()
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_split=0.2)

"""# Model Evaluation"""

# Save the model
model_path = os.path.join(MODEL_DIR, 'cnn_cifar10.h5')
model.save(model_path)
print(f"Model saved at: {model_path}")

# Save training history
history_path = os.path.join(RESULTS_DIR, 'training_history.txt')
with open(history_path, 'w') as f:
    f.write(str(history.history))
print(f"Training history saved at: {history_path}")

"""# Hyperparameter Tuning (needs to be tried by yourself)

# Visualization
"""

# Visualize and save the training process
def plot_training(history, save_dir):
    plt.figure(figsize=(12, 4))

    # Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history['accuracy'], label='Train Accuracy')
    plt.plot(history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    # Loss
    plt.subplot(1, 2, 2)
    plt.plot(history['loss'], label='Train Loss')
    plt.plot(history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # Save the plot
    plot_path = os.path.join(save_dir, 'training_plots.png')
    plt.savefig(plot_path)
    plt.show()
    print(f"Plots saved at: {plot_path}")

plot_training(history.history, PLOTS_DIR)

# Evaluate on the test dataset
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")
# -*- coding: utf-8 -*-
"""CNN TASK COMPLETE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tTWal9gygJuTABb-3TjAHWvXwIE--MFE

# Imports
"""

import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

"""# Data Analysis and Preparation"""

# Save results
RESULTS_DIR = './results'
PLOTS_DIR = os.path.join(RESULTS_DIR, 'plots')
MODEL_DIR = os.path.join(RESULTS_DIR, 'saved_models')
os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# Load and prepare data
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
y_train, y_test = to_categorical(y_train, 10), to_categorical(y_test, 10)

"""# Model Construction and Training"""

# Define CNN model
def create_cnn(input_shape=(32, 32, 3), num_classes=10):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Create and compile the model
model = create_cnn()
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_split=0.2)

"""# Model Evaluation"""

# Save the model
model_path = os.path.join(MODEL_DIR, 'cnn_cifar10.h5')
model.save(model_path)
print(f"Model saved at: {model_path}")

# Save training history
history_path = os.path.join(RESULTS_DIR, 'training_history.txt')
with open(history_path, 'w') as f:
    f.write(str(history.history))
print(f"Training history saved at: {history_path}")

"""# Hyperparameter Tuning (needs to be tried by yourself)

# Visualization
"""

# Visualize and save the training process
def plot_training(history, save_dir):
    plt.figure(figsize=(12, 4))

    # Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history['accuracy'], label='Train Accuracy')
    plt.plot(history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    # Loss
    plt.subplot(1, 2, 2)
    plt.plot(history['loss'], label='Train Loss')
    plt.plot(history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # Save the plot
    plot_path = os.path.join(save_dir, 'training_plots.png')
    plt.savefig(plot_path)
    plt.show()
    print(f"Plots saved at: {plot_path}")

plot_training(history.history, PLOTS_DIR)

# Evaluate on the test dataset
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")
