import streamlit as st

from services.document_service import (
    create_vector_store,
    upload_document
)

from services.openai_service import ask_question


# Page configuration

st.set_page_config(
    page_title="Document AI Assistant",
    page_icon="📚"
)


# Application title

st.title("📚 Document AI Assistant")

st.write(
    "Upload a PDF and ask questions based on its content."
)


# Initialize session state

if "vector_store_id" not in st.session_state:

    st.session_state.vector_store_id = None


if "messages" not in st.session_state:

    st.session_state.messages = []


# PDF Upload section

st.subheader("Upload Your Document")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


# Process document

if st.button("Process Document"):

    if uploaded_file is None:

        st.warning("Please upload a PDF first.")

    else:

        if uploaded_file.size > 20 * 1024 * 1024:

            st.error("File size must be below 20 MB.")

        else:

            try:

                with st.spinner(
                    "Processing your document..."
                ):

                    # Create vector store

                    if not st.session_state.vector_store_id:

                        st.session_state.vector_store_id = (
                            create_vector_store()
                        )

                    # Upload document

                    upload_document(
                        uploaded_file,
                        st.session_state.vector_store_id
                    )

                    st.success(
                        "Document processed successfully!"
                    )

                    st.session_state.messages = []

            except Exception as e:

                st.error(f"Error: {e}")


st.divider()


# Chatbot section

st.subheader("Ask Questions")


# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# Chat input

question = st.chat_input(
    "Ask something about your document..."
)


if question:

    if not st.session_state.vector_store_id:

        st.warning(
            "Please upload and process a document first."
        )

    else:

        # Display user question

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)


        # Generate AI response

        with st.chat_message("assistant"):

            with st.spinner("Searching your document..."):

                try:

                    answer = ask_question(
                        question,
                        st.session_state.vector_store_id
                    )

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except Exception as e:

                    st.error(f"Error: {e}")


# Clear chat history

if st.button("Clear Chat"):

    st.session_state.messages = []

    st.rerun()