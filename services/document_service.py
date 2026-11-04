from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def create_vector_store():

    vector_store = client.vector_stores.create(
        name="Document AI Knowledge Base"
    )

    return vector_store.id


def upload_document(uploaded_file, vector_store_id):

    file_bytes = uploaded_file.getvalue()

    # Upload PDF to OpenAI
    file = client.files.create(
        file=(
            uploaded_file.name,
            file_bytes
        ),
        purpose="assistants"
    )

    # Add PDF to vector store
    result = client.vector_stores.files.create_and_poll(
        vector_store_id=vector_store_id,
        file_id=file.id
    )

    if result.status != "completed":
        raise Exception(
            f"Document processing failed: {result.status}"
        )

    return True