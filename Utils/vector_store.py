from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key=GOOGLE_API_KEY
)

def create_vector_store(chunks):

    texts = []
    metadatas = []

    for item in chunks:

        texts.append(item["chunk"])

        metadatas.append(
            {
                "page": item["page"],
                "source": item["source"]
            }
        )
    print(type(embeddings))
    print(embeddings)
    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    return vector_store


def save_vector_store(vector_store):

    vector_store.save_local("vector_db")


























'''''
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key=GOOGLE_API_KEY
)
def create_vector_store(chunks):

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store
def save_vector_store(vector_store):

    vector_store.save_local("vector_db")
'''''