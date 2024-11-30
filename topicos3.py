import streamlit as st
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import os
from sklearn.neighbors import NearestNeighbors

# Configurações iniciais
st.set_page_config(page_title="Assistente Conversacional Baseado em LLM", layout="wide")
st.title("Assistente Conversacional Baseado em LLM")
st.sidebar.title("Configurações")

# Variáveis Globais
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Modelo para embeddings
index = None  # Índice FAISS para busca vetorial
documents = []  # Armazena os documentos originais
embeddings = None  # Embeddings dos documentos

# Função para carregar PDFs
def carregar_pdfs(uploaded_files):
    global documents
    documentos_texto = []
    for uploaded_file in uploaded_files:
        try:
            pdf_reader = PdfReader(uploaded_file)
            texto = ""
            for page in pdf_reader.pages:
                texto += page.extract_text()
            documentos_texto.append(texto)
        except Exception as e:
            st.error(f"Erro ao processar {uploaded_file.name}: {e}")
    documents.extend(documentos_texto)
    return documentos_texto

# Initialize NearestNeighbors
def criar_indice(documentos_texto):
    global index, embeddings
    st.info("Gerando embeddings...")
    embeddings = embedding_model.encode(documentos_texto, convert_to_tensor=False)
    index = NearestNeighbors(n_neighbors=1, metric='cosine').fit(embeddings)

# Search Function
def buscar_resposta(pergunta):
    global index, documents
    if index is None:
        st.error("Índice não criado. Faça o upload de documentos primeiro.")
        return None
    st.info("Gerando embedding para a pergunta...")
    query_embedding = embedding_model.encode([pergunta], convert_to_tensor=False)
    distances, indices = index.kneighbors(query_embedding)
    if len(indices) > 0:
        resposta = documents[indices[0][0]]
        return resposta
    else:
        return "Desculpe, não encontrei uma resposta relevante."

# Interface de Upload de Arquivos
st.sidebar.subheader("1. Carregue Documentos PDF")
uploaded_files = st.sidebar.file_uploader("Faça upload dos arquivos PDF", type="pdf", accept_multiple_files=True)
if st.sidebar.button("Processar Documentos"):
    if uploaded_files:
        documentos_texto = carregar_pdfs(uploaded_files)
        criar_indice(documentos_texto)
        st.success(f"{len(documentos_texto)} documentos processados com sucesso!")
    else:
        st.warning("Nenhum arquivo carregado.")

# Interface de Perguntas
st.subheader("2. Faça sua Pergunta")
pergunta = st.text_input("Digite sua pergunta:")
if st.button("Buscar Resposta"):
    if pergunta:
        resposta = buscar_resposta(pergunta)
        st.text_area("Resposta:", resposta, height=200)
    else:
        st.warning("Por favor, insira uma pergunta.")

# Rodapé
st.sidebar.info("Assistente Conversacional desenvolvido para a tarefa AS05.")

