# 📧 Email Spam Detection using Bidirectional LSTM

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge\&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A modern **Deep Learning** web application that classifies emails as **Spam** or **Ham (Legitimate)** using a **Bidirectional LSTM Neural Network**. The application provides real-time predictions through an elegant Streamlit interface with confidence scores, spam keyword detection, prediction history, and downloadable reports.

---

## 🚀 Live Demo

🔗 **Hugging Face:** https://huggingface.co/spaces/TEJASMAURYA/Spam-mail-prediction

---

### 🏠 Home Page

<img width="422" height="792" alt="image" src="https://github.com/user-attachments/assets/8bcfce77-745a-4cd8-aea6-30a803738cc7" />


# ✨ Features

* 📧 Real-time Email Spam Detection
* 🤖 Deep Learning using Bidirectional LSTM
* ⚡ Instant Predictions
* 📊 Confidence Score
* 📈 Spam/Ham Probability Bars
* 📋 Email Statistics
* 🔍 Spam Keyword Detection
* 🕘 Recent Prediction History
* 📥 Download Prediction Report
* 🎨 Modern Glassmorphism Interface
* 🌈 Animated Gradient Background
* 📱 Responsive Design
* ⚡ Cached Model Loading
* 🛡️ Error Handling
* ☁️ Ready for Streamlit & Hugging Face Deployment

---

# 🛠 Tech Stack

| Category         | Technologies       |
| ---------------- | ------------------ |
| Programming      | Python             |
| Deep Learning    | TensorFlow, Keras  |
| Neural Network   | Bidirectional LSTM |
| Data Processing  | NumPy, Pandas      |
| Machine Learning | Scikit-learn       |
| Frontend         | Streamlit          |
| Model Format     | `.keras`           |

---

# 📂 Project Structure

```text
Email-Spam-Detection/
│
├── app.py
├── spam_lstm.keras
├── tokenizer.pkl
├── config.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Email-Spam-Detection.git
```

```bash
cd Email-Spam-Detection
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 🧠 Model Workflow

```text
Input Email
      │
      ▼
Text Cleaning
      │
      ▼
Tokenizer
      │
      ▼
Sequence Padding
      │
      ▼
Embedding Layer
      │
      ▼
Bidirectional LSTM
      │
      ▼
Dense Layer
      │
      ▼
Sigmoid Activation
      │
      ▼
Spam / Ham Prediction
```

---

# 📊 Application Workflow

1. User enters an email.
2. The text is tokenized.
3. Tokens are converted into sequences.
4. Sequences are padded to a fixed length.
5. The Bidirectional LSTM predicts the probability.
6. The app displays:

   * Spam/Ham prediction
   * Confidence score
   * Spam/Ham probabilities
   * Email statistics
   * Spam keyword analysis
   * Downloadable prediction report

---

# 📷 Application Features

✅ Beautiful Glassmorphism UI

✅ Animated Gradient Background

✅ Large Email Input Box

✅ Predict Button

✅ Clear Button

✅ Load Sample Email

✅ Confidence Score

✅ Probability Visualization

✅ Spam Keyword Detection

✅ Email Statistics

✅ Recent Predictions

✅ Download Prediction Report

---

# 📈 Future Improvements

* 🔥 BERT-based Spam Detection
* 🌍 Multi-language Support
* 📧 Gmail API Integration
* ☁️ Cloud Database
* 📱 Mobile App
* 🤖 Explainable AI (SHAP/LIME)
* 🔗 Phishing URL Detection
* 📎 Attachment Scanning

---


# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Tejansh Maurya**

🎓 B.Tech Student

💻 Machine Learning & Deep Learning Enthusiast

🤖 Passionate about AI, NLP, and Computer Vision

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

## 💙 Thank You

Thank you for visiting this repository!

If you have any suggestions or feedback, feel free to open an issue or connect with me.

Happy Coding! 🚀
