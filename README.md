# TruScan--Deepfake-Image-Detection-System
TrueScan: MCA project for deepfake image detection using Vision Transformer (ViT). Achieves 92% accuracy on 200 images (100 Real, 100 Fake). Features Flask web interface for real-time predictions, built with Python, PyTorch, Transformers, Bootstrap. Includes educational pages on deepfake risks.


## Installation Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- M3 Mac with Metal Performance Shaders (MPS) recommended

### Setup
1. **Clone the Repository**:
   git clone https://github.com/KalerDiksha/TrueScan--Deepfake-Image-Detection-System.git
   cd TrueScan
   
2. **Create a Virtual Environment**:
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

3. **Install the dependencies**:
pip install -r requirements.txt
Prepare the Dataset:
Place your 200 preprocessed images (224x224 pixels, normalized) in the dataset/ folder, split into real/ and fake/ subdirectories.


4. **Run the Application**:
Activate the virtual environment (if not already active):
source myenv/bin/activate

5. **Start the Flask server**:
python app.py
Open your browser and navigate to http://localhost:5001.

6. **Upload and Predict**:
Use the web interface to upload an image.
View the prediction (e.g., "Real" or "Fake" with confidence score) in real-time.

7. **Results**:
Accuracy: 92% on the test set (80 images).
Precision: 90%.
Recall: 93%.
Visualized in fig3_training_accuracy.png, showing accuracy progression over 10 epochs.

**SDLC Flowchart**:
The development process is detailed in sdlc_flowchart.png, outlining phases from Project Initiation to Completion, including Planning, Analysis, Design, Implementation, and Deployment.

**Limitations**:
Limited dataset size (200 images) restricts generalization.
Struggles with low-resolution images (<100x100 pixels).
No real-time API; relies on batch processing.

**Future Work**:
Expand dataset to 10,000+ images for improved robustness.
Implement real-time detection with WebSocket integration.
Develop mobile apps (iOS/Android) using Flutter and ONNX runtime.
Enhance model with adversarial training against evolving deepfake techniques.
Contributing
Contributions are welcome! Please fork the repository and submit pull requests with improvements or bug fixes. For major changes, please open an issue first to discuss.

**License**:
This project is licensed under the MIT License - see the  file for details (create a LICENSE.md with MIT terms if not already present).

**Acknowledgments**:
Inspired by research from Dosovitskiy et al. (2021) on Vision Transformers.
Utilized open-source tools from PyTorch, Flask, and Bootstrap communities.
Guided by faculty at Guru Nanak Dev University.

**Contact**:
For questions or support, contact the project author:
email id: dikshakaler25@gmail.com
GitHub: KalerDiksha
