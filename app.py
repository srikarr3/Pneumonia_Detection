import os
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from util import base64_to_pil

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = 'models/Model.h5'
model = load_model(MODEL_PATH)
print('Model loaded. Ready to serve...')

def model_predict(img, model):
    # Resize image to 128x128
    img = img.resize((128, 128))

    # Convert to RGB if not already
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Convert to numpy array and normalize pixel values
    x = image.img_to_array(img)
    x = x / 255.0  # Normalize to [0, 1]
    x = np.expand_dims(x, axis=0)  # Add batch dimension

    # Predict using the model
    preds = model.predict(x)
    return preds

@app.route('/', methods=['GET'])
def index():
    # Render the main page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Convert base64 image data to PIL image
            img = base64_to_pil(request.json)

            # Save the uploaded image for verification (optional)
            img.save("uploads/image.jpg")

            # Predict using the model
            preds = model_predict(img, model)
            result = preds[0, 0]

            # Return prediction result
            if result > 0.5:
                return jsonify(result="PNEUMONIA")
            else:
                return jsonify(result="NORMAL")
        except Exception as e:
            print(f"Error during prediction: {e}")
            return jsonify(result="Error: Could not process the image.")

    return None

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5002, threaded=False)
