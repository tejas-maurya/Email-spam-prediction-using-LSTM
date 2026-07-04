import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import streamlit as st
import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import time

# PAGE CONFIG


st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CUSTOM CSS


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(-45deg, #0EA5E9, #38BDF8, #60A5FA, #818CF8, #A78BFA);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

.main-card {
    background: rgba(255,255,255,.12);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 35px;
    border: 1px solid rgba(255,255,255,.25);
    box-shadow: 0 15px 35px rgba(0,0,0,.35);
    margin-bottom: 20px;
}

.title {
    text-align: center;
    font-size: 46px;
    font-weight: 700;
    color: white;
    margin-bottom: 6px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    color: #F1F5F9;
    margin-bottom: 0;
}

textarea {
    font-size: 17px !important;
    border-radius: 15px !important;
}

.stButton>button {
    width: 100%;
    height: 52px;
    font-size: 16px;
    font-weight: 600;
    border: none;
    border-radius: 14px;
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    color: white;
    transition: .25s ease;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0,0,0,.35);
}

.result-card {
    padding: 26px;
    border-radius: 20px;
    color: white;
    text-align: center;
    box-shadow: 0 12px 30px rgba(0,0,0,.3);
    margin-bottom: 18px;
}

.result-card.spam {
    background: linear-gradient(135deg, #DC2626, #F97316);
}

.result-card.ham {
    background: linear-gradient(135deg, #16A34A, #22C55E);
}

.result-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 4px;
}

.result-sub {
    font-size: 15px;
    opacity: .9;
}

.metric-box {
    background: rgba(255,255,255,.9);
    border-radius: 16px;
    padding: 16px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(0,0,0,.15);
}

.keyword-chip {
    display: inline-block;
    padding: 6px 14px;
    margin: 4px;
    border-radius: 999px;
    background: linear-gradient(135deg, #DC2626, #F97316);
    color: white;
    font-size: 13px;
    font-weight: 600;
}

.footer {
    margin-top: 30px;
    text-align: center;
    color: white;
    opacity: .85;
}

hr {
    border-color: rgba(255,255,255,.25) !important;
}

</style>
""", unsafe_allow_html=True)

# LOAD MODEL


@st.cache_resource
def load_model():
    return tf.keras.models.load_model("spam_lstm.keras")

@st.cache_resource
def load_tokenizer():
    with open("tokenizer.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_config():
    with open("config.pkl", "rb") as f:
        return pickle.load(f)

try:
    model = load_model()
    tokenizer = load_tokenizer()
    config = load_config()
    MAX_LEN = config["maxlength"]
except Exception as e:
    st.error("Unable to load model files.")
    st.exception(e)
    st.stop()


# SESSION STATE

if "email_input" not in st.session_state:
    st.session_state.email_input = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None

SAMPLE_SPAM = (
    "Congratulations!\n\n"
    "You have won $5000 cash.\n\n"
    "Click here to claim your prize today.\n\n"
    "Offer expires tonight."
)

SPAM_KEYWORDS = [
    "free", "winner", "won", "cash", "money", "claim", "offer", "urgent",
    "click", "prize", "gift", "lottery", "bonus", "limited",
    "congratulations", "reward", "selected", "guaranteed"
]

def clear_email():
    st.session_state.email_input = ""
    st.session_state.last_result = None

def load_sample_email():
    st.session_state.email_input = SAMPLE_SPAM


# SIDEBAR


with st.sidebar:
    st.image(
        "https://tse1.mm.bing.net/th/id/OIP.gyNVEI2i3vFnsd9oVQXEKwHaEq?cb=thfc1falcon4&rs=1&pid=ImgDetMain&o=7&rm=3",
        width=90
    )
    st.title("Spam Detector")
    st.success("Bidirectional LSTM")
    st.markdown("---")
    st.markdown("""
**Features**

✅ Deep Learning
✅ TensorFlow
✅ Streamlit
✅ Fast Prediction
✅ Confidence Score
""")
    st.markdown("---")
    st.info("Paste an email and click **Predict**.")


# HEADER


st.markdown("""
<div class="main-card">
    <div class="title">📧 Email Spam Detection</div>
    <div class="subtitle">Detect whether an email is <b>Spam</b> or <b>Ham</b> using a Bidirectional LSTM model.</div>
</div>
""", unsafe_allow_html=True)


# INPUT AREA


st.text_area(
    "📩 Enter your Email",
    height=240,
    placeholder="Example\n\nCongratulations!\n\nYou have won a FREE iPhone.\n\nClick the link below to claim your prize.",
    key="email_input"
)

col1, col2, col3 = st.columns(3)
predict = col1.button("🚀 Predict", use_container_width=True)
col2.button("🗑 Clear", use_container_width=True, on_click=clear_email)
col3.button("📄 Load Sample", use_container_width=True, on_click=load_sample_email)

email = st.session_state.email_input

# PREDICTION
if predict:
    if email.strip() == "":
        st.warning("⚠ Please enter an email first.")
    else:
        with st.spinner("Analyzing email..."):
            time.sleep(0.6)
            try:
                sequence = tokenizer.texts_to_sequences([email])
                padded = pad_sequences(sequence, maxlen=MAX_LEN, padding="post", truncating="post")
                probability = float(model.predict(padded, verbose=0)[0][0])
            except Exception as e:
                st.error("Prediction failed.")
                st.exception(e)
                st.stop()

        is_spam = probability >= 0.5
        confidence = (probability if is_spam else 1 - probability) * 100

        st.session_state.last_result = {
            "email": email,
            "probability": probability,
            "confidence": confidence,
            "is_spam": is_spam,
        }

        st.session_state.history.insert(0, {
            "Email": email[:60] + "..." if len(email) > 60 else email,
            "Prediction": "🚨 Spam" if is_spam else "✅ Ham",
            "Confidence": f"{confidence:.2f}%"
        })
        st.session_state.history = st.session_state.history[:10]


# RESULT DISPLAY


result = st.session_state.last_result

if result:
    is_spam = result["is_spam"]
    probability = result["probability"]
    confidence = result["confidence"]
    spam_score = probability * 100
    ham_score = (1 - probability) * 100

    css_class = "spam" if is_spam else "ham"
    icon = "🚨" if is_spam else "✅"
    label = "SPAM EMAIL DETECTED" if is_spam else "HAM EMAIL DETECTED"

    st.markdown(f"""
    <div class="result-card {css_class}">
        <div class="result-title">{icon} {label}</div>
        <div class="result-sub">Confidence: {confidence:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.write("📧 **Spam Probability**")
            st.progress(min(int(spam_score), 100))
            st.write(f"{spam_score:.2f}%")
    with col2:
        with st.container(border=True):
            st.write("📨 **Ham Probability**")
            st.progress(min(int(ham_score), 100))
            st.write(f"{ham_score:.2f}%")

    st.write("")

    if is_spam:
        st.error("### 🚨 Warning\nThis email appears to be **Spam**. Avoid clicking suspicious links, downloading attachments, or sharing personal information.")
    else:
        st.success("### ✅ Safe Email\nThis email appears to be **Ham (Legitimate)**. No obvious spam characteristics were detected.")

    report = f"""======================================
 EMAIL SPAM DETECTION REPORT
======================================

Prediction : {'SPAM' if is_spam else 'HAM'}
Confidence : {confidence:.2f} %
Spam Probability : {spam_score:.2f} %
Ham Probability : {ham_score:.2f} %

--------------------------------------
Email
--------------------------------------
{result['email']}

======================================
"""
    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="spam_prediction_report.txt",
        mime="text/plain",
        use_container_width=True
    )


# TABS: ANALYSIS / MODEL INFO / TIPS & ABOUT


st.write("")
tab1, tab2, tab3 = st.tabs(["📊 Email Analysis", "🤖 Model Info", "🛡️ Tips & About"])

with tab1:
    if email.strip() == "":
        st.info("Enter an email above to see word stats and keyword analysis.")
    else:
        words = email.split()
        characters = len(email)
        spaces = email.count(" ")
        sentences = email.count(".") + email.count("!") + email.count("?")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Words", len(words))
        c2.metric("Characters", characters)
        c3.metric("Sentences", sentences)
        c4.metric("Spaces", spaces)

        st.write("")
        st.subheader("🔍 Spam Keyword Detection")

        lower = email.lower()
        found = [w for w in SPAM_KEYWORDS if w in lower]

        if not found:
            st.success("✅ No common spam keywords found.")
        else:
            chips = "".join(f'<span class="keyword-chip">{w.upper()}</span>' for w in found)
            st.markdown(chips, unsafe_allow_html=True)

        st.write("")
        with st.expander("📄 Email Preview"):
            st.write(email)

    if st.session_state.history:
        st.write("")
        st.subheader("🕘 Recent Predictions")
        for item in st.session_state.history:
            with st.container(border=True):
                c1, c2, c3 = st.columns([5, 2, 2])
                c1.write(item["Email"])
                c2.write(item["Prediction"])
                c3.write(item["Confidence"])

with tab2:
    st.markdown("""
**Architecture**
- Embedding Layer
- Bidirectional LSTM
- Dense (ReLU)
- Dense (Sigmoid)

**Framework**
- TensorFlow
- Keras
- Streamlit

**Input:** Raw Email Text
**Output:** Spam / Ham
""")
    st.write("")
    with st.expander("📄 Try Sample Emails"):
        colA, colB = st.columns(2)
        with colA:
            st.caption("Spam Example")
            st.code(
                "Congratulations!\n\nYou have won $5000 cash.\n\nClick here immediately to claim your reward.\n\nOffer expires today.",
                language="text"
            )
        with colB:
            st.caption("Ham Example")
            st.code(
                "Hello John,\n\nPlease find the meeting agenda attached.\n\nLet me know if you have any questions.\n\nRegards,\nDavid",
                language="text"
            )

with tab3:
    st.markdown("""
**How to Identify Spam Emails**

✔ Unknown sender
✔ Too good to be true
✔ Urgent payment requests
✔ Suspicious links
✔ Poor grammar
✔ Asking for passwords
✔ Lottery or prize scams
✔ Fake bank emails
""")
    st.write("")
    st.markdown("""
**About This Project**

This application uses a Bidirectional LSTM Neural Network trained on email spam data
to classify emails into ✅ Ham or 🚨 Spam. The model performs preprocessing using a
trained tokenizer and predicts the probability of spam using deep learning.
""")


# FOOTER


st.markdown("---")
st.markdown("""
<div class="footer">
    <h4>📧 Email Spam Detection using Bidirectional LSTM</h4>
    <p>Built with ❤️ using TensorFlow • Streamlit • Keras</p>
</div>
""", unsafe_allow_html=True)