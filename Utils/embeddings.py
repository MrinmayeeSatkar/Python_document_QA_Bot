from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key=GOOGLE_API_KEY
)

def create_embeddings(chunks):
    return embeddings.embed_documents(chunks)

#print("Embeddings API Key:", GOOGLE_API_KEY)