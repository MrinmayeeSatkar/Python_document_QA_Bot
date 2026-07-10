import streamlit as st

from Utils.pdf_reader import extract_pages
from Utils.text_splitter import split_into_chunks
from Utils.vector_store import create_vector_store
from Utils.search import search_document
from Utils.llm import generate_answer
from Utils.logger import logger
from Utils.custom_exception import PDFQAException


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="📄 Intelligent PDF Assistant",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "pages" not in st.session_state:
    st.session_state.pages = []

if "processed" not in st.session_state:
    st.session_state.processed = False

if "uploaded_file_names" not in st.session_state:
    st.session_state.uploaded_file_names = []


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("📄 Intelligent PDF Assistant")

    st.markdown("---")

    st.subheader("📂 Uploaded PDFs")

    if st.session_state.uploaded_file_names:

        for file in st.session_state.uploaded_file_names:
            st.success(file)

    else:
        st.info("No PDF Uploaded")

    st.markdown("---")

    st.subheader("📊 Statistics")

    st.metric(
        "Documents",
        len(st.session_state.uploaded_file_names)
    )

    st.metric(
        "Pages",
        len(st.session_state.pages)
    )

    st.metric(
        "Chunks",
        len(st.session_state.chunks)
    )

    st.markdown("---")

    if st.button("🗑️ New Chat", key="new_chat"):

        st.session_state.messages = []
        st.session_state.vector_store = None
        st.session_state.chunks = []
        st.session_state.pages = []
        st.session_state.processed = False
        st.session_state.uploaded_file_names = []

        st.rerun()

    st.markdown("---")

    st.subheader("ℹ️ About")

    st.write("🤖 Model : Gemini 2.5 Flash")
    st.write("🧠 Embeddings : Gemini Embedding")
    st.write("📚 Vector Database : FAISS")
    st.write("💻 Framework : Streamlit")


# ==========================================
# MAIN PAGE
# ==========================================

st.title("🤖 Intelligent PDF Assistant")

st.write(
    "Upload one or more PDF documents and ask questions using RAG."
)


# ==========================================
# DISPLAY CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

        if message["role"] == "assistant":

            if "source" in message:

                st.caption(
                    f"📄 Source : {message['source']}"
                )

            if "page" in message:

                st.caption(
                    f"📄 Page : {message['page']}"
                )


# ==========================================
# PDF UPLOAD
# ==========================================

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)


# ==========================================
# PROCESS PDF
# ==========================================

if uploaded_files and not st.session_state.processed:

    try:

        with st.spinner("Processing PDFs..."):

            all_pages = []
            uploaded_names = []

            for pdf in uploaded_files:

                uploaded_names.append(pdf.name)

                pages = extract_pages(pdf)

                all_pages.extend(pages)

            chunks = split_into_chunks(all_pages)

            vector_store = create_vector_store(chunks)

            st.session_state.vector_store = vector_store
            st.session_state.pages = all_pages
            st.session_state.chunks = chunks
            st.session_state.uploaded_file_names = uploaded_names
            st.session_state.processed = True

        st.success("✅ PDF Processing Completed")

    except PDFQAException as e:

        logger.error(str(e))
        st.error(str(e))

    except Exception as e:

        logger.exception(str(e))
        st.error(str(e))


# ==========================================
# SHOW GENERATED CHUNKS
# ==========================================

if st.session_state.chunks:

    with st.expander("📄 View Generated Chunks"):

        for i, chunk in enumerate(st.session_state.chunks):

            st.markdown(f"### Chunk {i+1}")

            st.write(chunk["chunk"])

            st.caption(
                f"📄 {chunk['source']} | Page {chunk['page']}"
            )

            st.divider()
# ==========================================
# CHAT INPUT
# ==========================================

question = st.chat_input(
    "Ask anything about your PDFs..."
)

if question:

    # Check whether PDFs are processed
    if st.session_state.vector_store is None:

        st.warning("Please upload and process a PDF first.")

        st.stop()

    # -----------------------------
    # Display User Message
    # -----------------------------
    with st.chat_message("user"):

        st.write(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # -----------------------------
    # Build Conversation History
    # -----------------------------
    history = ""

    for msg in st.session_state.messages[-10:]:

        history += f"{msg['role']}: {msg['content']}\n"

    try:

        # -----------------------------
        # Search Relevant Chunks
        # -----------------------------
        with st.spinner("Searching documents..."):

            docs = search_document(
                st.session_state.vector_store,
                question
            )

        if len(docs) == 0:

            st.warning("No relevant information found.")

            st.stop()

        # -----------------------------
        # Generate Answer
        # -----------------------------
        with st.spinner("Generating answer..."):

            answer = generate_answer(
                question,
                docs,
                history
            )

        # -----------------------------
        # Save Assistant Response
        # -----------------------------
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "source": docs[0].metadata.get("source", "Unknown"),
                "page": docs[0].metadata.get("page", "Unknown")
            }
        )

        # -----------------------------
        # Display Assistant Response
        # -----------------------------
        with st.chat_message("assistant"):

            st.write(answer)

            st.caption(
                f"📄 Source : {docs[0].metadata.get('source', 'Unknown')}"
            )

            st.caption(
                f"📄 Page : {docs[0].metadata.get('page', 'Unknown')}"
            )

        # -----------------------------
        # Retrieved Chunks
        # -----------------------------
        with st.expander("🔍 Retrieved Chunks"):

            for i, doc in enumerate(docs):

                st.markdown(f"### Chunk {i + 1}")

                st.write(doc.page_content)

                st.caption(
                    f"📄 Source : {doc.metadata.get('source', 'Unknown')}"
                )

                st.caption(
                    f"📄 Page : {doc.metadata.get('page', 'Unknown')}"
                )

                st.divider()

    except PDFQAException as e:

        logger.error(str(e))

        st.error(str(e))

    except Exception as e:

        logger.exception(str(e))

        st.error(f"Unexpected Error: {e}")


        

