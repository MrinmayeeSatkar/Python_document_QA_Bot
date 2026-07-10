User Uploads PDF
        ↓
Read PDF
        ↓
Extract Text
        ↓
Split into Chunks
        ↓
Convert Chunks to Embeddings
        ↓
Store in Vector Database (FAISS)
        ↓
User Asks Question
        ↓
Find Most Relevant Chunks
        ↓
Send Context + Question to LLM
        ↓
Return Answer


Project Structure 
PDF_QA_Bot/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── uploads/
├── vector_db/
├── logs/
│
├── utils/
│   ├── __init__.py
│   ├── pdf_reader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── llm.py
│   ├── prompt.py
│   ├── logger.py
│   └── helper.py