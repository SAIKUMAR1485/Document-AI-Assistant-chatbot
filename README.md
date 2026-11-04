# 📚 AI-Powered Document Intelligence & Question Answering System

An AI-powered chatbot that allows users to upload PDF documents and ask questions based on their content. The application uses OpenAI's API and Retrieval-Augmented Generation (RAG) to retrieve relevant information and generate accurate, document-based answers.

## 🚀 Project Overview

The Document AI Assistant simplifies the process of understanding lengthy PDF documents.

Instead of manually searching through pages, users can upload a PDF and interact with an AI chatbot to get answers to their questions.

The chatbot is designed to answer questions using information retrieved from uploaded documents rather than relying on general knowledge.

## ✨ Features

* 📄 **PDF Upload:** Upload PDF documents directly through the application.
* 🤖 **AI-Powered Chatbot:** Ask natural language questions about uploaded documents.
* 🔍 **Document Search:** Retrieve relevant information using OpenAI File Search.
* 🧠 **RAG Architecture:** Uses Retrieval-Augmented Generation to provide document-based answers.
* 💬 **Chat History:** Maintains conversation history during the session.
* 🚫 **Hallucination Control:** Instructs the AI not to answer questions using external knowledge.
* ☁️ **Cloud Deployment:** Deployable through Streamlit Community Cloud.

## 🛠️ Technologies Used

| Technology         | Purpose                               |
| ------------------ | ------------------------------------- |
| Python             | Backend programming                   |
| Streamlit          | Application interface                 |
| OpenAI API         | AI-powered responses                  |
| OpenAI File Search | Document retrieval                    |
| Vector Store       | Document indexing and semantic search |
| Python-dotenv      | Environment variable management       |
| Git & GitHub       | Version control and project hosting   |

## 🏗️ Project Structure

```text
Document_AI_Assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── services/
    ├── __init__.py
    ├── document_service.py
    └── openai_service.py
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/document-ai-assistant.git
```

### 2. Navigate to the Project Directory

```bash
cd document-ai-assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Configuration

This project requires an OpenAI API key.

1. Create an account on the OpenAI API Platform.
2. Generate an API key.
3. Create a `.env` file in the project root directory.
4. Add the following configuration:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4.1-mini
```

**Important:** Never upload your API key or `.env` file to GitHub.

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your default browser.

Local URL:

```text
http://localhost:8501
```

## 🔄 How It Works

1. **Upload Document:** The user uploads a PDF file.
2. **Document Processing:** The PDF is uploaded to OpenAI.
3. **Vector Store Creation:** The document is indexed for semantic search.
4. **User Query:** The user asks a question through the chatbot.
5. **Information Retrieval:** OpenAI File Search retrieves relevant document content.
6. **Answer Generation:** The AI model generates an answer based on the retrieved information.
7. **Display Response:** The answer is displayed in the Streamlit application.

## 🧠 Key Concepts Learned

* Generative Artificial Intelligence
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* Vector Search and Embeddings
* OpenAI API Integration
* Python Application Development
* Streamlit Development
* Cloud Deployment

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the main application file.
5. Configure your OpenAI API key using Streamlit Secrets.
6. Deploy the application.
