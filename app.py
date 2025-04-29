import logging
from flask import Flask, request, render_template, jsonify
import time
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static', template_folder='templates')

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for "What Are the Dangers of Deepfake Images?"
@app.route('/what-are-dangers-of-deepfake-images.html')
def dangers():
    return render_template('what-are-dangers-of-deepfake-images.html')

# Route for "What is Deepfake?"
@app.route('/what-is-deepfake.html')
def what_is_deepfake():
    return render_template('what-is-deepfake.html')

# Route for "How Does Deepfake Detection Work?"
@app.route('/How-does-deepfake-detection-work.html')
def how_does_detection_work():
    return render_template('How-does-deepfake-detection-work.html')

# Route for file upload and prediction
@app.route('/upload', methods=['POST'])
def upload():
    start_time = time.time()
    logger.debug("Received upload request")

    if 'file' not in request.files:
        logger.warning("No file part in request")
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '' or not file.filename.lower().endswith(('.jpg', '.jpeg')):
        logger.warning("Invalid file format or no file selected")
        return jsonify({'error': 'Please upload a JPG image'}), 400

    try:
        # Simulate prediction logic (randomly choose "Real" or "Fake")
        logger.debug("Processing file (simulated)")
        prediction = random.choice(['Real', 'Fake'])
        confidence = round(random.uniform(50, 100), 2)  # Random confidence between 50% and 100%
        total_time = time.time() - start_time
        logger.debug(f"Total processing time: {total_time:.2f}s")
        return jsonify({'prediction': prediction, 'confidence': str(confidence)})
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)