# Pneumonia Detection Using Flask and CNN  

This project is a Flask-based web application that leverages a Convolutional Neural Network (CNN) to detect pneumonia from chest X-ray images. Users can upload X-rays through a simple interface and receive instant predictions.  

---

## 🚀 Features  
- **Powerful Model**: A fine-tuned CNN for classifying chest X-ray images as *Normal* or *Pneumonia*.  
- **User-Friendly Interface**: Flask-powered web application for uploading images and displaying predictions.  
- **Robust Dataset**: Trained on a labeled dataset of X-ray images for reliable performance.  
- **Easy Deployment**: Lightweight application deployable on local machines or cloud platforms.  

---

## ⚙️ Workflow  

1. **Data Preprocessing**:  
   - Images resized and normalized for model compatibility.  

2. **Model Training**:  
   - Trained using TensorFlow/Keras to achieve high accuracy on pneumonia detection tasks.  

3. **Web Application Integration**:  
   - The trained model is integrated into a Flask app for seamless user interaction.  
   - Users upload chest X-ray images and get instant results.  

---

## 🛠️ Installation and Usage  

### 1. Clone the Repository  
```sh
git clone https://github.com/srikarr3/Pneumonia-Detection.git
cd pneumonia-detection
```
### 2. Install Dependencies
Install the required libraries using the command below:
```sh
pip install -r requirements.txt
```

### 3. Run the Application
Start the Flask app by running:
```sh
python app.py
```
### 4. Access the Web Application
Open your browser and navigate to:
```sh
http://127.0.0.1:5000
```
### Model
**For model refer this :**
```sh
https://colab.research.google.com/drive/1ccU48B4vV8xlMgi1RReunO7bAlM5a3RA#scrollTo=h7YIsf5Y3AIy
```

## 📚 Tools and Libraries  

- **Programming Language**: Python  
- **Framework**: Flask  
- **Deep Learning Libraries**: TensorFlow/Keras  
- **Additional Libraries**: OpenCV, NumPy, Matplotlib  

---

## 🙏 Acknowledgements  

Special thanks to [Kaggle and Paul Timothy Mooney](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) for providing the dataset used in this project.  

---

## 🎯 Future Enhancements  

- Add multi-class classification to detect specific types of pneumonia.  
- Implement cloud-based deployment (e.g., AWS, Heroku).  
- Integrate additional data preprocessing pipelines for real-world datasets.  

---

