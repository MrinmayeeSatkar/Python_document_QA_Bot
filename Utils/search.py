from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key=GOOGLE_API_KEY
)

#def load_vector_store():

   # vector_store = FAISS.load_local(
      #  "vector_db",
      #  embeddings,
       # allow_dangerous_deserialization=True
    #)

    #return vector_store
def search_document(vector_store, question):

    results = vector_store.similarity_search(
        question,
        k=3
    )

    return results

