# 🔮 Next Word Prediction Keyboard using LSTM

A Deep Learning project that predicts the next word in a sentence, similar to the predictive text feature found in mobile keyboards such as Gboard and SwiftKey.

The model is built using **TensorFlow/Keras**, trained on a large text corpus, and can predict the most probable next word based on the previously typed words.

---

## 📌 Features

- Next-word prediction using Deep Learning
- LSTM-based Language Model
- Text preprocessing and tokenization
- Sequence generation for training
- Embedding Layer for word representation
- Interactive prediction interface
- Save and load trained model
- Easy to extend with larger datasets

---

## 📂 Project Structure

```
Next-Word-Prediction/
│
├── dataset/
│   └── text_dataset.txt
│
├── notebooks/
│   └── training.ipynb
│
├── models/
│   ├── next_word_model.keras
│   ├── tokenizer.pkl
│   └── max_sequence_length.pkl
│
├── app.py
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🧠 Model Architecture

```
Input Text
      │
      ▼
Text Cleaning
      │
      ▼
Tokenizer
      │
      ▼
Text Sequences
      │
      ▼
Padding
      │
      ▼
Embedding Layer
      │
      ▼
LSTM Layer
      │
      ▼
Dropout
      │
      ▼
Dense Layer (ReLU)
      │
      ▼
Output Layer (Softmax)
      │
      ▼
Predicted Next Word
```

---

## 📊 Dataset

This project can be trained on various text datasets such as:

- WikiText-2
- WikiText-103
- Penn Treebank
- OpenWebText
- Reddit Comments
- Custom text corpus

> **Recommended:** WikiText-103 for better language modeling performance.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Next-Word-Prediction.git
```

Move into the project directory:

```bash
cd Next-Word-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Training the Model

Run:

```bash
python train.py
```

After training, the model and tokenizer will be saved inside the `models/` folder.

---

## ▶️ Running the Application

Launch the prediction interface:

```bash
python app.py
```

or, if using Streamlit:

```bash
streamlit run app.py
```

---

## 💬 Example

### Input

```
Machine learning is
```

### Output

```
transforming
```

---

### Input

```
Deep learning models
```

### Output

```
can
```

---

## 🧪 Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn
- Pickle
- Streamlit (optional)

---

## 📈 Future Improvements

- Bidirectional LSTM
- GRU implementation
- Transformer-based language model
- Beam Search decoding
- Top-K and Top-P sampling
- Attention mechanism
- Mobile keyboard integration
- Multilingual prediction
- Personalized prediction
- Real-time typing suggestions

---

## 📸 Screenshots

Add screenshots of:

- Home page
- Prediction interface
- Training accuracy and loss graphs
- Sample predictions

---

## 📊 Performance

Evaluate the model using:

- Training Accuracy
- Validation Accuracy
- Cross-Entropy Loss
- Perplexity
- Top-1 Accuracy
- Top-5 Accuracy

---


## 👨‍💻 Author

**Tejansh Maurya**

Feel free to connect and contribute to improve this project!
