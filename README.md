# PDF-RAG-CHATBOT
A Retrievel Augmented Generation(RAG) chatbot built using langchain, OpenAIEmbeddings ,Chromadb.
This project allows users to ask questions from a PDF document using semantic search and LLM-powered responses.

## FEATURES
- PDF Document Loading
- Text-splitting
- OpenAIEmbeddings
- Chroma Vector Database
- Semantic Retrievel
- Interactive chatbot
- context-based Answering

## TECH STACK
- Python
- LangChain
- OpenAI
- ChromaDB
- PyPDF
- LCEL (LangChain Expression Language)

## PROJECT FLOW
PDF → Chunking → Embeddings → Vector Database → Retriever → Prompt → LLM → Answer

## INSTALL DEPENDENCIES
pip install -r requirements.txt

## ENVIRONMENT VARIABLES
Create a `.env` file and add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here

## RUN PROJECT
python pdf_rag_chatbot.py

## EXAMPLE QUESTIONS
- What is Indian economy?
- What are the challenges in Indian economy?
- What is the role of agriculture?
- What sectors contribute to the economy?

## FOLDER STRUCTURE
pdf-rag-chatbot/
│
├── README.md
├── pdf_rag_chatbot.py
├── requirements.txt
└── test.pdf

## FUTURE IMPROVEMENT
- Streamlit UI
- Chat memory
- Multi-PDF support
- Hybrid search
- Conversation history









