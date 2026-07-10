from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

def split_into_chunks(pages):

    all_chunks = []

    for page in pages:

        chunks = text_splitter.split_text(page["text"])

        for chunk in chunks:

            all_chunks.append(
                {
                    "page": page["page"],
                    "chunk": chunk,
                    "source": page["source"],
                }
            )

    return all_chunks

#This files has only one responsibillity
#Text
#> converts
#Chunks
