import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Configurations
st.set_page_config(page_title="Conversational Assistant", layout="wide")
st.title("Conversational Assistant")
st.sidebar.title("Settings")

# Global Variables
documents = []  # Store document texts
vectorizer = None  # Store the vectorizer
doc_vectors = None  # Store document vectors


# Function to Load PDFs
def load_pdfs(uploaded_files):
    pdf_texts = []
    for uploaded_file in uploaded_files:
        try:
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            pdf_texts.append(text)
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")
    return pdf_texts


# Function to Vectorize Documents
def vectorize_documents(doc_texts):
    global vectorizer, doc_vectors
    st.info("Vectorizing documents...")
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(doc_texts)


# Function to Search for an Answer
def search_answer(question):
    global vectorizer, doc_vectors
    if vectorizer is None or doc_vectors is None:
        st.error("No documents processed. Please upload and process documents first.")
        return None
    st.info("Processing your question...")
    question_vector = vectorizer.transform([question])
    similarities = cosine_similarity(question_vector, doc_vectors).flatten()
    most_similar_idx = similarities.argmax()
    return documents[most_similar_idx] if similarities[most_similar_idx] > 0 else "No relevant answer found."


# Sidebar for File Upload
st.sidebar.subheader("1. Upload PDF Documents")
uploaded_files = st.sidebar.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if st.sidebar.button("Process Documents"):
    if uploaded_files:
        # Load and process the uploaded files
        pdf_texts = load_pdfs(uploaded_files)
        if pdf_texts:
            documents.extend(pdf_texts)  # Append to the global documents list
            vectorize_documents(documents)  # Vectorize the documents
            st.success(f"{len(documents)} documents processed successfully!")
        else:
            st.warning("No valid text extracted from the uploaded files.")
    else:
        st.warning("No files uploaded.")


# Question Input
st.subheader("2. Ask a Question")
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question:
        answer = search_answer(question)
        st.text_area("Answer:", answer, height=200)
    else:
        st.warning("Please enter a question.")

# Footer
st.sidebar.info("Minimal dependencies assistant.")
