from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents():

    docs = []

    files = [
        "data/client_profiles.txt",
        "data/meeting_notes.txt",
        "data/action_items.txt"
    ]

    for file in files:

        with open(file, "r", encoding="utf-8") as f:

            docs.append(f.read())

    return docs


def create_vector_store():

    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []

    for doc in documents:
        chunks.extend(
            splitter.split_text(doc)
        )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(
        chunks,
        embeddings
    )

    return vectorstore