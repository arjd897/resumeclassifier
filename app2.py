import streamlit as st
import pickle
from PyPDF2 import PdfReader

# Load the trained model and vectorizer
with open('clas.pkl', 'rb') as file:
    classifier = pickle.load(file)
with open('vecti.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to map prediction to category
def get_category_label(prediction):
    category_map = {
        1: "Data Science Engineer",
        2: "HR",
        3: "Advocate",
        4: "Arts",
        5: "Web Developer",
        6: "Mechanical Engineer",
        7: "Sales",
        8: "Health And Fitness",
        9: "Civil Engineer",
        10: "Web Developer",
        11: "Business Analyst",
        12: "SAP",
        14: "Electrical Engineer"
    }
    return category_map.get(prediction, "Unknown Category")

# Function to preprocess and predict category
def predict_category(text):
    text_tfidf = vectorizer.transform([text])
    prediction = classifier.predict(text_tfidf)
    return get_category_label(prediction[0])

# Streamlit app interface
st.title("Resume Category Predictor")

# Option to choose between PDF upload and text input
option = st.radio("Choose input method", ("Upload PDF", "Enter Text"))

if option == "Upload PDF":
    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload a PDF resume", type="pdf")

    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        resume_text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted Text", resume_text, height=250)

        # Predict button
        if st.button("Predict"):
            category = predict_category(resume_text)
            st.write(f"The predicted category is: **{category}**")
    else:
        st.write("Please upload a PDF file.")

elif option == "Enter Text":
    # Text area for manual input
    resume_text = st.text_area("Enter resume text here", height=250)

    # Predict button
    if st.button("Predict"):
        category = predict_category(resume_text)
        st.write(f"The predicted category is: **{category}**")

# Add a link to navigate to another webpage for resume score prediction
st.markdown("[Get Your Resume Score](https://yourresumescore.streamlit.app/)", unsafe_allow_html=True)
