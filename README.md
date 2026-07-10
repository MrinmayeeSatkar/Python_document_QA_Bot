# 🤖 Intelligent PDF Assistant (RAG-based PDF Question Answering)

An AI-powered PDF Question Answering application built using **Python, Streamlit, LangChain, Google Gemini 2.5 Flash, and FAISS**.

This application allows users to upload one or more PDF documents and ask natural language questions. It retrieves the most relevant content from the uploaded documents using Retrieval-Augmented Generation (RAG) and generates accurate responses with Google Gemini.

---

## 📌 Features

* 📄 Upload one or multiple PDF documents
* 🔍 Semantic search using FAISS Vector Database
* 🤖 AI-powered question answering with Gemini 2.5 Flash
* 🧠 Retrieval-Augmented Generation (RAG)
* 💬 Interactive chat interface
* 📚 Conversation history support
* 📍 Source document and page number references
* 📑 Automatic text chunking
* ⚡ Fast document retrieval
* 📝 Application logging
* ⚠️ Custom exception handling
* 🧩 Modular project architecture

---

## 🏗️ Project Architecture

```
PDF_QA_BOT/
│
├── Utils/
│   ├── custom_exception.py
│   ├── logger.py
│   ├── pdf_reader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   ├── search.py
│   ├── llm.py
│   └── __init__.py
│
├── Input/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Tech Stack

| Category              | Technology                              |
| --------------------- | --------------------------------------- |
| Programming Language  | Python                                  |
| Frontend              | Streamlit                               |
| LLM                   | Google Gemini 2.5 Flash                 |
| Embedding Model       | Gemini Embedding (gemini-embedding-001) |
| Framework             | LangChain                               |
| Vector Database       | FAISS                                   |
| PDF Processing        | PyPDF                                   |
| Logging               | Python Logging Module                   |
| Environment Variables | python-dotenv                           |

---

## 🚀 How It Works

1. Upload one or more PDF documents.
2. Extract text from each PDF.
3. Split text into smaller chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in a FAISS vector database.
6. Ask questions in natural language.
7. Perform similarity search to retrieve relevant chunks.
8. Send retrieved context to Gemini 2.5 Flash.
9. Display the generated answer along with the source document and page number.

---

## 📂 Installation

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/intelligent-pdf-assistant.git
```

Navigate to the project:

```bash
cd intelligent-pdf-assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Features

* Multi-PDF Upload
* PDF Text Extraction
* Intelligent Chunking
* Vector Embeddings
* Semantic Search
* AI-powered Question Answering
* Conversation Memory
* Chat Interface
* Source Citations
* Logging
* Error Handling

---

## 📈 Future Enhancements

* OCR support for scanned PDFs
* Support for Word, Excel and PowerPoint documents
* Persistent chat history
* User authentication
* Database integration
* Docker deployment
* Cloud deployment
* Streaming AI responses
* Hybrid search (Keyword + Vector Search)

---

## 🧪 Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Large Language Model Integration
* Prompt Engineering
* Vector Databases
* Semantic Search
* Document Processing
* Python Application Development
* Streamlit UI Development
* Exception Handling
* Logging
* Modular Software Design

---

## 🤝 Contributing

Contributions, suggestions and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is intended for learning and portfolio purposes.

---

## 👩‍💻 Author

**Mrinmayee Satkar**

Python Developer | RPA Developer | GenAI Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.
