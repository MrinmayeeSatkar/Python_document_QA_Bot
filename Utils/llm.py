from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=GOOGLE_API_KEY,
    temperature=0.2
)


def generate_answer(question, docs, history):

    # Combine retrieved document chunks
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # Build the prompt
    final_prompt = f"""
You are an AI assistant that answers questions only from the uploaded PDF documents.

Conversation History:
{history}

Document Context:
{context}

Current Question:
{question}

Instructions:
1. Answer ONLY using the document context.
2. Use the conversation history only to understand follow-up questions.
3. If the answer is not present in the document context, reply exactly:
"I couldn't find that information in the uploaded PDF."
4. Do not make up information.
5. Give clear and concise answers.
"""

    # Generate response
    response = llm.invoke(final_prompt)

    return response.content