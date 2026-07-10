from pypdf import PdfReader
from Utils.logger import logger
from Utils.custom_exception import PDFQAException

def extract_pages(uploaded_file):

    try:

        logger.info(f"Reading PDF : {uploaded_file.name}")

        reader = PdfReader(uploaded_file)

        pages = []

        for page_number, page in enumerate(reader.pages):

            text = page.extract_text()

            if text:

                pages.append(
                    {
                        "page": page_number + 1,
                        "text": text,
                        "source": uploaded_file.name
                    }
                )

        if not pages:

            raise PDFQAException("No text found in PDF.")

        logger.info("PDF Read Successfully")

        return pages

    except Exception as e:

        logger.error(str(e))

        raise PDFQAException(str(e))
# "'" reader = PdfReader(uploaded_file)
# '' ' text =
# for page in reader.pages:
# page_text = page.extract_text()
#  if page_text:
# text += page_text return text ''''''